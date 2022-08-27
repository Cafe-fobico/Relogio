import tkinter  as tk 
from tkinter import ttk
import time
from time import strftime


tela = tk.Tk()
tela.title("relogio")

def horario_atual():
    horario = strftime('%H:%M:%S %p \n %A')
    l1.config(text = horario)
    l1.after(1000,horario_atual) # delay de tempo de 1000 millisegundos 
    
tela.geometry("420x200")
my_font =('times',52,'bold')
l1=tk.Label(tela,font=my_font,bg='white')
l1.grid(row=1,column=1,padx=5,pady=25)
l1.pack(anchor = 'center')

horario_atual()
tela.mainloop()