#Insert class library. Difference between tk and ttk. ttk adds styles to the buttons like the font, text 
import tkinter as tk
from tkinter import ttk

#Create an item onject that obtains the value of the selected item.
def on_select(event):

    selected_item = event.widget.get()
    print("Selected item", selected_item)


#create a root window and widget object
root = tk.Tk()
root.title("Combobox Example")

#create an array of items
items = ["Item1", "Item 2", "Item 3", "Item 4", "Item5"]

#Combo box operator and call array of items
combo_box = ttk.Combobox(root, values=items)
combo_box.bind("<<ComboboxSelected>>", on_select)

combo_box.pack()

#Create a loop to keep window open
root.mainloop()