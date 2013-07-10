# -*- coding: utf-8 -*-
"""
Created on Tue Jul 09 15:38:53 2013

@author: Luisa
"""

#fazer guião


#todos os ficheiros irão estar todos na mesma directoria (pasta) que o user indica inicialmente
#o user ira correr o programa e este percorre todos os ficheiros BF de 1 individuo e cada sem BF, consequentemente para todos os individuos

#DIRECTORIAS PARA GUARDAR
directory1='Analysis_Ap1\\' #pasta unica para guardar excel de ficheiros BF
directory2='Analysis_Ap2\\' #pasta unica para guardar excel de ficheiros sem BF
directory_plots='Plots_Ap2\\' #pasta unica para plots


#APLICACAO 1 E 2 
#CONSTANTES
FA = 1000.0 #sampling frequency
INTERVALO = 50.0 #interval to calculate Fmed
LIMIT = 50.0


#APLICACAO 1
#CONSTANTES
AP1_MOMENTO1 = 5 #para mudar depois para 0
AP1_MOMENTO2 = 5
AP1_POSICAO1 = 30
AP1_POSICAO2 = 40

AP1_NUMERO_COLUNAS = 5 #so queremos 5 valores de cada ficheiro



#APLICACAO 2
#CONSTANTES
AP2_MOMENTO1 = 5 #so existem dois momentos: 0 e 5 - para mudar posteriormente
AP2_MOMENTO2 = 5
AP2_POSICAO1 = 30 #existem posicoes 30, 40, 50, 60, 70, 75, 80, 85, 90 e 100
AP2_POSICAO2 = 100

AP2_NUMERO_COLUNAS = 7 #queremos 7 valores de cada ficheiro




#ESTRUTURA DO DICIONARIO:
#channels=canais - admitindo que para cada sujeito há uma sequencia de canais
#directory1=directoria onde guardar excel da aplicacao 1
#directory2=directoria onde guardar excel da aplicacao 2

def dicionario():

    conf = {'MB': {'channels': [6, 9, 12], 'directory1': directory1, 'directory2': directory2,' directoria_plots': directory_plots},
    }
    
    return conf



def aplicacao1():
    return AP1_MOMENTO1, AP1_MOMENTO2, AP1_POSICAO1, AP1_POSICAO2, AP1_NUMERO_COLUNAS
    
def aplicacao2():
    return AP2_MOMENTO1, AP2_MOMENTO2, AP2_POSICAO1, AP2_POSICAO2, AP2_NUMERO_COLUNAS

def calculos():
    return FA, INTERVALO, LIMIT

