#difference between tk and ttk. ttk adds styles to the buttons like the font, text 
import tkinter as tk
from tkinter import ttk

#Create an item onject that obtains the value of the selected item.
def on_select(event):

    selected_item = event.widget{}
    print(Selected item:", selected_item")


#hey
    root = tk.Tk()
    root.title("Combobox Example")