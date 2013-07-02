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
import xlwt
import process as process




#abrir ficheiro em que muda M# e e ISOM_#


#este será um ficheiro execute e outro será o ficheiro process.py e fazemos import process.py, e usamos process.funcao....


#ABERTURA AUTOMATICA DOS FICHEIROS
for a in range(0,101): #ver cada sujeito
    for b in range(0,101): #ver cada ficheiro de cada sujeito
    
        if(os.path.isfile('M'+str(a)+'_MB_ESQ_ISOM_'+str(b)+'.txt')):
            f = open("M"+str(a)+"_MB_ESQ_ISOM_" +str(b) +".txt", "r")
            
            process.
            
            
            a=loadtxt('M'+str(a)+'_MB_ESQ_ISOM_'+str(b)+'.txt')
            nome='M'+str(a)+'_MB_ESQ_ISOM_'+str(b)+'.txt'
    #f.close()
   


''' 
f = open("M5_MB_ESQ_ISOM_30.txt", "r")
a=loadtxt('M5_MB_ESQ_ISOM_30.txt')
f.close()
'''

