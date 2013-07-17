# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:45:30 2013

@author: Ana Luisa Gomes
"""

import pylab as py
import novainstrumentation as ni
from scipy import signal
import code.execute_aplic1 as exec1
import conf as conf

FA = conf.FA
INTERVALO = conf.INTERVALO
LIMIT = conf.LIMIT
FREQ1 = conf.FREQ1
FREQ2 = conf.FREQ2
FREQ_HIGHPASS = conf.FREQ_HIGHPASS

    
def filtro(sign, freq, freqs = FA):
    """Filters"""
    freqs = float(freqs)/2.0
    if (conf.FILTRO50):
        filtr = ni.bandstop(sign, FREQ1, FREQ2, 4, fs = freqs)
    else:
        filtr = sign
    bfilt, afilt = signal.butter(4, freq / freqs, btype='highpass')
    return signal.lfilter(bfilt, afilt, filtr)



def calculo_valores(directoria, iniciais, all_sign, c_trigger, c_emg, c_pos, c_tor):
    """function which calculates all values we want"""
    signal_trigger = all_sign[:, c_trigger]   
    signal_emg = all_sign[:, c_emg]
    signal_posicao = all_sign[:, c_pos]
    signal_torque = all_sign[:, c_tor]
    
    filtrado = filtro(signal_emg, FREQ_HIGHPASS)
    
    signal_torque = abs(signal_torque)
    
    results = [] #vector will have all calculated values
    
    
    #Maximum Force value
    
    forca_max = max(signal_torque)
    
    for i in range(0, len(signal_torque)): #search time of Fmax
        if (signal_torque[i]>=forca_max):
            tempo = i
    
    
#function criteria to find the best Fmax
    
  # for a in range(0, len(signal_torque)):
  #      if (abs(signal_torque[tempo-INTERVALO/2]-signal_torque[tempo])>=LIMIT 
  #      or abs(signal_torque[tempo+INTERVALO/2]-signal_torque[tempo])>=LIMIT):
  #          del signal_torque[tempo]
  #          forca_max=max(signal_torque)
  #          for i in range(0, len(signal_torque)): #search time of Fmax
  #              if (signal_torque[i]>=forca_max):
  #                  tempo = i 
                    
                    
    results += [{'Fmax (N.m)': forca_max}]
    
    
    #Time interval value
    
    interval = py.find(signal_torque>conf.TRESH)
    tempo_10m = interval[0]
    intervalo_de_tempo = tempo-tempo_10m
    
    results += [{'Tempo (ms)': intervalo_de_tempo}]
    
    #Criteria to find trigger signal

    for s_tri in range(0, len(signal_trigger)-10)  :
        if (abs(signal_trigger[s_tri]-signal_trigger[s_tri+10])>2.5):
            sample = abs(tempo - s_tri)
    results += [{'Sample US (ms)': sample}]
    
    #Time interval values
    if(tempo>INTERVALO/2):
        t_0 = tempo - INTERVALO / 2
    else:
        t_0 = 0      
    t_1 = tempo + INTERVALO/2
    
    #Fmean (intervalo : 300 ms)
    results += [{'Fmed (N.m)': py.mean((signal_torque[t_0:t_1]))}]
    
    #Medium Position
    results += [{'Angulo Medio': py.mean(signal_posicao[t_0:t_1])}]

    #Root Mean Square (RMS)
    results += [{'RMS': float(py.sqrt(sum(filtrado[t_0:t_1]**2))/INTERVALO)}]
    rms_int = float(py.sqrt(sum(filtrado[t_0:t_1]**2))/INTERVALO)   
    
    aplicacao1 = exec1.valores_aplicacao2(directoria, iniciais, c_emg, c_pos, c_tor)

    
    #Contribuition force and Total Force:

    
    contribuicao = (aplicacao1[0]*rms_int)/aplicacao1[1]
    results += [{'Contribuicao da Forca': contribuicao}]
    
        
    results += [{'Forca Total': forca_max + contribuicao}]
  
    
    return results
    
    

