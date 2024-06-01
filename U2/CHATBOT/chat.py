import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def evaluar_respuestas():
    try:
        presupuesto_val = int(presupuesto_var.get())
        potencia_val = int(potencia_var.get())
        uso_val = int(uso_var.get())
        zona_val = int(zona_var.get())

        recomendacion_simulador.input['presupuesto'] = presupuesto_val
        recomendacion_simulador.input['potencia'] = potencia_val
        recomendacion_simulador.input['uso'] = uso_val
        recomendacion_simulador.input['zona'] = zona_val

        recomendacion_simulador.compute()
        resultado = recomendacion_simulador.output['recomendacion']

        tipo_motocicleta = ""
        if resultado <= 3:
            tipo_motocicleta = "Motocicleta de Trabajo"
        elif resultado <= 7:
            tipo_motocicleta = "Motocicleta Doble Propósito"
        else:
            tipo_motocicleta = "Motocicleta Deportiva"

        recomendacion_label.config(text="Recomendación: " + str(resultado) + " (" + tipo_motocicleta + ")")
        recomendacion_frame.grid(row=6, column=1) 
    except Exception as e:
        messagebox.showerror("Error", str(e))


def limpiar_respuestas():
    presupuesto_var.set("")
    potencia_var.set("")
    uso_var.set("")
    zona_var.set("")
    recomendacion_frame.grid_forget()  

root = tk.Tk()
root.title("Recomendación de Motocicletas")

presupuesto_var = tk.StringVar()
potencia_var = tk.StringVar()
uso_var = tk.StringVar()
zona_var = tk.StringVar()

opciones = [str(i) for i in range(1, 11)]  
root.geometry("1050x500")

imagen_izquierda = Image.open("izquierda.png")  
imagen_izquierda = imagen_izquierda.resize((200, 200)) 
imagen_izquierda = ImageTk.PhotoImage(imagen_izquierda)
imagen_izquierda_label = ttk.Label(root, image=imagen_izquierda)

preguntas_frame = tk.Frame(root)
preguntas_frame.grid(row=1, column=1, pady=10) 

header_label = tk.Label(root, text="RECOMENDACIÓN DE MOTOCICLETAS", font=("Arial", 18))
header_label.grid(row=0, column=1, pady=10)

botones_frame = tk.Frame(root)

preguntas = [
    ("1. ¿Cuál es tu presupuesto para comprar una motocicleta?", presupuesto_var),
    ("2. ¿Qué nivel de potencia prefieres en una motocicleta?", potencia_var),
    ("3. ¿Cómo describirías tu uso previsto de la motocicleta?", uso_var),
    ("4. ¿En qué tipo de zona principal usarás la motocicleta?", zona_var)
]

for i, (pregunta, variable) in enumerate(preguntas):
    label = tk.Label(preguntas_frame, text=pregunta, font=("Arial", 12))
    label.grid(row=i, column=0, sticky="w", padx=10, pady=5)
    menu = ttk.Combobox(preguntas_frame, textvariable=variable, values=opciones, state="readonly", width=5)
    menu.grid(row=i, column=1, padx=10, pady=5)

indicaciones_texto = "Rangos de Respuesta:\n1 al 3: Bajo\n4 al 7: Medio\n8 al 10: Alto\nEn la ultima pregunta los rangos son Rural, Semi-Urbano y Urbano Respectivamente de Menor a Mayor"
indicaciones_label = tk.Label(root, text=indicaciones_texto, font=("Arial", 10), justify="center", anchor="center")
indicaciones_label.grid(row=2, column=1, pady=5, sticky="nsew")

# Variables difusas
presupuesto = ctrl.Antecedent(np.arange(1, 11, 1), 'presupuesto')
potencia = ctrl.Antecedent(np.arange(1, 11, 1), 'potencia')
uso = ctrl.Antecedent(np.arange(1, 11, 1), 'uso')
zona = ctrl.Antecedent(np.arange(1, 11, 1), 'zona')
recomendacion = ctrl.Consequent(np.arange(1, 11, 1), 'recomendacion')

# Funciones de membresía
presupuesto.automf(3, names=['bajo', 'medio', 'alto'])
potencia.automf(3, names=['baja', 'media', 'alta'])
uso.automf(3, names=['bajo', 'medio', 'alto']) 
zona.automf(3, names=['rural', 'suburbana', 'urbana'])
recomendacion.automf(3, names=['poca', 'moderada', 'alta'])

# Definir reglas difusas
reglas = [
    ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['bajo'] & zona['rural'], recomendacion['poca']),
    ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['medio'] & zona['suburbana'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['alto'] & zona['urbana'], recomendacion['alta']),
    ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['bajo'] & zona['suburbana'], recomendacion['poca']),
    ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['medio'] & zona['rural'], recomendacion['poca']),
    ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['alto'] & zona['urbana'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['medio'] & zona['urbana'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['bajo'] & zona['suburbana'], recomendacion['poca']),
    ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['bajo'] & zona['rural'], recomendacion['poca']),
    ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['bajo'] & zona['urbana'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['medio'] & zona['suburbana'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['alto'] & zona['rural'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['alto'] & zona['urbana'], recomendacion['alta']),
    ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['bajo'] & zona['suburbana'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['bajo'] & zona['rural'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['bajo'] & zona['urbana'], recomendacion['alta']),
    ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['bajo'] & zona['urbana'], recomendacion['poca']),
    ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['alto'] & zona['suburbana'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['medio'] & zona['rural'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['alto'] & zona['urbana'], recomendacion['alta']),
    ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['bajo'] & zona['rural'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['medio'] & zona['suburbana'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['alto'] & zona['urbana'], recomendacion['alta']),
    ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['bajo'] & zona['suburbana'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['medio'] & zona['rural'], recomendacion['alta']),
    ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['alto'] & zona['urbana'], recomendacion['alta']),
    ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['bajo'] & zona['suburbana'], recomendacion['moderada']),
    ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['bajo'] & zona['urbana'], recomendacion['alta']),
    ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['medio'] & zona['rural'], recomendacion['alta']),
    ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['medio'] & zona['suburbana'], recomendacion['alta']),
    ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['alto'] & zona['urbana'], recomendacion['alta'])
]

recomendacion_ctrl = ctrl.ControlSystem(reglas)
recomendacion_simulador = ctrl.ControlSystemSimulation(recomendacion_ctrl)

recomendacion_frame = tk.Frame(root)
recomendacion_label = tk.Label(recomendacion_frame, text="")
recomendacion_label.pack()

imagen_derecha = Image.open("derecha.png")  
imagen_derecha = imagen_derecha.resize((200, 200))
imagen_derecha = ImageTk.PhotoImage(imagen_derecha)
imagen_derecha_label = ttk.Label(root, image=imagen_derecha)

imagen_izquierda_label.grid(row=1, column=0, padx=10, pady=10, rowspan=5)
imagen_derecha_label.grid(row=1, column=2, padx=10, pady=10, rowspan=5)


botones_frame = tk.Frame(root)
botones_frame.grid(row=5, column=1, pady=10)

evaluar_button = tk.Button(botones_frame, text="Evaluar Respuestas", command=evaluar_respuestas)
evaluar_button.pack(side=tk.LEFT, padx=5)
limpiar_button = tk.Button(botones_frame, text="Limpiar Respuestas", command=limpiar_respuestas)
limpiar_button.pack(side=tk.LEFT, padx=5)

root.mainloop()