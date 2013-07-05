# -*- coding: utf-8 -*-
"""
Created on Tue Jul 02 16:14:14 2013

@author: Luisa
"""


import pylab as py
import novainstrumentation as ni
from scipy import signal
import xlwt


#Constants
FA = 1000.0 #sampling frequency
INTERVALO = 300.0 #interval to calculate Fmed
JANELA_RMS = 30.0

#Channels
C_EMG = 6
C_POS = 9
C_TOR = 7

DIRECT = 'Analysis\\'# Data folder is in Documents file


def filtro(sign, freq, freqs = FA):
    """Filters"""
    freqs = float(freqs)/2.0
    filtr = ni.bandstop(sign, 49.5, 50.5, 4, fs = freqs)
    bfilt, afilt = signal.butter(4, freq / freqs, btype='highpass')
    return signal.lfilter(bfilt, afilt, filtr)




def calculo_valores(all_sign):
    """function which calculates all values we want"""
    signal_emg = all_sign[:, C_EMG]
    signal_posicao = all_sign[:, C_POS]
    signal_torque = all_sign[:, C_TOR]
    
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
    
    results += [{'Tempo (ms)': tempo}]
    #Tempo=argmax(Torque) -ESTA FUNCAO DA VALORES ERRADOS!!
    
    #Time interval values
    if(tempo>INTERVALO/2):
        t_0 = tempo - INTERVALO / 2
    else:
        t_0 = 0      
    t_1 = tempo + INTERVALO/2
    
    #Fmean (intervalo : 300 ms)
    results += [{'Fmed (N.m)': py.mean((signal_torque[t_0:t_1]))}]
    
    #Root Mean Square (RMS)
    results += [{'RMS': float(py.sqrt(sum(filtrado[t_0:t_1]**2))/INTERVALO)}]
    rms_int = float(py.sqrt(sum(filtrado[t_0:t_1]**2))/INTERVALO)
    #rms_int2=mean(rms[t0:t1])
    
    #Medium Position
    results += [{'Angulo Medio': py.mean(signal_posicao[t_0:t_1])}]
    
    #EMG_100%
    results += [{'EMG_100%': filtrado[tempo]}]
    emg_100 = filtrado[tempo]
    
    #Total Force
    results += [{'Forca Total': forca_max + ((forca_max*rms_int)/emg_100)}]
    return results
    

def guardar_excel(nome, results):
    """save all values in a excel document"""
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    
    sheet.write(0, 0, 'Descricao') 
    sheet.write(0, 1, 'Valores') 

    i = 0
    #for que escreve os valores obtidos 
    for line in range(1, len(results) + 1):
        sheet.write(line, 0, results[i].keys()[0])
        sheet.write(line, 1, str(results[i].values()[0]))
        i= i + 1   
        
    wbk.save(DIRECT + str(nome) +'.xls')


