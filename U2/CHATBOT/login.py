import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import subprocess

conn = sqlite3.connect('usuarios.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
             username TEXT PRIMARY KEY,
             password TEXT,
             email TEXT)''')

def iniciar_sesion():
    username = username_login_var.get()
    password = password_login_var.get()

    if not username or not password:
        messagebox.showerror("Error", "Por favor, ingresa un nombre de usuario y contraseña.")
        return

    c.execute("SELECT * FROM usuarios WHERE username=? AND password=?", (username, password))
    if c.fetchone() is not None:
        messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
        conn.close()  
        root.destroy()  
        subprocess.run(["python", "chat.py"]) 
    else:
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos.")


def abrir_registro():
    root.withdraw()

    registro_window = tk.Toplevel()
    registro_window.title("Registro")

    username_registro_var = tk.StringVar()
    password_registro_var = tk.StringVar()

    def agregar_usuario():
        username = username_registro_var.get()
        password = password_registro_var.get()

        if not username or not password:
            messagebox.showerror("Error", "Por favor, ingresa un nombre de usuario y contraseña.")
            return

        c.execute("SELECT * FROM usuarios WHERE username=?", (username,))
        if c.fetchone() is not None:
            messagebox.showerror("Error", "El nombre de usuario ya está en uso.")
        else:
            c.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Éxito", "Registro exitoso. Por favor, inicia sesión.")
            registro_window.destroy()
            root.deiconify()

    tk.Label(registro_window, text="Nombre de usuario:").grid(row=0, column=0)
    tk.Entry(registro_window, textvariable=username_registro_var).grid(row=0, column=1)
    tk.Label(registro_window, text="Contraseña:").grid(row=1, column=0)
    tk.Entry(registro_window, textvariable=password_registro_var, show="*").grid(row=1, column=1)
    tk.Button(registro_window, text="Registrar", command=agregar_usuario).grid(row=2, columnspan=2, pady=10)

root = tk.Tk()
root.title("Inicio de Sesión")

username_login_var = tk.StringVar()
password_login_var = tk.StringVar()
imagen = Image.open("moto.png")
imagen = imagen.resize((300, 300))
imagen = ImageTk.PhotoImage(imagen)

imagen_label = tk.Label(root, image=imagen)
imagen_label.image = imagen
imagen_label.grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(root, text="Nombre de usuario:").grid(row=1, column=0, pady=5)
tk.Entry(root, textvariable=username_login_var).grid(row=1, column=1, pady=5)
tk.Label(root, text="Contraseña:").grid(row=2, column=0, pady=5)
tk.Entry(root, textvariable=password_login_var, show="*").grid(row=2, column=1, pady=5)
tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion).grid(row=3, column=0, columnspan=2, pady=10)

registro_link = tk.Label(root, text="¿No tienes una cuenta? Regístrate aquí", fg="blue", cursor="hand2")
registro_link.grid(row=4, column=0, columnspan=2)
registro_link.bind("<Button-1>", lambda e: abrir_registro())

root.mainloop()

conn.close()
