from tkinter import *
from tkinter import messagebox

usuario=[]

i=0
def borrar():
    """Funciones para el boton Borrar"""
    entrada_nombre.delete(0,END)
    entrada_apellido.delete(0,END)
    entrada_cedula.delete(0,END)
    entrada_contrasena.delete(0,END)
    i=0


def registrar():
    """Funciones de Boton Registrar"""
    i = messagebox.askquestion("Salir","Registrar Usuario")
    if i=='yes' and opciones.get()==1 or opciones.get()==2:
        usuario.append((entrada_nombre.get(),entrada_apellido.get(),opciones.get(),entrada_cedula.get(),entrada_contrasena.get()))
        #Se hará la conexion con la bd de tacosoft desde la lista usuario.
        print(usuario)    
        entrada_nombre.delete(0,END)
        entrada_apellido.delete(0,END)
        entrada_cedula.delete(0,END)
        entrada_contrasena.delete(0,END)
        i=0
    else:
        root.destroy()


root=Tk()
#Creacion de la ventana de la aplicación
root.title('Tacosoft')
root.iconbitmap('iconoTS.ico')
root.geometry('500x500')
root.resizable(0,0)

#Creacion del encabezado

imagen=PhotoImage(file='Tacos.gif')
label1=Label(root,image=imagen)
label1.place(x=330,y=30)
label1.config(pady=5,padx=5)

label2=Label(root,text="Registro\n Usuarios")
label2.place(x=150,y=60)
label2.config(font=('Century',20,'bold'))

#Creacion del marco/frame
frame1=Frame(root)
frame1.config(width=450,height=325)
frame1.config(bg='light gray')
frame1.config(bd='20')
frame1.place(x=25,y=150)

"""Se crean las entradas en donde se van a insertar los datos en la aplicación"""
entrada_nombre = Entry(frame1,width=40)
entrada_nombre.place(x=120,y=50)
entrada_nombre.config(justify='center',state='normal')

entrada_apellido = Entry(frame1,width=40)
entrada_apellido.place(x=120,y=90)
entrada_apellido.config(justify='center',state='normal')

entrada_cedula = (Entry(frame1,width=40))
entrada_cedula.place(x=120,y=170)
entrada_cedula.config(justify='center',state='normal')

entrada_contrasena = Entry(frame1,width=40)
entrada_contrasena.place(x=120,y=210)
entrada_contrasena.config(show='*',justify='center')

#Creacion de las etiquetas de las entradas: 
label_nombre =Label(frame1, text='Nombre:')
label_nombre.config(bg='light gray',font=('Times New Roman',12))
label_nombre.place(x=40,y=50)

label_apellido =Label(frame1, text='Apellido:')
label_apellido.config(bg='light gray',font=('Times New Roman',12))
label_apellido.place(x=40,y=90)

label_rol =Label(frame1, text='Rol:')
label_rol.config(bg='light gray',font=('Times New Roman',12))
label_rol.place(x=40,y=130)

label_cedula=Label(frame1, text='Cédula:')
label_cedula.config(bg='light gray',font=('Times New Roman',12))
label_cedula.place(x=40, y=170)

label_contrasena =Label(frame1, text='Contraseña:')
label_contrasena.config(bg='light gray',font=('Times New Roman',12))
label_contrasena.place(x=40, y=210)

#Creacion de Botones "Registrar" y "Borrar"
botonRegistar=Button(frame1, text='Registrar',command=registrar)
botonRegistar.place(x=100,y=260)
botonRegistar.config(bd=5, font="Curier 10")

botonBorrar=Button(frame1, text='Borrar',command=lambda:borrar())
botonBorrar.place(x=260,y=260)
botonBorrar.config(bd=5, font="Curier 10")

#Creacion RadioButton para Roles:
opciones = IntVar()
Radiobutton(frame1,text='Administrador', variable=opciones, value=1,bg="light gray").place(x=120, y=130)
Radiobutton(frame1, text='Usuario',variable=opciones, value=2,bg="light gray").place(x=250, y=130)

root.mainloop()