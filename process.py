# -*- coding: utf-8 -*-
"""
Created on Tue Jul 02 16:14:14 2013

@author: Luisa
"""


from base64 import *
from scipy import stats
from numpy import *
from pylab import *
from novainstrumentation import *
import novainstrumentation as ni
from scipy import *
import scipy.interpolate as si
from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.lines
import scipy as scipy
from scipy import signal
import xlwt
#import process as process

#Constantes

FA = 1000.0 #frequencia de amostragem
INTERVALO = 300.0 #intervalo de milissegundos para achar a forca maxima media
JANELA_RMS = 30.0



'''
for a in range(0,101): #ver cada sujeito
    for b in range(0,101): #ver cada ficheiro de cada sujeito
    
        if(os.path.isfile('M'+str(a)+'_MB_ESQ_ISOM_'+str(b)+'.txt')):
            f = open("M"+str(a)+"_MB_ESQ_ISOM_" +str(b) +".txt", "r")
            
           # process.
            
            
            a=loadtxt('M'+str(a)+'_MB_ESQ_ISOM_'+str(b)+'.txt')
            nome='M'+str(a)+'_MB_ESQ_ISOM_'+str(b)+'.txt'
    #f.close()
  ''' 


f = open("M5_MB_ESQ_ISOM_30.txt", "r")
a=loadtxt('M5_MB_ESQ_ISOM_30.txt')
f.close()

#labels do primeiro ficheiro
#Torque     0      
#Velocidade 1     
#Posicao    2    
#Trigger    3     
#Estimulacao4     
#EMG BF     5 <-   
#Torque     6     
#Velocidade 7     
#Posicao    8     
#Radianos   9     
#Factor Correccao 10
#Torque Corrigido 11 <-
#EMG B 12






#FILTROS

#fft do sinal - 50Hz presentes     
#plotfft(Emg,FA)
#figure()
#t=arange(len(Emg))/FA
#Emg=sin(2*pi*50*t)



#filtros dimensionados
def filtro(s,f, order=2, fs=FA, use_filtfilt=True):
    
     fs=float(fs)/2.0
     g=bandstop(s,49.5,50.5,4,fs=fs) 
     b, a = signal.butter(4, f / fs, btype='highpass')
     return signal.lfilter(b, a, g)






def calculo_valores():
    #guardar os 3 canais importantes em 3 vectores
    Emg=a[:,6] #6 ou 14 ver diferenca, qual uso agora?
    Posicao=a[:,9]
    Torque=a[:,7] # canal 15 e o torque rectificado
    
    filtrado=filtro(Emg,10.0)
 
    
    results=[] #vector que vai ter todos os valores obtidos na analise do sinal
    
    #Calculo do Valor de Forca Maxima - Fmax
    results += [{'Fmax (N.m)': max(Torque)}]
    Fmax=max(Torque)
    
    #Retirar valor de tempo correspondente a Fmax
    results += [{'Tempo (ms)': argmax(Torque)}]
    Tempo=argmax(Torque)
    
    #FCalcular intervalo de tempo:
    
    if(Tempo>INTERVALO/2):
       t0=Tempo-INTERVALO/2
    else:
       t0=0      
    t1=Tempo+INTERVALO/2
    
    #Calculo do Valor de Forca Media - Fmean (com intervalo do 300 ms)
    results += [{'Fmed (N.m)': mean(Torque[t0:t1])}]
    
    #Calculo Root Mean Square (RMS)
    results += [{'RMS': float(sqrt(sum(filtrado[t0:t1]**2))/INTERVALO)}]
    rms_int=float(sqrt(sum(filtrado[t0:t1]**2))/INTERVALO)
    #rms_int2=mean(rms[t0:t1])
    
    #Calculo da posicao media
    results += [{'Angulo Medio': mean(Posicao[t0:t1])}]
    
    #Calculo de EMG_100%
    results += [{'EMG_100%': filtrado[Tempo]}]
    emg_100=filtrado[Tempo]
    
    #Calculo do Incremento de Forca e da Forca Total
    results += [{'Forca Total': Fmax+((Fmax*rms_int)/emg_100)}]
    return results
    




#Colocar valores em doc Excel

def guardar_excel(nome):
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    
    #primeiro linha depois coluna (comeca em 0)
    sheet.write(0,0,'Descricao') 
    sheet.write(0,1,'Valores') 

    results=calculo_valores()

    i=0
    for l in range(1,len(results)+1): #for que escreve os valores obtidos 
        sheet.write(l,0,results[i].keys()[0])
        sheet.write(l,1,str(results[i].values()[0]))
        i=i+1
        
    #salvar em doc excel
    wbk.save(str(nome)+'.xls')





#fazer automatico com for onde nome toma um nome proprio
nome='../data/M5_MB_ESQ_ISOM_30'
guardar_excel(str(nome))

