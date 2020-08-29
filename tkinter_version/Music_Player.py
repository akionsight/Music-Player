import pygame
import tkinter as tkr 
from get_file import get_file
import PySimpleGUI
import os
from pathlib import Path
from tkinter import PhotoImage
file = get_file()
if file != '':

    player = tkr.Tk()
    player.title('Music player')
    player.geometry("205x350")
    player.iconbitmap("logo.ico")
    def Play():
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

    def Reset():
        pygame.mixer.music.stop()
        pygame.mixer.music.play()

    def Pause():
        pygame.mixer.music.pause()

    def Unpause():
        pygame.mixer.music.unpause()
    def ExitWindow():
        exit()
    button1 = tkr.Button(player,width=5,height=3,text='Play', command=Play)
    button1.pack(fill='x')

    button2 = tkr.Button(player,width=5,height=3,text='Reset',command=Reset)
    button2.pack(fill='x')

    button3 = tkr.Button(player,width=5,height=3,text='Pause',command=Pause)
    button3.pack(fill='x')

    button4 = tkr.Button(player,width=5,height=3,text='Unpause',command=Unpause)
    button4.pack(fill='x')

    button5 = tkr.Button(player,width=5,height=3,text='Exit Player',command=ExitWindow)
    button5.pack(fill='x')


    label1 = tkr.LabelFrame(player,text='SongName')
    label1.pack(fill='both', expand='yes')
    contents1 = tkr.Label(label1,text=Path(file).name)
    contents1.pack()
    player.mainloop()
else:
    PySimpleGUI.popup('Sorry, No file given')
    exit()
    