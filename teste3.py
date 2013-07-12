
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:45:30 2013

@author: Luisa
"""

import Image as Image
import Tkinter, Tkconstants, tkFileDialog
import os, sys
from Tkinter import Tk
#from tkinter.messagebox import showinfo

import tkMessageBox
from Tkinter import *
from tkCommonDialog import Dialog
import shutil
import tkFileDialog
import win32com.client
from PIL import ImageTk,Image

import os, sys
import Tkinter as tki
import Image as Image
import ImageTk
import time

from Tkinter import *
from PIL import ImageTk
import os


from Tkinter import *
from tkMessageBox import *


import Tkinter as tki # Tkinter -> tkinter in Python 3
#para sair do programa (cancel)
import sys
#para executar aplicacao
import execute_aplic2 as exec2

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:40:34 2013

@author: Luisa
"""
import os, sys
import Tkinter as tki
import Image, ImageTk
import time

from Tkinter import *
from PIL import ImageTk, Image
import os

import execute_program_apl2 as ex


class GUI(tki.Tk):
    """ initial program"""    
    
    def __init__(self):
        """ funcao de inicio do programa """
        
        #root = Tk()
        
        #img = Image.open("C:\Users\Luisa\Documents\GitHub\Codigo_EMG\cao.jpg")
        '''
        img = ImageTk.PhotoImage(Image.open("C:\\Users\\Luisa\\Documents\\GitHub\\Codigo_EMG\\frontimage.jpg"))
        panel = Label(image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        '''
       
        self.default_directory = '..\\..\\Data_Ap2\\' # a default name
        
        
        # notice that lambda allows us to pass args
        self.go_message = 'Please, make sure your channels are right in the library. '
        button1 = tki.Button(self, activebackground= '#5D8AA8', text ='RUN',
                            command=lambda: 
                                self.go_to_application(self.go_message, 
                                                       self.default_directory))
        button1.pack( side= LEFT)
        
        
        # cancel the application
        self.cancel_message = 'Are you sure you want to close the application?  '
        button2 = tki.Button(self, activebackground= '#5D8AA8', text='Close',
                            command=lambda: 
                                self.cancel(self.cancel_message)) #fg='#E32636'
        button2.pack( side= RIGHT)
        
        self.mainloop()
        
    def cancel(self, message):
        """ ask if the user wants to go out """
        
        top = self.top = tki.Toplevel(self)
        label0 = tki.Label(top, text=message)
        label0.pack()
        
        button2 = tki.Button(top, activebackground= '#5D8AA8', text='Yes', 
                             command=lambda: sys.exit())
        button2.pack()
    def go_to_application(self, message, data):
        """ apply application 2"""
        self.askdirectory()
        top = self.top = tki.Toplevel(self)
        label0 = tki.Label(top, text=message)
        label0.pack()

        button3 = tki.Button(top, activebackground= '#5D8AA8', text='OK', 
                     command=lambda: self.application(data))
        button3.pack()
    
    def application(self, directoria):
        """ execute application"""
        exec2.abrir_ficheiro(directoria)        
            
    def submit_name(self, directoria):
        """ submit directory name"""
        top = self.top = tki.Toplevel(self)
        self.default_directory = directoria
        self.top.destroy()          
        
    def askdirectory(self):
        """ function to ask what directory we want"""
        
        des = tkFileDialog.askdirectory(title = "The Destination folder is ")
            
        if des:
            self.submit_name(des)
            

    

GUI = GUI()
#GUI.mainloop()