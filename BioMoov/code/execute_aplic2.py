# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:45:30 2013

@author: Ana Luisa Gomes
"""

from numpy import loadtxt
import code.process_aplic2 as pro2
import os
import xlwt
import conf as conf
import code.execute_aplic1 as exec1
import code.plot_analysis_aplic1 as plots1
import code.plot_analysis_aplic2 as plots2

MOMENTO1 = conf.AP2_MOM1
MOMENTO2 = conf.AP2_MOM2
POSICAO1 = conf.AP2_POS1
POSICAO2 = conf.AP2_POS2
NUMERO_COLUNAS = 8


#AUTOMATIC OPENING FILES
def abrir_ficheiro(direct_open):
    """function opens all files in directory d"""
 
    #calls application 1:
    exec1.abrir_ficheiro(direct_open) #Time : 1s
    
    #if PLOTS_AP1 and PLOTS_AP2 True, calls plots applications:
    if (conf.PLOTS_AP1):
        plots1.abrir_ficheiro(direct_open) #Time : 11.63 s
    if (conf.PLOTS_AP2):
        plots2.abrir_ficheiro(direct_open) #Time : 4.9 min
      
    instrucao = conf.SUJEITOS
   
    
    results = []
    
    numero_de_ficheiros = 0
    for moment in range(MOMENTO1, MOMENTO2 + 1): #search each moment
        for sujeito in range(0, len(instrucao)): #search each subject
            iniciais = instrucao.keys()[sujeito]
            c_trigger = instrucao.get(iniciais).values()[0][0]
            c_emg = instrucao.get(iniciais).values()[0][1]
            c_pos = instrucao.get(iniciais).values()[0][2]
            c_tor = instrucao.get(iniciais).values()[0][3]
            directoria = direct_open+"\\Files_Application"
            if not(os.path.exists(directoria)):
                os.mkdir( directoria)
            #directory to save our work aplication 2
            for s_file in range(POSICAO1, POSICAO2 + 1): 
                #search each file of each subject
                nome = 'M' + str(moment) + '_'
                nome = nome + iniciais + '_ESQ_ISOM_' + str(s_file)
                if(os.path.isfile(direct_open + '\\' + nome + '.txt')):
                    results += [{'Nome': str(nome)}]
                    load = loadtxt( direct_open + '\\' + nome + '.txt')
                    numero_de_ficheiros = numero_de_ficheiros + 1
                    results += pro2.calculo_valores(direct_open, iniciais, load, c_trigger, c_emg, c_pos, c_tor)
            directoria = directoria 
    nome = 'Aplicacao2'  
    guardar_excel(nome, results, directoria, numero_de_ficheiros)
    
    

#save in excell
def guardar_excel(nome, results, directoria, numero_de_ficheiros):
    """save all values in a excel document"""
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    
    
    sheet.write(0, 0, 'Nome') 
    sheet.write(0, 1, 'Forca Maxima') 
    sheet.write(0, 2, 'Intervalo de Tempo entre F=10Nm e Fmax')
    sheet.write(0, 3, 'Sample US')
    sheet.write(0, 4, 'Forca Media')
    sheet.write(0, 5, 'Posicao') 
    sheet.write(0, 6, 'RMS') 
    sheet.write(0, 7, 'Contribuicao') 
    sheet.write(0, 8, 'Forca Total') 
     
    i = 0
    for line in range( 1, numero_de_ficheiros + 1):
        for column in range(0, NUMERO_COLUNAS + 1):
            sheet.write(line, column, str(results[i].values()[0]))
            i = i + 1
        
    wbk.save(directoria + '\\' + str(nome) +'.xls')
