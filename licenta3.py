#import RPi.GPIO as GPIO
import tkinter as tk
import random as random
#import time
#import threading
from PIL import ImageTk,Image

window = tk.Tk()
window.geometry("750x550")
window.title("Likentzz 2022")


def clicker():
    print("Functioneaza")


schema_rezervor = ImageTk.PhotoImage(Image.open("D:\Facultate 2020\Licenta\Schema.png"))
schema_vana = ImageTk.PhotoImage(Image.open("D:\Facultate 2020\Licenta\Vana.png"))
schema_debit = ImageTk.PhotoImage(Image.open("D:\Facultate 2020\Licenta\debit.png"))

#bloc-cod pt rezervor
labelRezervor = tk.Label(image=schema_rezervor)
labelRezervor.grid(row=0, column = 0)

myButton = tk.Button(window, text = "Fa click", command = clicker)
myButton.grid(row=0, column = 1)

#bloc cod pt vana
labelVana = tk.Label(image=schema_vana)
labelVana.grid(row=0, column = 2)

sliderVana = tk.Scale(window, label = "Pozitie Vana", orient = tk.HORIZONTAL, from_= 0, to = 100)
sliderVana.grid(row=1, column=2)

#bloc cod pt debitmetru
labelDebit = tk.Label(image=schema_debit)
labelDebit.grid(row=0, column = 3)

labelVal_Debit = tk.Label(text = " x m^3/s")
labelVal_Debit.grid(row=1, column = 3)


window.mainloop()