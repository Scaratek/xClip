from threading import Thread
from tkinter import *
import keyboard
import gd


global NoclipEnabled
NoclipEnabled = False

def WaitGD():
    global memory
    memory = None
    
    while True:
        try:
            memory = gd.memory.get_memory()
            break
        except:
            pass

    opengd.config(text="xClip", font=("Trebuchet MS", 14))
    NoclipBtn.pack(side=TOP, pady=10)

def Noclip(): # Hack
    global NoclipEnabled

    if NoclipEnabled:
        memory.disable_noclip()
        NoclipEnabled = False
        NoclipBtn.config(text="Enable Noclip")
    else:
        memory.enable_noclip()
        NoclipEnabled = True
        NoclipBtn.config(text="Disable Noclip")

def toggle_noclip(event=None):
    Noclip()

root = Tk()
root.configure(background="black")

root.title('xClip')
root.geometry('250x150')  # Window

opengd = Label(root, text="Please open Geometry Dash", font=("Trebuchet MS", 17), bg="black", fg="white")
opengd.pack(side=TOP, pady=20)  

NoclipBtn = Button(text="Enable Noclip", command=Noclip, height=1, width=15, bg="black", fg="white", bd=3)
NoclipBtn.pack(side=TOP, pady=10)

NoclipBtn.pack_forget()

Thread(target=WaitGD).start()

keyboard.add_hotkey("m", toggle_noclip) # Hotkey

root.mainloop()
