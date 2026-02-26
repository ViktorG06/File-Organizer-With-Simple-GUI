from tkinter import *
import file_sorter

# Main window
root = Tk()
root.title("Viktor's file sorter")
root.geometry("300x200")

# User instructions
lbl = Label(root, text="Please input which folder you want to sort.\n (PLEASE IMPORT FULL DIRECTORY)")
lbl.grid(column=0, row=0, padx=10, pady=5)

# Entry box
dir_box = Entry(root, width=30)
dir_box.grid(column=0, row=1, padx=10, pady=5)

# Button logic
def clicked(): 
    folder_path = dir_box.get()
    moved = file_sorter.sort_files(folder_path)
    btn_lbl.configure(text=f"File(s) sorted: {moved}")

# Button
btn = Button(root, text="Sort", command=clicked)
btn.grid(column=0, row=2, padx=10, pady=5)

# Tells the user how many items have been sorted
btn_lbl = Label(root, text="")
btn_lbl.grid(column=0, row=3, padx=10, pady=5)

root.mainloop()
