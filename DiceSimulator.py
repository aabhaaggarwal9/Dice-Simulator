import random #import random module
from tkinter import * #import everything from tkinter module
root =Tk() #instantiation
root.geometry("800x400") #creating canvas
l1=Label(root,text="",font=("times",300)) #creating label
def dice():
    options=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685'] #Dice options
    l1.config(text=f'{random.choice(options)}{random.choice(options)}') #displays two dices and randomly showing different values
    l1.pack() #packs the widgets on the geometry
b1=Button(root,text="Roll the dice",command=dice) #button to roll the dice
b1.place(x=350,y=0) #placing the button
root.mainloop() # To iterate over dice