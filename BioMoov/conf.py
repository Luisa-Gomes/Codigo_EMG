
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:45:30 2013

@author: Ana Luisa Gomes
"""

#   DOCUMENTO DE REGISTO DE PARAMETROS


#Utilização das configurações:
    
# 1. Todos os ficheiros em formato .txt devem estar na mesma 
#directoria (pasta 'data') - que o user indica inicialmente
# 2. É aconselhado em primeiro lugar a leitura do respectivo guião desenvolvido 


#INPUTS:
    
#    1. O utilizador configura as variáveis neste ficheiro conf.py
#    2. Os parâmetros assinalados devem ter sempre um valor atribuido 
#    3. Executa o ficheiro run.py com apenas double click



#APLICACAO 1 E 2 
#Parametros

#Frequencia de amotragem  
#default: 
#FA = 1000.0
FA = 1000.0 #sampling frequency

#Intervalo de tempo para cálculo de RMS (numero de amostras)
#default:
#INTERVALO = 50.0
INTERVALO = 50.0

#Limit utilizado no critério da escolha do valor máximo de Torque (Nm)
#default:
#LIMIT = 50.0
LIMIT = 50.0

#Frequencias utilizadas para o filtro banda-stop aos 50Hz
#default:
#FREQ1 = 49.5
#FREQ2 = 50.5
FREQ1 = 49.5
FREQ2 = 50.5

#Filtro banda-stop aos 50Hz: se True o filtro está activo, se False inactivo
#default:
#FILTRO50 = True
FILTRO50 = True

#Frequencia utilizada para o filtro passa-alto aos 10Hz
#default:
#FREQ_HIGHPASS = 10.0
FREQ_HIGHPASS = 10.0


#criterio de 10Nm como threshold
#default:
#TRESH = 10.0
TRESH = 10.0



#APLICACAO 1
#Parametros

#Valores de Momento menor e maior, respectivamente, para a aplicacao 1
#default:
#AP1_MOM1 = 0
#AP1_MOM2 = 5
AP1_MOM1 = 0
AP1_MOM2 = 5

#Valores de Posicao menor e maior, respectivamente, para a aplicacao 1
#default:
#AP1_POS1 = 30
#AP1_POS2 = 40
AP1_POS1 = 30
AP1_POS2 = 40




#APLICACAO 2
#Parametros

#Valores de Momento menor e maior, respectivamente, para a aplicacao 2
#default:
#AP2_MOM1 = 0
#AP2_MOM2 = 5
AP2_MOM1 = 0
AP2_MOM2 = 5

#Valores de Posicao menor e maior, respectivamente, para a aplicacao 2
#default:
#AP2_POS1 = 30
#AP2_POS2 = 100
AP2_POS1 = 30
AP2_POS2 = 100


#Valores True/False para guardar ficheiros pdf.
#Estes ficheiros apresentam os sinais a utilizar em plots
#com a representação dos valores de forca maxima.
#Caso se queira a representação destes sinais, altera-se
#o valor das variáveis para True.
#default:
#PLOTS_AP1 = False
#PLOTS_AP2 = False
PLOTS_AP1 = False
PLOTS_AP2 = False


#Sujeitos e canais
#Configuração relativa a cada sujeito
#Atenção: deve-se respeitar esta ordem: [trigger, emg, posicao, torque]
#default:
#canal do sinal trigger = 3
#canal do sinal emg = 6
#canal do sinal da posicao = 9
#canal do sinal do torque = 12


#A contagem de canais no pythonxy começa a partir do 0.
#Entre cada linha, é necessário uma virgula.
SUJEITOS = {
    'MB': {'channels': [3, 6, 9, 15]},

#exemplos
    #'MJ': {'channels': [3, 6, 9, 15]},
    #'LG': {'channels': [3, 6, 9, 15]}

    }
    


