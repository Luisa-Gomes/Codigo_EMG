# -*- coding: utf-8 -*-
"""file to execute the file process.py"""

from numpy import loadtxt
import process as pro
import os


#AUTOMATIC OPENING FILES
def abrir_ficheiro():
    """function opens all files in directory d"""
    for subject in range(1, 6): #search each subject
        for s_file in range(1, 101): #search each file of each subject
            direct = '..\\..\\Data\\'
            nome = 'M' + str(subject) + '_MB_ESQ_ISOM_' + str(s_file)
            if(os.path.isfile(direct + nome + '.txt')):
                load = loadtxt(direct + nome+ '.txt')
                results = pro.calculo_valores(load)
                pro.guardar_excel(nome, results)
   

abrir_ficheiro()
