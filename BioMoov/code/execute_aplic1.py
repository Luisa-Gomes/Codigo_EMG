# -*- coding: utf-8 -*-

"""
Created on Wed Jul 10 09:45:30 2013

@author: Ana Luisa Gomes
"""
# file to execute the file process.py

from numpy import loadtxt
import code.process_aplic1 as pro
import os
import xlwt
import conf  as conf



#ONLY FOR FILES _BF
MOMENTO1 = conf.AP1_MOM1
MOMENTO2 = conf.AP1_MOM2
POSICAO1 = conf.AP1_POS1
POSICAO2 = conf.AP1_POS2
NUMERO_COLUNAS = 5


#AUTOMATIC OPENING FILES
def abrir_ficheiro(direct):
    """function opens all files in directory d"""
    
    instrucao = conf.SUJEITOS   
    
    results = []
    
    numero_de_ficheiros = 0
    for moment in range(MOMENTO1, MOMENTO2 + 1): #search each moment
        for sujeito in range(0, len(instrucao)): #search each subject
            iniciais = instrucao.keys()[sujeito]
            c_emg = instrucao.get(iniciais).values()[0][1]
            c_pos = instrucao.get(iniciais).values()[0][2]
            c_tor = instrucao.get(iniciais).values()[0][3]
            directoria = direct +"\\Files_Application"
            if not(os.path.exists(directoria)):
                os.mkdir( directoria)
            #directory to save our work aplication 1
            
            for s_file in range(POSICAO1, POSICAO2 + 1):
                #search each file of each subject
                nome = 'M' + str(moment) + '_'
                nome =  nome + iniciais +'_ESQ_ISOM_' + str(s_file) + '_BF'
                if(os.path.isfile(direct + '\\' + nome + '.txt')):
                    results += [{'Nome': str(nome)}]
                    load = loadtxt(direct + '\\'  + nome + '.txt')
                    numero_de_ficheiros = numero_de_ficheiros+1
                    results += pro.calculo_valores(load, c_emg, c_pos, c_tor)
    nome = 'Aplicacao1'
    #nome a guardar so para 1 excell   
    guardar_excel(nome, results, directoria, numero_de_ficheiros)


#guardar em apenas 1 doc EXCELL 
def guardar_excel(nome, results, directoria, numero_de_ficheiros):
    """save all values in a excel document"""
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    
    
    sheet.write(0, 0, 'Nome') 
    sheet.write(0, 1, 'Forca Maxima') 
    sheet.write(0, 2, 'Intervalo de Tempo entre F=10Nm e Fmax') 
    sheet.write(0, 3, 'Forca Media')
    sheet.write(0, 4, 'Posicao') 
    sheet.write(0, 5, 'RMS') 
    
     
    i = 0 
    for line in range( 1, numero_de_ficheiros + 1):
        for column in range(0, NUMERO_COLUNAS + 1):
            sheet.write(line, column, str(results[i].values()[0]))
            i = i + 1
        
    wbk.save(directoria + '\\' + str(nome) +'.xls')



def valores_aplicacao2(direct, iniciais, c_emg, c_pos, c_tor):
    '''important function to save values for application2'''
    
    results = []
    for subject in range(MOMENTO1, MOMENTO2 + 1): #search each moment
    #for each subject (how to do it?)
        for s_file in range(POSICAO1, POSICAO2 + 1):
            #search each file of each subject
            nome = '/M' + str(subject)
            nome = nome + '_'+ iniciais +'_ESQ_ISOM_' + str(s_file) + '_BF'
            if(os.path.isfile(direct + nome + '.txt')):
                results += [{'Nome': str(nome)}]
               
                load = loadtxt(direct + nome + '.txt')
                results += pro.calculo_valores(load, c_emg, c_pos, c_tor)
               
    aplicacao2 = []   
    if (results[1].values()[0]>=results[7].values()[0]):
        aplicacao2 += [results[1].values()[0]]
        aplicacao2 += [results[5].values()[0]]
    else:
        aplicacao2 += [results[7].values()[0]]
        aplicacao2 += results[11].values()[0]
    
    return aplicacao2
    
