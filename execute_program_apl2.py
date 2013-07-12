
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:45:30 2013

@author: Luisa
"""

import tkFileDialog
import Tkinter as tki
import execute_aplic2 as exec2
import Image, ImageTk
import sys




class GUI(tki.Tk):
    """ initial program"""    
  
    
    def __init__(self):
        """ funcao de inicio do programa """
        
        tki.Tk.__init__(self)
        
        im = "C:\\Users\\Luisa\\Documents\\GitHub\\Codigo_EMG\\frontimage.jpg"
        img = ImageTk.PhotoImage(Image.open(im))
        panel = tki.Label(self, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        
        
        #tki.Tk.__init__(self)
        self.default_directory = '..\\..\\Data_Ap2\\' # a default name
        
        # notice that lambda allows us to pass args
        self.go_message = 'Please, make sure all channels are right. '
        button1 = tki.Button(self, activebackground = '#5D8AA8', text ='RUN', 
                             heigh = 2, width = 38,command = lambda: 
                                self.go_to_application(self.go_message, 
                                                       self.default_directory))
        button1.pack(side = tki.LEFT)
        
        
        # cancel the application
        self.cancel_message = 'Are you sure you want to close the application?'
        button2 = tki.Button(self, activebackground= '#5D8AA8', text = 'Close', 
                             heigh = 2, width = 38, command = lambda: 
                                self.cancel(self.cancel_message)) #fg='#E32636'
        button2.pack(side = tki.RIGHT)
        
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