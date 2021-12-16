#import RPi.GPIO as GPIO
from tkinter import *
#import time
#import threading
from PIL import ImageTk,Image

window = Tk()
window.geometry("750x550")
window.title('Licenta Denis Sebastian 2021-2022')
#window.resizable(0, 0)
tensiune=0

class app_layout:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.schema = ImageTk.PhotoImage(Image.open("D:\Facultate 2020\Licenta\Schema.png"))
        self.labelSchema = Label(image = self.schema)
        self.labelSchema.pack()

        self.myButton = Button(master, text = "Fa click", command = self.clicker)
        self.myButton.pack(pady=20)
    def clicker(self):
        print("Functioneaza")


#def read_voltage(tensiune):
#    voltage = open("voltage.txt", "r")
#    tensiune = voltage.read()
#    voltage.close()
chestie = app_layout(window)

#label_voltage = Label(window, text = "Debit")
#label_voltage.pack(pady=20)

#slider_vana = Scale(window, from_ = 0, to = 100, orient = HORIZONTAL)
#slider_vana.pack(pady=20)

#button_vana = Button(window, text = "Inchidere vana")
#button_vana.pack(pady=20)

#i=0

#while i < 6:
#    read_voltage(tensiune)
#    print(tensiune)
#    i += 1
#    time.sleep(6)



window.mainloop()
