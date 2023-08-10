from tkinter import *
import winsound
import time
import threading

def ThreadStart():
    t1=threading.Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        min=15*60
        time.sleep(min)
        print("Time to Drink Water")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
window = Tk()
window.geometry("400x250")

Label(window, text="Alarm Clock", font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(window, text="Drink water every 15 minutes", font=("Helvetica 15 bold")).pack()

frame=Frame(window)
frame.pack()

Button(window,text="Start Alarm",font=("Helvetica 15"),command=ThreadStart).pack(pady=20)

window.mainloop()
