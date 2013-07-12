# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:27:43 2013

@author: Luisa
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we use tkColorChooser
dialog to change the background of a frame.

author: Jan Bodnar
last modified: January 2011
website: www.zetcode.com
"""
from Tkinter import *
import execute_program_apl2 as ex
import Tkinter as tki

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.parent = master
        self.initUI()

    def initUI(self):
        self.outputBox = Text(self.parent, bg='yellow', height= 10, fg='green', relief=SUNKEN, yscrollcommand='TRUE')
        self.outputBox.pack(fill='both', expand=True)
        self.button1 = Button(self.parent, text='button1', width=20, bg ='blue', fg='green', activebackground='black', activeforeground='green')
        self.button1.pack(side=RIGHT, padx=5, pady=5)
        self.button2 = Button(self.parent, text='button2', width=25, bg='white', fg='green', activebackground='black', activeforeground='green', command=lambda: ex.GUI().cancel('hey you!'))
        self.button2.pack(side=LEFT, padx=5, pady=5)

def main():
    root = Tk()
    app = Application(root)
    app.parent.geometry('300x200+100+100')
    app.parent.configure(background = 'red')
    app.mainloop()

main()