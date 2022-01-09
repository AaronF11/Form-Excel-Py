from UI import *
from utils import *
from tkinter import *
from tkinter import messagebox

# < --------- MESSAGEBOXS --------- >
def info_about():
    messagebox.showinfo("Acerca de", "VERSIÓN [1.0]")

def warning():
    messagebox.showwarning("Aviso", "Acción no guardada")

def end():
    answer = messagebox.askquestion("CERRAR", "FINALIZAR PROGRAMA")
    if answer == "yes":
        exit(0)
    else:
        pass


