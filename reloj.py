import tkinter as tk
import time 
ventana = tk.Tk()
ventana.title('Reloj simple')
ventana.geometry('400x200')
## Reloj
reloj = tk.Label(ventana, font = ('Calibri', 12), bg = 'white', fg = 'green')
def hora():
    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text = tiempo_actual)
    ventana.after(1000, hora)
reloj.pack(anchor = 'ne')
hora()

## Barra
marco = tk.Frame(ventana)
marco.pack(padx = 10, pady = 10)
scrollbar = tk.Scrollbar (marco)
scrollbar .pack(side = tk.RIGHT, fill = tk.Y)
lista = tk.Listbox(marco, yscrollcommand = scrollbar .set)

for i in range(100):
    lista.insert(tk.END, f'Tareas{i+1}')

lista.pack(side = tk.LEFT, fill = tk.BOTH)
scrollbar .config(command = lista.yview)

ventana.mainloop()