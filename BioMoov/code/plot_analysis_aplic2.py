# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:45:30 2013

@author: Ana Luisa Gomes
"""


from numpy import loadtxt
import pylab as plab
import novainstrumentation as ni
from scipy import signal
import os
import code.process_aplic2 as pro
import conf as conf


FA = conf.FA
INTERVALO = conf.INTERVALO
LIMIT = conf.LIMIT

MOMENTO1 = conf.AP2_MOM1
MOMENTO2 = conf.AP2_MOM2
POSICAO1 = conf.AP2_POS1
POSICAO2 = conf.AP2_POS2
NUMERO_COLUNAS = 7

INSTRUCAO = conf.SUJEITOS


#space left, bottom, right, top, wspace, hspace
SL = 0.10
SB = 0.1
SR = 0.95
ST = 0.95
SW = 0.3
SH = 0.6


def abrir_ficheiro(directoria_open):
    """AUTOMATIC OPENING FILES"""
    for moment in range(MOMENTO1, MOMENTO2 + 1): #search each moment
        for sujeito in range(0, len(INSTRUCAO)): #search each subject
            iniciais = INSTRUCAO.keys()[sujeito]
            c_tri = INSTRUCAO.get(iniciais).values()[0][0]
            c_emg = INSTRUCAO.get(iniciais).values()[0][1]
            c_pos = INSTRUCAO.get(iniciais).values()[0][2]
            c_tor = INSTRUCAO.get(iniciais).values()[0][3]
            dire = directoria_open+"\\Files_Plots"
            if not(os.path.exists(dire)):
                os.mkdir( dire)
            for s_file in range(POSICAO1, POSICAO2 + 1): 
                nom = 'M' + str(moment) + '_'
                nom = nom + iniciais + '_ESQ_ISOM_' + str(s_file)
                if(os.path.isfile(directoria_open + '/' +nom + '.txt')): 
                    #if file exists
                    load = loadtxt(directoria_open + '/' + nom + '.txt')
    
                    plotscanais(nom + '_canais', iniciais, load, c_tri, c_emg, c_pos, c_tor, directoria_open, dire)
                    filtro(nom +'_filtro', load, conf.FREQ_HIGHPASS, dire)
               
                 
def plotscanais(nome, iniciais, load, c_trigger, c_emg, c_pos, c_tor, directoria_open, directoria):
    """function to show all important signals with plots"""
    picture = plab.figure() #opening a figure to save later
    
    emg = load[:, c_emg]
    posicao = load[:, c_pos]
    torque = abs(load[:, c_tor])
    
    
    results = pro.calculo_valores(directoria_open, iniciais, load, c_trigger, c_emg, c_pos, c_tor)
    
    
    
    axisy = results[0].values()[0] #Fmax calculated
    
    for i in range(0, len(torque)):
        if (torque[i]>=max(torque)):
            tempo = i    
 
    
    axisx = tempo #time calculated
    
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
    axish = results[3].values()[0] #position value
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
    
    picture.savefig(directoria + '/' + nome + '.pdf')



def filtro(nome, load, freq, directoria):
    """function to show signals (original and filtrated) in time or as FFT"""
    
    freqs = FA
    picture = plab.figure()
    
    #filters
    emg = load[:, 6]
    freqs = float(freqs)/2.0
    if (conf.FILTRO50):
        filt = ni.bandstop(emg, conf.FREQ1, conf.FREQ2, 4, fs = freqs)
    else:
        filt = load
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
    
    picture.savefig(directoria + '/' + nome + '.pdf')
    
 

