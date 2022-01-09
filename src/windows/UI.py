from functions import *
from utils import *
from tkinter import * 
import pandas


# < --------- GLOBAL WIDGETS --------- >

root = Tk()
menu = Menu(root)
frame = Frame(root,
            bg='#1D6F42')
root_two = False
add_id = Entry(frame,  width=20, font = ('Bell T',12))
add_name = Entry(frame,  width=20, font = ('Bell T',12))
add_last_name = Entry(frame, width=20, font = ('Bell T',12))
add_age = Entry(frame,  width=20, font = ('Bell T',12))
add_mail = Entry(frame,  width=20, font = ('Bell T',12))
add_phone = Entry(frame, width=20, font = ('Bell T',12))


def main():

    # < --------- MAIN --------- >
    root.iconbitmap('src\img\excel.ico')
    root.config(background = 'green2')
    root.title('FORMULARIO')
    #root.geometry('560x390')
    root.resizable(0,0)
    frame.grid(column=0,
            row=0,
            sticky='nsew')

    main = Menu(menu, tearoff = 0)
    main.add_command(label = 'GUARADAR REGISTRO', command = seconds)
    menu.add_cascade(label = 'ARCHIVO', menu = main)
    close = Menu(menu, tearoff = 0)
    close.add_command(label = 'FINALIZAR REGISTRO', command = end)
    menu.add_cascade(label = 'CERRAR', menu = close)
    about = Menu(menu, tearoff = 0)
    about.add_command(label = 'VESIÓN', command = info_about)
    menu.add_cascade(label = 'ACERCA DE', menu = about)
    root.config(menu = menu)


    # < --------- LABELS --------- >
    id = Label(frame, text ='ID', width=10)
    id.grid(column=0, row=0, pady=5, padx= 5)

    name = Label(frame, text ='NOMBRE', width=10)
    name.grid(column=1, row=0, pady=5, padx= 5)

    last_name = Label(frame, text ='APELLIDO', width=10)
    last_name.grid(column=0, row=2, pady=5, padx= 5)

    age = Label(frame, text ='EDAD', width=10)
    age.grid(column=1, row=2, pady=5, padx= 5)

    mail = Label(frame, text ='CORREO', width=10)
    mail.grid(column=0, row=4, pady=5, padx= 5)

    phone = Label(frame, text ='TELEFONO', width=10)
    phone.grid(column=1, row=4, pady=5, padx= 5)


    # < --------- ENTRYS --------- >
    add_id.grid(column=0, row=1)
    add_name.grid(column=1, row=1)
    add_last_name.grid(column=0, row=3)
    add_age.grid(column=1, row=3)
    add_mail.grid(column=0, row=5)
    add_phone.grid(column=1, row=5)

    # < --------- BUTTON --------- >
    add_button = Button(frame, width=20, font = ('Bell T',12, 'bold'), text='Agregar', bg='orange',bd=5, command=add)
    add_button.grid(columnspan=2, row=6, pady=20, padx= 10)

    mainloop()

# < --------- SECOND --------- >
def seconds():
    
    def data():
        global id, name, last_name, age, mail, phone
        records = {'ID':id, 'NOMBRE':name, 'APELLIDOS':last_name, 'EDAD':age, 'CORREO INSTITUCIONAL':mail, 'TELEFONO':phone}
        excel = str(file_name.get() + '.xlsx')
        dataFrame = pandas.DataFrame(records, columns = ['ID', 'NOMBRE', 'APELLIDOS', 'EDAD', 'CORREO INSTITUCIONAL', 'TELEFONO'])
        dataFrame.to_excel(excel)
        file_name.delete(0,END)

    root_two = Toplevel()
    root_two.iconbitmap('src\img\excel.ico')
    root_two.config(background = 'green2')
    root_two.title('FORMULARIO')
    # < --------- Toplevel --------- >
    file = Label(root_two, text ='NOMBRA EL REGISTRO', width=25, bg='gray16',font = ('Bell T',12, 'bold'), fg='white')
    file.grid(column=0, row=0, pady=10, padx= 10)

    file_name = Entry(root_two, width=23, font = ('Bell T',12),highlightbackground = "green", highlightthickness=4)
    file_name.grid(column=0, row=1, pady=1, padx= 10)

    save = Button(root_two, width=20, font = ('Arial',12, 'bold'), text='GUARDAR', bg='green2',bd=5, command = data)
    save.grid(column=0, row=2, pady=20, padx= 10)
       

# < --------- FUNCTIONS --------- >
def add():
    global id, name, last_name, age, mail, phone

    id.append(add_id.get())
    name.append(add_name.get())
    last_name.append(add_last_name.get())
    age.append(add_age.get())
    mail.append(add_mail.get())
    phone.append(add_phone.get())

    add_id.delete(0,END)
    add_name.delete(0,END)
    add_last_name.delete(0,END)
    add_age.delete(0,END)
    add_mail.delete(0,END)
    add_phone.delete(0,END)


def func():
     pass