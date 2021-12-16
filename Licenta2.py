#import RPi.GPIO as GPIO
import tkinter as tk
#import time
#import threading
from PIL import ImageTk,Image


#window.geometry("750x550")
#window.title('App licenta')
#window.resizable(0, 0)

class app_layout:
    def __init__(self, master):
        self.master = master
        self.window = tk.Tk()
        self.window.geometry("750x550")
        self.window.title("App licenta")
        #myFrame = Frame(master)
        #myFrame.grid()

        self.schema = ImageTk.PhotoImage(Image.open("D:\Facultate 2020\Licenta\Schema.png"))
        self.labelSchema = tk.Label(image=self.schema)
        self.labelSchema.grid(row=0, column = 0)

        self.myButton = tk.Button(master, text = "Fa click", command = self.clicker)
        self.myButton.grid(row=0, column = 1)

    def clicker(self):
        print("Functioneaza")

if __name__ == "__main__" :
    window = tk.Tk()
    #window.withdraw()
    app = app_layout(window)
    window.mainloop()





