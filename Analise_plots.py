# -*- coding: utf-8 -*-

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

#Constantes

FA = 1000.0 #frequencia de amostragem
INTERVALO = 300.0 #intervalo de milissegundos para achar a forca maxima media
JANELA_RMS = 30.0



#abrir ficheiro

'''
#ABERTURA AUTOMATICA DOS FICHEIROS
for i in range(0,101):
    
    if(os.path.isfile('M5_MB_ESQ_ISOM_'+str(i)+'.txt')):
        print(i)
        f = open("M5_MB_ESQ_ISOM_" +str(i) +".txt", "r")
        a=loadtxt('M5_MB_ESQ_ISOM_'+str(i)+'.txt')
        nome='M5_MB_ESQ_ISOM_'+str(i)+'.txt'
    else:
        i=i+1
    #f.close()
   
    
import sys
for filename in sys.argv[1:]:
    with open(filename) as f:
        print filename
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




#guardar os 3 canais importantes em 3 vectores
Emg=a[:,6] #6 ou 14 ver diferenca, qual uso agora?
Posicao=a[:,9]
Torque=a[:,7] # canal 15 e o torque rectificado

#mostrar plots de cada canal
#Electromiografia - canal6
subplot(3,1,1)
plot(Emg)
title('EMG', fontsize=10)
xlabel('Tempo', fontsize=8)
ylabel('Amplitude', fontsize=8)

#Posicao - canal9
subplot(3,1,2)
plot(Posicao)
title('Posicao', fontsize=10)
xlabel('Tempo', fontsize=8)
ylabel('Graus', fontsize=8)

#Torque Corrigido - canal15
subplot(3,1,3)
plot(Torque)
title('Momento de Forca Corrigido para a Gravidade', fontsize=10)
xlabel('Tempo', fontsize=8)
ylabel('Torque', fontsize=8)

figure()




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

filtrado=filtro(Emg,10.0)

#print(sum(filtrado-Emg))

#para ver se houve mudanca nas frequencias com os filtros:
#atenuacao de sinal ate aos 10Hz e ausencia de 50Hz pedidos
subplot(2,1,1)
plotfft(Emg,FA)
title('FFT do Emg original', fontsize=10)
xlabel('Frequencia', fontsize=8)
ylabel('Amplitude', fontsize=8)
subplot(2,1,2)
plotfft(filtrado,FA)
title('FFT do Emg Filtrado', fontsize=10)
xlabel('Frquencia', fontsize=8)
ylabel('Amplitude', fontsize=8)
figure()



#para ver diferencas entre EMG original e filtrado
subplot(2,1,1)
plot(filtrado)
title('EMG Filtrado', fontsize=10)
xlabel('Tempo', fontsize=8)
ylabel('Amplitude', fontsize=8)

subplot(2,1,2)
plot(Emg)
title('EMG Original', fontsize=10)
xlabel('Tempo', fontsize=8)
ylabel('Amplitude', fontsize=8)
show()





results=[]


#Calculo do Valor de Forca Maxima - Fmax
Fmax=max(Torque)
print 'Fmax: ' + str(Fmax)

results += [{'Fmax (N.m)': max(Torque)}]

#Retirar valor de tempo correspondente a Fmax

#Tempo=0
#for e in Torque:
#    if(e==Fmax):
#        break
#    Tempo=Tempo+1
#print 'Tempo respectivo da Forca Maxima (ms): ' + str(Tempo)

Tempo=argmax(Torque)
print 'Tempo: ' + str(Tempo)


#FCalcular intervalo de tempo:

if(Tempo>INTERVALO/2):
    t0=Tempo-INTERVALO/2
else:
    t0=0      
t1=Tempo+INTERVALO/2

    
    

#Calculo do Valor de Forca Media - Fmean (com intervalo do 300 ms)
forca_media=mean(Torque[t0:t1])
print 'Fmed: ' + str(forca_media)




#Calculo do plot e valor rms
#rms=smooth(((filtrado**2)**0.5),JANELA_RMS) # janela de 30 ms
rms=smooth(((filtrado**2)**0.5),INTERVALO) #janela de 300 ms
plot(rms)
title('RMS', fontsize=10)
xlabel('Tempo', fontsize=8)
ylabel('Amplitude', fontsize=8)
show()



#Calculo Root Mean Square (RMS)
#Este e o valor de 100% do EMG
rms_int=float(sqrt(sum(filtrado[t0:t1]**2))/INTERVALO)
rms_int2=mean(rms[t0:t1])
print 'RMS: ' + str(rms_int)
print 'RMS: ' + str(rms_int2) #VALORES DIFERENTES (?)
#print 'Valor de EMG Maxima no intervalo de 300 ms pedidos: ' + str(valor_em_intervalo_300(Emg))




#Calculo da posicao media
posicao_media=mean(Posicao[t0:t1])
print 'Angulo Medio: ' + str(posicao_media)



#Calculo de EMG_100%
emg_100=filtrado[Tempo]
print 'EMG_100%: ' + str(emg_100)

#Calculo do Incremento de Forca e da Forca Total
fi=(Fmax*rms_int)/emg_100
forca_total=double(Fmax+fi)
print 'Forca Total: ' + str(forca_total)

#Colocar valores em doc Excel

def guardar_excel(nome):
    import xlwt
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    
    #primeiro linha depois coluna (comeca em 0)
    sheet.write(0,0,'Descricao') 
    sheet.write(0,1,'Valores') 

    #preencher 1a coluna
    #ciclo for
   ''' 
  a.keys()

>>> a.values()
[23]
>>> a=[]
>>> a+=[{'forca'.23})
  File "<console>", line 1
    a+=[{'forca'.23})
                  ^
SyntaxError: invalid syntax
>>> a+=[{'forca':23})
  File "<console>", line 1

    a+=[{'forca':23})
                    ^
SyntaxError: invalid syntax
>>> a+=[{'forca':23}]
>>> a+=[{'emg':23}]
>>> a
[{'forca': 23}, {'emg': 23}]
'''

    sheet.write(1,0,'Fmax (N.m)') 
    sheet.write(2,0,'Fmed') 
    sheet.write(3,0,'Tempo') 
    sheet.write(4,0,'Angulo Medio') 
    sheet.write(5,0,'RMS') # REVER VALOR
    sheet.write(6,0,'EMG_100%') # REVER VALOR
    sheet.write(7,0,'Forca Total')

    #preencher 2a coluna
    sheet.write(1,1,Fmax)
    sheet.write(2,1,forca_media) 
    sheet.write(3,1,Tempo) 
    sheet.write(4,1,posicao_media) 
    sheet.write(5,1,rms_int) # REVER VALOR
    sheet.write(6,1,emg_100) # REVER VALOR
    sheet.write(7,1,forca_total)    
    
    #salvar em doc excel
    wbk.save(str(nome)+'.xls')


#fazer automatico com for onde nome toma um nome proprio
nome='M5_MB_ESQ_ISOM_30'
guardar_excel(str(nome))


