
# -*- coding: utf-8 -*-

"""
Created on Wed Jul 10 09:45:30 2013

@author: Ana Luisa Gomes
"""

#    DOCUMENTO DE REGISTO DE PARAMETROS 




#APLICACAO 1 E 2 
#Parametros

#Frequencia de amotragem  
FA = 1000.0

#Intervalo de tempo para cálculo de RMS (numero de amostras)
INTERVALO = 50.0

#Limit utilizado no critério da escolha do valor máximo de Torque (Nm)
LIMIT = 50.0

#Frequencias utilizadas para o filtro banda-stop aos 50Hz
FREQ1 = 49.5
FREQ2 = 50.5

#Filtro banda-stop aos 50Hz: se True o filtro está activo, se False inactivo
FILTRO50 = True

#Frequencia utilizada para o filtro passa-alto aos 10Hz
FREQ_HIGHPASS = 10.0


#criterio de 10Nm como threshold
TRESH = 10.0



#APLICACAO 1
#Parametros

#Valores de Momento menor e maior, respectivamente, para a aplicacao 1
AP1_MOM1 = 0
AP1_MOM2 = 5

#Valores de Posicao menor e maior, respectivamente, para a aplicacao 1
AP1_POS1 = 30
AP1_POS2 = 40




#APLICACAO 2
#Parametros

#Valores de Momento menor e maior, respectivamente, para a aplicacao 2
AP2_MOM1 = 0
AP2_MOM2 = 5

#Valores de Posicao menor e maior, respectivamente, para a aplicacao 2
AP2_POS1 = 30
AP2_POS2 = 100


#Valores True/False para guardar plots em pdf.
PLOTS_AP1 = False
PLOTS_AP2 = False


#Sujeitos e canais
#Configuração relativa a cada sujeito
#Atenção: deve-se respeitar esta ordem: [trigger, emg, posicao, torque]
#default:
#canal do sinal trigger = 3 
#canal do sinal emg = 6
#canal do sinal da posicao = 9
#canal do sinal do torque = 15


SUJEITOS = {
    'MB': {'channels': [3, 6, 9, 15]},

    }
    


