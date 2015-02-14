#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Python支持多种图形界面的第三方库，包括：Tk, wxWidgets, Qt, GTK


Tkinter
'''
from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

app = Application()
# 设置窗口标题:
app.master.title('Hello')
# 主消息循环:
app.mainloop()

import tkMessageBox

class Application2(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)


app = Application2()
# 设置窗口标题:
app.master.title('Message')
# 主消息循环:
app.mainloop()
