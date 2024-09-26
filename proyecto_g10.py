import tkinter as tk
import time

ventana = tk.Tk()
barra_menu = tk.Menu(ventana)
## RELOJ 
reloj = tk.Label(ventana, font = ('Arial', 24), bg = 'gray', fg = 'black')
def hora():
    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text = tiempo_actual)
    ventana.after(1000, hora)
reloj.pack(anchor = 'ne')
hora()
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)

barra_menu.add_cascade(label = 'Principal', menu=menu_principal)
submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label = 'Opciones', menu=submenu)
submenu.add_command(label = 'Tareas')
submenu.add_command(label = 'Notas adicionales')

## VENTANA TAREAS
ingreso_tarea = tk.Entry(ventana)
ingreso_tarea.pack()
def agregar_tarea():
    tarea = ingreso_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        
        ingreso_tarea.delete(0, tk.END)

boton_agregar = tk.Button(ventana, text = 'Agregar tarea', command = agregar_tarea)
boton_agregar.pack()
def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)
boton_eliminar = tk.Button(ventana, text = 'Eliminar tarea', command = eliminar_tarea)
boton_eliminar.pack()
lista_tareas = tk.Listbox(ventana)
lista_tareas.pack()


ventana.mainloop()