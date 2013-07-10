
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:45:30 2013

@author: Luisa
"""

import Tkinter as tki # Tkinter -> tkinter in Python 3
#para sair do programa (cancel)
import sys
#para executar aplicacao
import execute_aplic2 as exec2


#IMPORTANTE: COMO JÁ ESTAMOS NUMA DETERMINADA DIRECTORIA
#A DIRECTORIA A COLOCAR TERÁ DE SER
#..\\..\\Data_Ap2\\
#tal como utilizada antes
#presente directoria: C:\Users\Luisa\Documents\GitHub\Codigo_EMG


class GUI(tki.Tk):
    """ initial program"""    
    
    def __init__(self):
        """ funcao de inicio do programa """
        tki.Tk.__init__(self)
        self.default_directory = '..\\..\\Data_Ap2\\' # a default name

        button0 = tki.Button(self, text='Directory', command=self.msg_box)
        button0.pack()

        # notice that lambda allows us to pass args
        self.go_message = 'Please, make sure your channels are right in the library. '
        button1 = tki.Button(self, text ='Ok',
                            command=lambda: 
                                self.go_to_application(self.go_message, 
                                                       self.default_directory))
        button1.pack()
        
        # cancel the application
        self.cancel_message = 'Are you sure you want to close the application?  '
        button2 = tki.Button(self, text='Close',
                            command=lambda: 
                                self.cancel(self.cancel_message))
        button2.pack()

    def exit_application(self):
        """ exit """
        sys.exit()
    
    def cancel(self, message):
        """ ask if the user wants to go out """
        top = self.top = tki.Toplevel(self)
        label0 = tki.Label(top, text=message)
        label0.pack()
        
        button2 = tki.Button(top, text='Yes', 
                             command=lambda: self.exit_application())
        button2.pack()

    def go_to_application(self, message, data):
        """ apply application 2"""
        top = self.top = tki.Toplevel(self)
        label0 = tki.Label(top, text=message)
        label0.pack()

        button3 = tki.Button(top, text='OK', 
                             command=lambda: self.application(data))
        button3.pack()

    def msg_box(self, msg='Please, choose your directory to work with. ', extra=True):
        """ choose directory"""
        top = self.top = tki.Toplevel(self)
        label0 = tki.Label(top, text=msg)
        label0.pack()

        if extra:
            self.entry0 = tki.Entry(top)
            self.entry0.pack()

            button2 = tki.Button(top, text='Submit', command=self.submit_name)
            button2.pack()
        

        button3 = tki.Button(top, text='Cancel',
                                command=lambda: self.top.destroy())
        button3.pack()

    def application(self, directoria):
        """ execute application"""
        exec2.abrir_ficheiro(str(directoria))        
        
    def submit_name(self):
        """ submit directory name"""
        data = self.entry0.get()
        if data:
            self.default_directory = data
            self.top.destroy()

GUI = GUI()
GUI.mainloop()