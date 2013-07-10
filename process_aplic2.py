# -*- coding: utf-8 -*-
"""
Created on Mon Jul 08 12:37:34 2013

@author: Luisa
"""



import pylab as py
import novainstrumentation as ni
from scipy import signal
import execute_aplic1 as exec1
import dictionary as dic


FA, INTERVALO, LIMIT = dic.calculos()
    
def filtro(sign, freq, freqs = FA):
    """Filters"""
    freqs = float(freqs)/2.0
    filtr = ni.bandstop(sign, 49.5, 50.5, 4, fs = freqs)
    bfilt, afilt = signal.butter(4, freq / freqs, btype='highpass')
    return signal.lfilter(bfilt, afilt, filtr)


def calculo_valores(all_sign, c_emg, c_pos, c_tor):
    """function which calculates all values we want"""
    signal_emg = all_sign[:, c_emg]
    signal_posicao = all_sign[:, c_pos]
    signal_torque = all_sign[:, c_tor]
    
    filtrado = filtro(signal_emg, 10.0)
    
    signal_torque = abs(signal_torque)
    
    results = [] #vector will have all calculated values
    
    
    #Maximum Force value
    
    forca_max = max(signal_torque)
    
    for i in range(0, len(signal_torque)): #search time of Fmax
        if (signal_torque[i]>=forca_max):
            tempo = i
    
    #tempo2=tempo #varaivel utilizada para o ciclo seguinte    
    
    
    """
   for a in range(0, len(signal_torque)):
        if (abs(signal_torque[tempo-INTERVALO/2] - signal_torque[tempo]) >= LIMIT 
        or abs(signal_torque[tempo+INTERVALO/2] - signal_torque[tempo]) >= LIMIT):
            del signal_torque[tempo]
            forca_max=max(signal_torque)
            for i in range(0, len(signal_torque)): #search time of Fmax
                if (signal_torque[i]>=forca_max):
                    tempo = i """
                    
                    
    results += [{'Fmax (N.m)': forca_max}]
    
    
    #Time interval value
    interval = py.find(signal_torque>10)
    tempo_10m = interval[0]
    intervalo_de_tempo = tempo-tempo_10m
    
    results += [{'Tempo (ms)': intervalo_de_tempo}]
    #Tempo=argmax(Torque) -ESTA FUNCAO DA VALORES ERRADOS!!
    
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
    
    
    aplicacao1 = exec1.valores_aplicacao2(c_emg, c_pos, c_tor)
    #Contribuition force and Total Force - apenas usada na segunda aplicacao:
    contribuicao = (aplicacao1[0]*rms_int)/aplicacao1[1]
    results += [{'Contribuicao da Forca': contribuicao}]
    
        
    results += [{'Forca Total': forca_max + contribuicao}]
  
    #print results
    return results
    
    

