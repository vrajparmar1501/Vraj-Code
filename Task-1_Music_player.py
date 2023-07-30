# importing necessary library
import pygame
from pygame import mixer
from tkinter import *
import os

# for playing
def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

# for pausing
def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

# for resuming
def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()   

# for stopping
def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop() 

root=Tk()
root.title('Music player project')

# for choosing
mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

# playlist

playlist=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('Calibri',15),width=40)
playlist.grid(columnspan=5)

# directory in which songs are there
os.chdir(r'C:\Users\hp\Downloads\Music Album')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

# play button
playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('arial',20),bg="grey",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

# pause button
pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('arial',20),bg="grey",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

# resume button
Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('arial',20),bg="grey",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=2)

# stop button
stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('arial',20),bg="grey",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=3)

mainloop()