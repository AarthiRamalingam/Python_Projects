from tkinter import Label,Tk
#themed widgets
from tkinter.ttk import *
#to retrive systems' time
from time import strftime
#creating main window object
tk=Tk()
#specifying title name for the window
tk.title("DIGITAL CLOCK")
tk.geometry("560x120")

def time(): 
    string = strftime('%H:%M:%S') 
    lbl.config(text = string) 
    lbl.after(100, time) 
    
#styling the label widget
lbl = Label(tk, font = ('boulder', 40, 'bold'), background = 'black', foreground = 'white') 
#it organizes it in blocks before placing it in parent widget
lbl.pack(anchor = 'center') 
time() 
tk.mainloop()
