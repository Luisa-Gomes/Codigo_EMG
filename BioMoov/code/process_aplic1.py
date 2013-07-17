# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:45:30 2013

@author: Ana Luisa Gomes
"""

import pylab as py
import novainstrumentation as ni
from scipy import signal
import conf as conf



#Constants
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




def calculo_valores(all_sign, c_emg, c_pos, c_tor):
    """function which calculates all values we want"""
    signal_emg = all_sign[:, c_emg]
    signal_posicao = all_sign[:, c_pos]
    signal_torque = all_sign[:, c_tor]

    
    filtrado = filtro(signal_emg, FREQ_HIGHPASS)
    
    signal_torque = abs(signal_torque)
    
    results = [] #vector will have all calculated values
    
    
    #Maximum Force value
    results += [{'Fmax (N.m)': max(signal_torque)}]
    forca_max = max(signal_torque)
    
    #Time value
    for i in range(0, len(signal_torque)):
        if (signal_torque[i]>=forca_max):
            tempo = i
    
    #we want the time interval between F=10Nm and Fmax  
    limite = py.find(signal_torque>conf.TRESH)
    tempo_10m = limite[0]
    intervalo_de_tempo = tempo - tempo_10m
    results += [{'Tempo (ms)': intervalo_de_tempo}]
    
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
        
    
    return results
    

