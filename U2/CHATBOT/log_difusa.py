import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir las variables de entrada
presupuesto = ctrl.Antecedent(np.arange(0, 11, 1), 'presupuesto')
potencia = ctrl.Antecedent(np.arange(0, 11, 1), 'potencia')
uso = ctrl.Antecedent(np.arange(0, 26, 1), 'uso')
zona = ctrl.Antecedent(np.arange(0, 26, 1), 'zona')

# Definir las funciones de membresía para las variables de entrada
presupuesto.automf(3)
potencia.automf(3)
uso.automf(4, names=['esporadico', 'regular', 'frecuente', 'muy_frecuente'])
zona.automf(3)

# Definir las variables de salida
deportiva = ctrl.Consequent(np.arange(0, 101, 1), 'deportiva')
doble_proposito = ctrl.Consequent(np.arange(0, 101, 1), 'doble_proposito')
trabajo = ctrl.Consequent(np.arange(0, 101, 1), 'trabajo')

# Definir las funciones de membresía para las variables de salida
deportiva.automf(3)
doble_proposito.automf(3)
trabajo.automf(3)

presupuesto['average'].view()
deportiva.view()

# Definir las reglas
regla1 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['esporadico'] & zona['rural'], trabajo['alto'])
regla2 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['esporadico'] & zona['urbano'], trabajo['alto'])
regla3 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['esporadico'] & zona['semi-urbano'], trabajo['alto'])
regla4 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['regular'] & zona['rural'], trabajo['alto'])
regla5 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['regular'] & zona['urbano'], trabajo['alto'])
regla6 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['regular'] & zona['semi-urbano'], doble_proposito['alto'])
regla7 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['frecuente'] & zona['rural'], trabajo['alto'])
regla8 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['frecuente'] & zona['urbano'], doble_proposito['alto'])
regla9 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['frecuente'] & zona['semi-urbano'], doble_proposito['alto'])
regla10 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['muy_frecuente'] & zona['rural'], trabajo['alto'])
regla11 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['muy_frecuente'] & zona['urbano'], doble_proposito['alto'])
regla12 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['muy_frecuente'] & zona['semi-urbano'], doble_proposito['alto'])
regla13 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['esporadico'] & zona['rural'], trabajo['alto'])
regla14 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['esporadico'] & zona['urbano'], doble_proposito['alto'])
regla15 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['esporadico'] & zona['semi-urbano'], doble_proposito['alto'])
regla16 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['regular'] & zona['rural'], trabajo['alto'])
regla17 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['regular'] & zona['urbano'], doble_proposito['alto'])
regla18 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['regular'] & zona['semi-urbano'], doble_proposito['alto'])
regla19 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['frecuente'] & zona['rural'], trabajo['alto'])
regla20 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['frecuente'] & zona['urbano'], doble_proposito['alto'])
regla21 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['frecuente'] & zona['semi-urbano'], doble_proposito['alto'])
regla22 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['muy_frecuente'] & zona['rural'], trabajo['alto'])
regla23 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['muy_frecuente'] & zona['urbano'], doble_proposito['alto'])
regla24 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['muy_frecuente'] & zona['semi-urbano'], doble_proposito['alto'])
regla25 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['esporadico'] & zona['rural'], doble_proposito['alto'])
regla26 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['esporadico'] & zona['urbano'], doble_proposito['alto'])
regla27 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['esporadico'] & zona['semi-urbano'], doble_proposito['alto'])
regla28 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['regular'] & zona['rural'], doble_proposito['alto'])
regla29 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['regular'] & zona['urbano'], doble_proposito['alto'])
regla30 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['regular'] & zona['semi-urbano'], doble_proposito['alto'])
regla31 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['frecuente'] & zona['rural'], doble_proposito['alto'])
regla32 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['frecuente'] & zona['urbano'], doble_proposito['alto'])
regla33 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['frecuente'] & zona['semi-urbano'], doble_proposito['alto'])
regla34 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['muy_frecuente'] & zona['rural'], doble_proposito['alto'])
regla35 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['muy_frecuente'] & zona['urbano'], doble_proposito['alto'])
regla36 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['muy_frecuente'] & zona['semi-urbano'], doble_proposito['alto'])
regla37 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['esporadico'] & zona['rural'], trabajo['alto'])
regla38 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['esporadico'] & zona['urbano'], doble_proposito['alto'])
regla39 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['esporadico'] & zona['semi-urbano'], doble_proposito['alto'])
regla40 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['regular'] & zona['rural'], trabajo['alto'])
regla41 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['regular'] & zona['urbano'], doble_proposito['alto'])
regla42 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['regular'] & zona['semi-urbano'], doble_proposito['alto'])
regla43 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['frecuente'] & zona['rural'], trabajo['alto'])
regla44 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['frecuente'] & zona['urbano'], doble_proposito['alto'])
regla45 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['frecuente'] & zona['semi-urbano'], doble_proposito['alto'])
regla46 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['muy_frecuente'] & zona['rural'], trabajo['alto'])
regla47 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['muy_frecuente'] & zona['urbano'], doble_proposito['alto'])
regla48 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['muy_frecuente'] & zona['semi-urbano'], doble_proposito['alto'])
regla49 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['esporadico'] & zona['rural'], doble_proposito['alto'])
regla50 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['esporadico'] & zona['urbano'], doble_proposito['alto'])
regla51 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['esporadico'] & zona['semi-urbano'], doble_proposito['alto'])
regla52 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['regular'] & zona['rural'], trabajo['alto'])
regla53 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['regular'] & zona['urbano'], doble_proposito['alto'])
regla54 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['regular'] & zona['semi-urbano'], doble_proposito['alto'])
regla55 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['frecuente'] & zona['rural'], doble_proposito['alto'])
regla56 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['frecuente'] & zona['urbano'], deportiva['alto'])
regla57 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['frecuente'] & zona['semi-urbano'], doble_proposito['alto'])
regla58 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['muy_frecuente'] & zona['rural'], doble_proposito['alto'])
regla59 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['muy_frecuente'] & zona['urbano'], deportiva['alto'])
regla60 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['muy_frecuente'] & zona['semi-urbano'], trabajo['alto'])
regla61 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['esporadico'] & zona['rural'], doble_proposito['alto'])
regla62 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['esporadico'] & zona['urbano'], deportiva['alto'])
regla63 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['esporadico'] & zona['semi-urbano'], doble_proposito['alto'])
regla64 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['regular'] & zona['rural'], doble_proposito['alto'])
regla65 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['regular'] & zona['urbano'], deportiva['alto'])
regla66 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['regular'] & zona['semi-urbano'], doble_proposito['alto'])
regla67 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['frecuente'] & zona['rural'], doble_proposito['alto'])
regla68 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['frecuente'] & zona['urbano'], deportiva['alto'])
regla69 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['frecuente'] & zona['semi-urbano'], deportiva['alto'])
regla70 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['muy_frecuente'] & zona['rural'], doble_proposito['alto'])
regla71 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['muy_frecuente'] & zona['urbano'], deportiva['alto'])
regla72 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['muy_frecuente'] & zona['semi-urbano'], trabajo['alto'])
regla73 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['esporadico'] & zona['rural'], trabajo['alto'])
regla74 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['esporadico'] & zona['urbano'], doble_proposito['alto'])
regla75 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['esporadico'] & zona['semi-urbano'], doble_proposito['alto'])
regla76 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['regular'] & zona['rural'], trabajo['alto'])
regla77 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['regular'] & zona['urbano'], doble_proposito['alto'])
regla78 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['regular'] & zona['semi-urbano'], doble_proposito['alto'])
regla79 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['frecuente'] & zona['rural'], trabajo['alto'])
regla80 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['frecuente'] & zona['urbano'], doble_proposito['alto'])
regla81 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['frecuente'] & zona['semi-urbano'], doble_proposito['alto'])
regla82 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['muy_frecuente'] & zona['rural'], trabajo['alto'])
regla83 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['muy_frecuente'] & zona['urbano'], doble_proposito['alto'])
regla84 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['muy_frecuente'] & zona['semi-urbano'], doble_proposito['alto'])
regla85 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['esporadico'] & zona['rural'], doble_proposito['alto'])
regla86 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['esporadico'] & zona['urbano'], deportiva['alto'])
regla87 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['esporadico'] & zona['semi-urbano'], doble_proposito['alto'])
regla88 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['regular'] & zona['rural'], doble_proposito['alto'])
regla89 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['regular'] & zona['urbano'], deportiva['alto'])
regla90 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['regular'] & zona['semi-urbano'], doble_proposito['alto'])
regla91 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['frecuente'] & zona['rural'], doble_proposito['alto'])
regla92 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['frecuente'] & zona['urbano'], deportiva['alto'])
regla93 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['frecuente'] & zona['semi-urbano'], deportiva['alto'])
regla94 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['muy_frecuente'] & zona['rural'], doble_proposito['alto'])
regla95 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['muy_frecuente'] & zona['urbano'], deportiva['alto'])
regla96 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['muy_frecuente'] & zona['semi-urbano'], trabajo['alto'])
regla97 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['esporadico'] & zona['rural'], doble_proposito['alto'])
regla98 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['esporadico'] & zona['urbano'], deportiva['alto'])
regla99 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['esporadico'] & zona['semi-urbano'], doble_proposito['alto'])
regla100 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['regular'] & zona['rural'], doble_proposito['alto'])
regla101 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['regular'] & zona['urbano'], deportiva['alto'])
regla102 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['regular'] & zona['semi-urbano'], doble_proposito['alto'])
regla103 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['frecuente'] & zona['rural'], doble_proposito['alto'])
regla104 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['frecuente'] & zona['urbano'], deportiva['alto'])
regla105 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['frecuente'] & zona['semi-urbano'], deportiva['alto'])
regla106 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['muy_frecuente'] & zona['rural'], doble_proposito['alto'])
regla107 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['muy_frecuente'] & zona['urbano'], deportiva['alto'])
regla108 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['muy_frecuente'] & zona['semi-urbano'], trabajo['alto'])

# Crear el sistema de control difuso
sistema_ctrl = ctrl.ControlSystem([regla1, regla2, ..., regla108])

# Crear la simulación del sistema de control
simulacion = ctrl.ControlSystemSimulation(sistema_ctrl)

valor_presupuesto = 7  
valor_potencia = 8 
valor_uso = 15  
valor_zona = 20  

# Configurar las entradas
simulacion.input['presupuesto'] = valor_presupuesto
simulacion.input['potencia'] = valor_potencia
simulacion.input['uso'] = valor_uso
simulacion.input['zona'] = valor_zona

# Ejecutar la simulación
simulacion.compute()

# Obtener los resultados
resultado_deportiva = simulacion.output['deportiva']
resultado_doble_proposito = simulacion.output['doble_proposito']
resultado_trabajo = simulacion.output['trabajo']

print("Deportiva:", resultado_deportiva)
print("Doble propósito:", resultado_doble_proposito)
print("Trabajo:", resultado_trabajo)
