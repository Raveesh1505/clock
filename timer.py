import time
import winsound
from tkinter import *

def Time_Seconds():
    t = hour.get() * 3600 + min.get() * 60 + sec.get()
    t = int(t)
    countdown(t)

def countdown(t):
    freq = 100
    dur = 50
    while t > 0:
        print(t)
        t = t-1
        time.sleep(1)
        winsound.Beep(freq,dur)
    winsound.Beep(800,3000)
    print("Time's up")

clock = Tk()
clock.title("CountDown Timer")
clock.geometry("400x250")
time_format=Label(clock, text= "Enter time in hour-min-sec format!", fg="red",bg="black",font="Arial").place(x=90,y=120)
addTime = Label(clock,text = "Hour   Min      Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "Add",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x= 80, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)
submit = Button(clock,text = "Set Timer",fg="red",width = 10,command = Time_Seconds).place(x =110,y=70)
  
clock.mainloop()