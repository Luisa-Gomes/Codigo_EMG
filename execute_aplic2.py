# -*- coding: utf-8 -*-
"""
Created on Mon Jul 08 12:37:38 2013

@author: Luisa
"""

from numpy import loadtxt
import process_aplic2 as pro2
import os
import xlwt
import dictionary as dic
import execute_aplic1 as exec1
import plot_analysis_aplic1 as plots1
import plot_analysis_aplic2 as plots2
#from novainstrumentation import tictac as t

MOMENTO1, MOMENTO2, POSICAO1, POSICAO2, NUMERO_COLUNAS = dic.aplicacao2()


#AUTOMATIC OPENING FILES
def abrir_ficheiro(direct_open):
    """function opens all files in directory d"""
    #print direct_open
    #direct_open=u'C:/Users/Luisa/Documents/Data_Ap2'
    #direct_open='..\\..\\Data_Ap2\\'
    #faz aplicacao 1 automaticamente:
    
    #exec1.abrir_ficheiro(direct_open) #1s e tal
    
    
    #plots1.abrir_ficheiro(direct_open) #11.63 s
    
    #t.tic()
    #plots2.abrir_ficheiro(direct_open) #4.9 min
    #t.tac()    
    
    instrucao = dic.dicionario()
   
    
    results = []
    
    numero_de_ficheiros = 0
    for moment in range(MOMENTO1, MOMENTO2 + 1): #search each moment
        for sujeito in range(0, len(instrucao)): #search each subject
            iniciais = instrucao.keys()[sujeito]
            c_emg = instrucao.get(iniciais).values()[0][0]
            c_pos = instrucao.get(iniciais).values()[0][1]
            c_tor = instrucao.get(iniciais).values()[0][2]
            directoria = direct_open+"\\Files_Application2"
            if not(os.path.exists(directoria)):
                os.mkdir( directoria)
            #directory to save our work aplication 2
            for s_file in range(POSICAO1, POSICAO2 + 1): 
                #search each file of each subject
                nome = '/M' + str(moment) + '_'
                nome = nome + iniciais + '_ESQ_ISOM_' + str(s_file)
                if(os.path.isfile(direct_open + nome + '.txt')):
                    results += [{'Nome': str(nome)}]
                    load = loadtxt( direct_open + nome + '.txt')
                    numero_de_ficheiros = numero_de_ficheiros + 1
                    results += pro2.calculo_valores(load, c_emg, c_pos, c_tor)
            nome = '/M' + str(moment) + '_'+ iniciais +'_ESQ_ISOM'  
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
    sheet.write(0, 6, 'Contribuicao') 
    sheet.write(0, 7, 'Forca Total') 
     
    i = 0
    for line in range( 1, numero_de_ficheiros + 1):
        for column in range(0, NUMERO_COLUNAS + 1):
            sheet.write(line, column, str(results[i].values()[0]))
            i = i + 1
        
    wbk.save(directoria + str(nome) +'.xls')
