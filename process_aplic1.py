# -*- coding: utf-8 -*-
"""
Created on Tue Jul 02 16:14:14 2013

@author: Luisa
"""


import pylab as py
import novainstrumentation as ni
from scipy import signal
import dictionary as dic



#Constants
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
    results += [{'Fmax (N.m)': max(signal_torque)}]
    forca_max = max(signal_torque)
    
    #Time value
    for i in range(0, len(signal_torque)):
        if (signal_torque[i]>=forca_max):
            tempo = i
    
    #we want the time interval between F=10Nm and Fmax  
    limite = py.find(signal_torque>10)
    tempo_10m = limite[0]
    intervalo_de_tempo = tempo - tempo_10m
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
    #rms_int = float(py.sqrt(sum(filtrado[t_0:t_1]**2))/INTERVALO)
    #rms_int2=mean(rms[t0:t1])
    
    
    
    #EMG_100%
    #results += [{'EMG_100%': filtrado[tempo]}]
    #emg_100 = filtrado[tempo]
    
    #Contribuition force and Total Force - apenas usada na segunda aplicacao:
    #results += [{'Contribuicao da Forca': ((forca_max*rms_int)/emg_100)}]
        
    #results += [{'Forca Total': forca_max + ((forca_max*rms_int)/emg_100)}]
    return results
    

