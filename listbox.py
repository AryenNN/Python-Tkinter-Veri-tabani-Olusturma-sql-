from tkinter import *
 
from tkinter import messagebox
 
pencere = Tk()
 
pencere.title("AryenN")
pencere.geometry("500x400")
 
#grid form çizdirme
uygulama = Frame(pencere)
uygulama.grid()
 
 
Lb1 = Listbox(uygulama)
Lb1.insert(1, "Felix Roleplay")
Lb1.insert(2, "Felix Network")
Lb1.insert(3, "Felix Developer : AryenN , GlestG")
Lb1.insert(4, "AryenN")
Lb1.grid(padx=110, pady=10)
 

pencere.mainloop()
