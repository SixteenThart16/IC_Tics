import tkinter as tk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Diccionario para almacenar usuarios y contraseñas
usuarios = {"admin": "admin123"}

# Crear objeto para el sistema difuso
sistema_difuso = ctrl.ControlSystem([])

# Variables de entrada
ansiedad = ctrl.Antecedent(np.arange(0, 11, 1), 'ansiedad')

# Funciones de membresía para la ansiedad
ansiedad['baja'] = fuzz.trimf(ansiedad.universe, [0, 0, 5])
ansiedad['media'] = fuzz.trimf(ansiedad.universe, [0, 5, 10])
ansiedad['alta'] = fuzz.trimf(ansiedad.universe, [5, 10, 10])

# Variables de salida
consejos = ctrl.Consequent(np.arange(0, 11, 1), 'consejos')

# Funciones de membresía para los consejos
consejos['bajo'] = fuzz.trimf(consejos.universe, [0, 0, 5])
consejos['medio'] = fuzz.trimf(consejos.universe, [0, 5, 10])
consejos['alto'] = fuzz.trimf(consejos.universe, [5, 10, 10])

# Reglas
regla1 = ctrl.Rule(ansiedad['baja'], consejos['bajo'])
regla2 = ctrl.Rule(ansiedad['media'], consejos['medio'])
regla3 = ctrl.Rule(ansiedad['alta'], consejos['alto'])

# Agregar reglas al sistema difuso
sistema_difuso.addrule(regla1)
sistema_difuso.addrule(regla2)
sistema_difuso.addrule(regla3)

# Crear objeto de simulación
simulacion = ctrl.ControlSystemSimulation(sistema_difuso)

# Función para realizar el test de ansiedad
def realizar_test():
    if usuario_logueado:
        preguntas = [
            ("¿Sientes frecuentes ataques de pánico?", 1),
            ("¿Te cuesta trabajo conciliar el sueño debido a la preocupación?", 1),
            ("¿Te sientes irritable o nervioso la mayor parte del tiempo?", 1),
            ("¿Evitas situaciones que te causan ansiedad?", 1),
            ("¿Tienes dificultad para concentrarte en tus actividades diarias debido a la ansiedad?", 1)
        ]
        respuestas = []
        for pregunta, valor in preguntas:
            respuesta = messagebox.askyesno("Pregunta", pregunta)
            respuestas.append(valor if respuesta else 0)
        
        # Calcular puntaje de ansiedad
        ansiedad_valor = sum(respuestas)
        simulacion.input['ansiedad'] = ansiedad_valor
        simulacion.compute()
        consejo_valor = simulacion.output['consejos']
        messagebox.showinfo("Resultado", f"Tienes ansiedad con un grado de {consejo_valor:.2f}.\n\nConsejos: {obtener_consejos(consejo_valor)}")
    else:
        messagebox.showinfo("Iniciar sesión", "Necesitas iniciar sesión para realizar el test.")

# Función para obtener consejos basados en el grado de ansiedad
def obtener_consejos(valor):
    if valor <= 3:
        return "Intenta practicar técnicas de relajación, como la respiración profunda o la meditación."
    elif valor <= 7:
        return "Es importante hablar con alguien de confianza sobre tus preocupaciones y buscar actividades que te relajen."
    else:
        return "Te recomendamos buscar ayuda profesional para abordar tus niveles de ansiedad."

# Función para iniciar sesión
def iniciar_sesion():
    global ventana_inicio_sesion
    ventana_inicio_sesion = Toplevel(root)
    ventana_inicio_sesion.title("Inicio de Sesión")
    
    # Crear y posicionar los elementos en la ventana emergente
    label_usuario = tk.Label(ventana_inicio_sesion, text="Usuario:")
    label_usuario.grid(row=0, column=0)
    entry_usuario = tk.Entry(ventana_inicio_sesion)
    entry_usuario.grid(row=0, column=1)
    
    label_contrasena = tk.Label(ventana_inicio_sesion, text="Contraseña:")
    label_contrasena.grid(row=1, column=0)
    entry_contrasena = tk.Entry(ventana_inicio_sesion, show="*")
    entry_contrasena.grid(row=1, column=1)
    
    btn_iniciar_sesion_ventana = tk.Button(ventana_inicio_sesion, text="Iniciar Sesión", command=lambda: iniciar_sesion_accion(entry_usuario.get(), entry_contrasena.get()))
    btn_iniciar_sesion_ventana.grid(row=2, columnspan=2)

# Función para realizar el inicio de sesión
def iniciar_sesion_accion(usuario, contrasena):
    # Verificar si el usuario existe y la contraseña es correcta
    if usuario in usuarios and usuarios[usuario] == contrasena:
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso.")
        mostrar_usuario(usuario)
        btn_iniciar_sesion.pack_forget()  # Ocultar botón de iniciar sesión
        btn_registro.pack_forget()  # Ocultar botón de registro
        btn_cerrar_sesion.pack(side="right")  # Mostrar botón de cerrar sesión
        global usuario_logueado
        usuario_logueado = True
        ventana_inicio_sesion.destroy()  # Cerrar ventana de inicio de sesión
    else:
        messagebox.showerror("Inicio de sesión", "Usuario o contraseña incorrectos.")

# Función para mostrar el nombre de usuario
def mostrar_usuario(usuario):
    label_usuario.config(text=f"Bienvenido, {usuario}")

# Función para cerrar sesión
def cerrar_sesion():
    label_usuario.config(text="")
    btn_iniciar_sesion.pack(side="right")  # Mostrar botón de iniciar sesión
    btn_registro.pack(side="right")  # Mostrar botón de registro
    btn_cerrar_sesion.pack_forget()  # Ocultar botón de cerrar sesión
    btn_test.config(state="disabled")  # Deshabilitar botón para realizar el test
    global usuario_logueado
    usuario_logueado = False
    messagebox.showinfo("Cerrar sesión", "Sesión cerrada exitosamente.")

# Función para abrir una ventana emergente y realizar el registro
def registrar_usuario():
    global ventana_registro  # Definir como variable global
    ventana_registro = Toplevel(root)
    ventana_registro.title("Registro de Usuario")
    
    # Crear y posicionar los elementos en la ventana emergente
    label_usuario_nuevo = tk.Label(ventana_registro, text="Nuevo usuario:")
    label_usuario_nuevo.grid(row=0, column=0)
    global entry_usuario_nuevo
    entry_usuario_nuevo = tk.Entry(ventana_registro)
    entry_usuario_nuevo.grid(row=0, column=1)
    
    label_contrasena_nueva = tk.Label(ventana_registro, text="Nueva contraseña:")
    label_contrasena_nueva.grid(row=1, column=0)
    global entry_contrasena_nueva
    entry_contrasena_nueva = tk.Entry(ventana_registro, show="*")
    entry_contrasena_nueva.grid(row=1, column=1)
    
    btn_registrar = tk.Button(ventana_registro, text="Registrar", command=registrar)
    btn_registrar.grid(row=2, columnspan=2)

# Función para registrar usuario
def registrar():
    usuario = entry_usuario_nuevo.get()
    contrasena = entry_contrasena_nueva.get()
    # Verificar si el usuario ya existe
    if usuario in usuarios:
        messagebox.showerror("Registro de usuario", "El usuario ya existe.")
    elif usuario and contrasena:
        usuarios[usuario] = contrasena
        messagebox.showinfo("Registro de usuario", "Usuario registrado exitosamente.")
        ventana_registro.destroy()  # Cerrar ventana de registro

# Configurar la ventana principal
root = tk.Tk()
root.title("Test de Ansiedad")

# Ajustar el tamaño de la ventana
root.geometry("800x600")

# Crear un marco para mostrar el nombre de usuario
frame_usuario = tk.Frame(root)
frame_usuario.pack(side="top", fill="x")

# Etiqueta para mostrar el nombre de usuario
label_usuario = tk.Label(frame_usuario, text="")
label_usuario.pack(side="right")

# Botón para iniciar sesión
btn_iniciar_sesion = tk.Button(frame_usuario, text="Iniciar Sesión", command=iniciar_sesion)
btn_iniciar_sesion.pack(side="right")

# Botón para registrar usuario
btn_registro = tk.Button(frame_usuario, text="Registro", command=registrar_usuario)
btn_registro.pack(side="right")

# Botón para cerrar sesión
btn_cerrar_sesion = tk.Button(frame_usuario, text="Cerrar Sesión", command=cerrar_sesion)

# Botón para realizar el test de ansiedad
btn_test = tk.Button(root, text="Realizar Test", command=realizar_test)
btn_test.pack(side="bottom")

# Variable para controlar el estado de inicio de sesión
usuario_logueado = False

# Estilos de los botones
btn_iniciar_sesion.configure(bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), borderwidth=3, relief="raised")
btn_registro.configure(bg="#008CBA", fg="white", font=("Arial", 12, "bold"), borderwidth=3, relief="raised")
btn_cerrar_sesion.configure(bg="#f44336", fg="white", font=("Arial", 12, "bold"), borderwidth=3, relief="raised")
btn_test.configure(bg="#FFD700", fg="black", font=("Arial", 14, "bold"), borderwidth=3, relief="raised")

# Ejecutar la aplicación
root.mainloop()
