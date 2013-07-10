# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:45:30 2013

@author: Luisa
"""

import Tkinter as tki # Tkinter -> tkinter in Python 3

#para a directoria
import Tkinter, Tkconstants, tkFileDialog
#import chrome
#import filedialog
#para sair do programa (cancel)
import sys
#para executar aplicacao
import execute_aplic2 as exec2
#para dialog box caso se clique em cancel
import tkMessageBox

class GUI(tki.Tk):
    def __init__(self):
        tki.Tk.__init__(self)
        self.username = 'Bob' # a default name

        button0 = tki.Button(self, text='Directory', command=self.msg_box)
        button0.pack()

        # notice that lambda allows us to pass args
        self.go_message='Please, make sure your channels are right in the library. '
        button1 = tki.Button(self, text='Ok',
                            command=lambda: self.go_to_application(self.go_message, self.username))
        button1.pack()
        
        # cancel the application
        self.cancel_message='Are you sure you want to close the application?  '
        button2 = tki.Button(self, text='Close',
                            command=lambda: self.cancel(self.cancel_message, True))
        button2.pack()

    def exit_application(self):
        sys.exit()
    
    def cancel(self, message, extra=True):
        """ go out from that program """
        top = self.top = tki.Toplevel(self)
        label0 = tki.Label(top, text=message)
        label0.pack()
        
        button2 = tki.Button(top, text='Yes', command=lambda: self.exit_application())
        button2.pack()

    def go_to_application(self, message, data):
        top = self.top = tki.Toplevel(self)
        label0 = tki.Label(top, text=message)
        label0.pack()

        button3 = tki.Button(top, text='OK', command=lambda: self.application(data))
        button3.pack()

    def msg_box(self, msg='Please, choose your directory to work with. ', extra=True):
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
        exec2.abrir_ficheiro(directoria)        
        
    def return_data(data):
        return data
        
    def submit_name(self):
        data = self.entry0.get()
        if data:
            self.username = data
            self.top.destroy()
        #self.return_data(data)

gui = GUI()
gui.mainloop()