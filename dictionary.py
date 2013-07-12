# -*- coding: utf-8 -*-
"""
Created on Tue Jul 09 15:38:53 2013

@author: Luisa
"""

#fazer guião


#todos os ficheiros irão estar todos na mesma directoria (pasta)
# que o user indica inicialmente
#o user ira correr o programa e este percorre todos os ficheiros BF 
#de 1 individuo e cada sem BF, consequentemente para todos os individuos



#APLICACAO 1 E 2 
#CONSTANTES
FA = 1000.0 #sampling frequency
INTERVALO = 50.0 #interval to calculate Fmed
LIMIT = 50.0


#APLICACAO 1
#CONSTANTES
AP1_MOM1 = 5 #para mudar depois para 0
AP1_MOM2 = 5
AP1_POS1 = 30
AP1_POS2 = 40

AP1_NUMERO_COLUNAS = 5 #so queremos 5 valores de cada ficheiro



#APLICACAO 2
#CONSTANTES
AP2_MOM1 = 5 #so existem dois momentos: 0 e 5 - para mudar posteriormente
AP2_MOM2 = 5
AP2_POS1 = 30 #existem posicoes 30, 40, 50, 60, 70, 75, 80, 85, 90 e 100
AP2_POS2 = 100

AP2_NUMERO_COLUNAS = 7 #queremos 7 valores de cada ficheiro




#ESTRUTURA DO DICIONARIO:
#channels=canais - admitindo que para cada sujeito há uma sequencia de canais

def dicionario():
    """ dicionario"""

    conf = {'MB': {'channels': [6, 9, 12]},
    }
    
    return conf



def aplicacao1():
    """ constantes para a aplicacao1"""
    return AP1_MOM1, AP1_MOM2, AP1_POS1, AP1_POS2, AP1_NUMERO_COLUNAS
    
def aplicacao2():
    """ constantes para a aplicacao2"""
    return AP2_MOM1, AP2_MOM2, AP2_POS1, AP2_POS2, AP2_NUMERO_COLUNAS

def calculos():
    """ constantes para as duas aplicacoes"""
    return FA, INTERVALO, LIMIT
    
#create function to return directory to save files:
    #3 folders (1Application, 2Application, Plots)



