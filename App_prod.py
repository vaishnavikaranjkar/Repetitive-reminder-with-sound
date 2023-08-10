from tkinter import *
import winsound
from time import strftime
import time
import threading

def clock():
    string = time.strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, clock)

def ThreadStart():
    t1=threading.Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        min=15*60
        time.sleep(min)
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

window = Tk()
window.title("Timer")
window.geometry("400x300")

Label(window, text="Alarm Clock", font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(window, text="Drink water every 15 minutes", font=("Helvetica 15 bold")).pack()

lbl=Label(window, font=("Helvetica 15 bold"))
lbl.pack(pady=10)

frame=Frame(window)
frame.pack()

Button(window,text="Start Alarm",font=("Helvetica 15"),command=ThreadStart).pack(pady=20)

clock()
window.mainloop()