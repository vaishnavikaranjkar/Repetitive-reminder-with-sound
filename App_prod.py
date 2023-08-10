from tkinter import *
import winsound
from time import strftime
import time
import threading

def countdown():
    temp = 15*60
    while temp >-1:
        second.set("{0:2d} seconds remaining".format(temp))
        window.update()
        time.sleep(1)
        if (temp == 0):
            second.set("00 seconds")
        temp -= 1
    countdown()

def ThreadStart():
    t1=threading.Thread(target=alarm)
    t1.start()
    t2=threading.Thread(target=countdown)
    t2.start()

def alarm():
    min=15*60
    count=0
    while True:
        time.sleep(min)
        count=count+1
        print(count,". Time to Drink Water")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
window = Tk()
window.title("Timer")
window.geometry("400x250")

Label(window, text="Timer Clock", font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(window, text="Drink water every 15 minutes", font=("Helvetica 15 bold")).pack()

second=StringVar()
second.set("00")
secondEntry= Label(window, font=("Helvetica",18,""), textvariable=second).pack(pady=10)

frame=Frame(window)
frame.pack()

Button(window,text="Start Alarm",font=("Helvetica 15"),command=ThreadStart).pack(pady=20)

window.mainloop()