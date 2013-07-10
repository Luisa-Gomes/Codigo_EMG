# -*- coding: utf-8 -*-
"""file to process plots from data"""

from numpy import loadtxt
import pylab as plab
import novainstrumentation as ni
from scipy import signal
import os
import process_aplic1 as pro
import dictionary as dic
#import matplotlib.pyplot as plt
#import matplotlib.lines

#Constants:
FA, INTERVALO, LIMIT = dic.calculos()


#space left, bottom, right, top, wspace, hspace
SL = 0.10
SB = 0.1
SR = 0.95
ST = 0.95
SW = 0.3
SH = 0.6


#DIRECT = '..\\..\\Data_Ap2\\' #Data folder is in Documents folder
#DIRECTORY_TO_SAVE = 'Plots_Ap1\\'#Folder to save all plots



MOMENTO1, MOMENTO2, POSICAO1, POSICAO2, NUMERO_COLUNAS, NUMERO_DE_FICHEIROS = dic.aplicacao1()


instrucao = dic.dicionario()

def abrir_ficheiro(directoria_open):
    """AUTOMATIC OPENING FILES"""
    for moment in range(MOMENTO1, MOMENTO2 + 1): #search each moment
        for sujeito in range(0, len(instrucao)): #search each subject
            iniciais = instrucao.keys()[sujeito]
            c_emg = instrucao.get(iniciais).values()[0][0]
            c_pos = instrucao.get(iniciais).values()[0][1]
            c_tor = instrucao.get(iniciais).values()[0][2]
            directoria = instrucao.get(iniciais).values()[3]
            for s_file in range(POSICAO1, POSICAO2 + 1): 
                
                nome = 'M' + str(moment) + '_' + iniciais + '_ESQ_ISOM_' + str(s_file) + '_BF'
                if(os.path.isfile(directoria_open + nome + '.txt')): #if file exists
                    load = loadtxt(directoria_open + nome+ '.txt')
                    plotscanais(nome +'_canais', load, c_emg, c_pos, c_tor,directoria)
                    filtro(nome +'_filtro', load, 10.0, directoria)
                   
                 
def plotscanais(nome, load, C_EMG, C_POS, C_TOR, DIRECTORY_TO_SAVE):
    """function to show all important signals with plots"""
    picture = plab.figure() #opening a figure to save later
    
    emg = load[:, C_EMG]
    posicao = load[:, C_POS]
    torque = abs(load[:, C_TOR])
    
    results = pro.calculo_valores(load, C_EMG, C_POS, C_TOR)
    
    axisy = results[0].values()[0] #Fmax calculated
    
    for i in range(0, len(torque)):
        if (torque[i]>=axisy):
            tempo = i    
    
    axisx = tempo #time calculated #not right
    
    #EMG plot
    plab.subplot(3, 1, 1)
    
    arrow = picture.add_subplot(311)     
    arrow.annotate('Tempo', xy = (axisx, 0), xytext = (axisx, 0),
                arrowprops = dict(color='red', shrink = 0.5),
                horizontalalignment = 'center', verticalalignment = 'bottom',)
    arrow.annotate('', xy = (axisx + 150, 0), xytext = (axisx, 0),
                arrowprops = dict(shrink = 0.5))
    arrow.annotate('', xy = (axisx - 150, 0), xytext = (axisx, 0), 
                arrowprops = dict(shrink = 0.5))
    
    plab.plot(emg)
    plab.title('EMG', fontsize=10)
    plab.xlabel('Tempo', fontsize=8)
    plab.ylabel('Amplitude', fontsize=8)
    
    #Position plot
    plab.subplot(3, 1, 2)
    
    arrow = picture.add_subplot(312)   
    axish = results[3].values()[0]
    

    arrow.annotate('Tempo', xy = (axisx, axish), xytext = (axisx, axish), 
                arrowprops = dict(color='red', shrink = 0.5), 
                horizontalalignment = 'center', verticalalignment = 'bottom',)
    arrow.annotate('', xy = (axisx + 150, axish), xytext = (axisx, axish), 
                arrowprops = dict(shrink = 0.5))
    arrow.annotate('', xy = (axisx - 150, axish), xytext = (axisx, axish), 
                arrowprops = dict(shrink = 0.5))
   
    posicao[-1] = posicao[-2] 
    #This removes the last point that appears to be incorrect. 
    
    plab.plot(posicao)
    plab.title('Posicao', fontsize = 10)
    plab.xlabel('Tempo', fontsize = 8)
    plab.ylabel('Graus', fontsize = 8)
    
    #Force plot
    plab.subplot(3, 1, 3)
    
    arrow = picture.add_subplot(313)     
    arrow.annotate('Fmax', xy = (axisx, axisy), xytext = (axisx, axisy), 
                arrowprops = dict(color='red', shrink = 0.5),
                horizontalalignment = 'center', verticalalignment = 'bottom',)
    arrow.annotate('', xy = (axisx + 150, axisy), xytext = (axisx, axisy), 
                arrowprops = dict(shrink = 0.5))
    arrow.annotate('', xy = (axisx - 150, axisy), xytext = (axisx, axisy), 
                arrowprops = dict(shrink = 0.5))
    
    plab.plot(torque)
    plab.title('Momento de Forca Corrigido para a Gravidade', fontsize = 10)
    plab.ylim((min(torque) - 10, max(torque) + 60))
    plab.xlabel('Tempo', fontsize = 8)
    plab.ylabel('Torque', fontsize = 8)
    
    #space between plots    
    plab.subplots_adjust(SL, SB, SR, ST, SW, SH)
    
    picture.savefig(DIRECTORY_TO_SAVE + nome + '.pdf')



def filtro(nome, load, freq, DIRECTORY_TO_SAVE):
    """function to show signals (original and filtrated) in time or as FFT"""
    
    freqs = FA
    picture = plab.figure()
    
    #filters
    emg = load[:, 6]
    freqs = float(freqs)/2.0
    filt = ni.bandstop(emg, 49.5, 50.5, 4, fs=freqs) 
    bfilt, afilt = signal.butter(4, freq / freqs, btype = 'highpass')
    filtrado = signal.lfilter(bfilt, afilt, filt)
    
   #plots: Signals and time - original and filtrated
    plab.subplot(2, 2, 1)
    plab.plot(filtrado)
    plab.title('EMG Filtrado', fontsize=10)
    plab.xlabel('Tempo', fontsize=8)
    plab.ylabel('Amplitude', fontsize=8)
    
    plab.subplot(2, 2, 2)
    plab.plot(emg)
    plab.title('EMG Original', fontsize=10)
    plab.xlabel('Tempo', fontsize=8)
    plab.ylabel('Amplitude', fontsize=8)
        
        
    #plots: FFTsignals - original and filtrated
    plab.subplot(2, 2, 3)
    ni.plotfft(emg, FA)
    plab.title('FFT do Emg original', fontsize=10)
    plab.xlabel('Frequencia', fontsize=8)
    plab.ylabel('Amplitude', fontsize=8)
    plab.subplot(2, 2, 4)
    ni.plotfft(filtrado, FA)
    plab.title('FFT do Emg Filtrado', fontsize=10)
    plab.xlabel('Frquencia', fontsize=8)
    plab.ylabel('Amplitude', fontsize=8)
    
    plab.subplots_adjust(SL, SB, SR, ST, SW, SH)    
    
    picture.savefig(DIRECTORY_TO_SAVE + nome + '.pdf')
    



