import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definición de las variables de entrada
presupuesto = ctrl.Antecedent(np.arange(0, 15001, 1), 'presupuesto')
potencia = ctrl.Antecedent(np.arange(0, 11, 1), 'potencia')
uso = ctrl.Antecedent(np.arange(0, 5, 1), 'uso')
zona = ctrl.Antecedent(np.arange(0, 3, 1), 'zona')

# Definición de las variables de salida
recomendación = ctrl.Consequent(np.arange(0, 4, 1), 'recomendación')

# Definición de las funciones de membresía para las variables de entrada
presupuesto['bajo'] = fuzz.trimf(presupuesto.universe, [0, 5000, 10000])
presupuesto['medio'] = fuzz.trimf(presupuesto.universe, [5000, 10000, 15000])
presupuesto['alto'] = fuzz.trimf(presupuesto.universe, [10000, 15000, 15000])

potencia['baja'] = fuzz.trimf(potencia.universe, [0, 0, 5])
potencia['media'] = fuzz.trimf(potencia.universe, [0, 5, 10])
potencia['alta'] = fuzz.trimf(potencia.universe, [5, 10, 10])

uso['esporádico'] = fuzz.trimf(uso.universe, [0, 0, 1])
uso['regular'] = fuzz.trimf(uso.universe, [0, 1, 2])
uso['frecuente'] = fuzz.trimf(uso.universe, [1, 2, 3])
uso['muy_frecuente'] = fuzz.trimf(uso.universe, [2, 3, 4])

zona['rural'] = fuzz.trimf(zona.universe, [0, 0, 1])
zona['semi_urbano'] = fuzz.trimf(zona.universe, [0, 1, 2])
zona['urbano'] = fuzz.trimf(zona.universe, [1, 2, 2])

# Definición de las funciones de membresía para las variables de salida
recomendación['trabajo'] = fuzz.trimf(recomendación.universe, [0, 0, 1])
recomendación['doble_propósito'] = fuzz.trimf(recomendación.universe, [0, 1, 2])
recomendación['deportiva'] = fuzz.trimf(recomendación.universe, [1, 2, 3])

# Reglas difusas
regla1 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['esporádico'] & zona['rural'], recomendación['trabajo'])
regla2 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['esporádico'] & zona['semi_urbano'], recomendación['trabajo'])
regla3 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['esporádico'] & zona['urbano'], recomendación['trabajo'])
regla4 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['regular'] & zona['rural'], recomendación['trabajo'])
regla5 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['regular'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla6 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['regular'] & zona['urbano'], recomendación['trabajo'])
regla7 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['frecuente'] & zona['rural'], recomendación['trabajo'])
regla8 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla9 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla10 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['muy_frecuente'] & zona['rural'], recomendación['trabajo'])
regla11 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['muy_frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla12 = ctrl.Rule(presupuesto['bajo'] & potencia['baja'] & uso['muy_frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla13 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['esporádico'] & zona['rural'], recomendación['trabajo'])
regla14 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['esporádico'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla15 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['esporádico'] & zona['urbano'], recomendación['trabajo'])
regla16 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['regular'] & zona['rural'], recomendación['trabajo'])
regla17 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['regular'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla18 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['regular'] & zona['urbano'], recomendación['trabajo'])
regla19 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['frecuente'] & zona['rural'], recomendación['trabajo'])
regla20 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla21 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla22 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['muy_frecuente'] & zona['rural'], recomendación['trabajo'])
regla23 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['muy_frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla24 = ctrl.Rule(presupuesto['bajo'] & potencia['media'] & uso['muy_frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla25 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['esporádico'] & zona['rural'], recomendación['trabajo'])
regla26 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['esporádico'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla27 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['esporádico'] & zona['urbano'], recomendación['trabajo'])
regla28 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['regular'] & zona['rural'], recomendación['trabajo'])
regla29 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['regular'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla30 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['regular'] & zona['urbano'], recomendación['trabajo'])
regla31 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['frecuente'] & zona['rural'], recomendación['trabajo'])
regla32 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla33 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla34 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['muy_frecuente'] & zona['rural'], recomendación['trabajo'])
regla35 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['muy_frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla36 = ctrl.Rule(presupuesto['bajo'] & potencia['alta'] & uso['muy_frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla37 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['esporádico'] & zona['rural'], recomendación['trabajo'])
regla38 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['esporádico'] & zona['semi_urbano'], recomendación['trabajo'])
regla39 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['esporádico'] & zona['urbano'], recomendación['trabajo'])
regla40 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['regular'] & zona['rural'], recomendación['trabajo'])
regla41 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['regular'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla42 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['regular'] & zona['urbano'], recomendación['trabajo'])
regla43 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['frecuente'] & zona['rural'], recomendación['trabajo'])
regla44 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla45 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla46 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['muy_frecuente'] & zona['rural'], recomendación['trabajo'])
regla47 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['muy_frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla48 = ctrl.Rule(presupuesto['medio'] & potencia['baja'] & uso['muy_frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla49 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['esporádico'] & zona['rural'], recomendación['trabajo'])
regla50 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['esporádico'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla51 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['esporádico'] & zona['urbano'], recomendación['trabajo'])
regla52 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['regular'] & zona['rural'], recomendación['trabajo'])
regla53 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['regular'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla54 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['regular'] & zona['urbano'], recomendación['trabajo'])
regla55 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['frecuente'] & zona['rural'], recomendación['trabajo'])
regla56 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla57 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla58 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['muy_frecuente'] & zona['rural'], recomendación['trabajo'])
regla59 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['muy_frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla60 = ctrl.Rule(presupuesto['medio'] & potencia['media'] & uso['muy_frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla61 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['esporádico'] & zona['rural'], recomendación['trabajo'])
regla62 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['esporádico'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla63 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['esporádico'] & zona['urbano'], recomendación['trabajo'])
regla64 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['regular'] & zona['rural'], recomendación['trabajo'])
regla65 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['regular'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla66 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['regular'] & zona['urbano'], recomendación['trabajo'])
regla67 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['frecuente'] & zona['rural'], recomendación['trabajo'])
regla68 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla69 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla70 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['muy_frecuente'] & zona['rural'], recomendación['trabajo'])
regla71 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['muy_frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla72 = ctrl.Rule(presupuesto['medio'] & potencia['alta'] & uso['muy_frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla73 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['esporádico'] & zona['rural'], recomendación['trabajo'])
regla74 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['esporádico'] & zona['semi_urbano'], recomendación['trabajo'])
regla75 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['esporádico'] & zona['urbano'], recomendación['trabajo'])
regla76 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['regular'] & zona['rural'], recomendación['trabajo'])
regla77 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['regular'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla78 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['regular'] & zona['urbano'], recomendación['trabajo'])
regla79 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['frecuente'] & zona['rural'], recomendación['trabajo'])
regla80 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla81 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla82 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['muy_frecuente'] & zona['rural'], recomendación['trabajo'])
regla83 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['muy_frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla84 = ctrl.Rule(presupuesto['alto'] & potencia['baja'] & uso['muy_frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla85 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['esporádico'] & zona['rural'], recomendación['trabajo'])
regla86 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['esporádico'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla87 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['esporádico'] & zona['urbano'], recomendación['trabajo'])
regla88 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['regular'] & zona['rural'], recomendación['trabajo'])
regla89 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['regular'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla90 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['regular'] & zona['urbano'], recomendación['trabajo'])
regla91 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['frecuente'] & zona['rural'], recomendación['trabajo'])
regla92 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla93 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla94 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['muy_frecuente'] & zona['rural'], recomendación['trabajo'])
regla95 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['muy_frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla96 = ctrl.Rule(presupuesto['alto'] & potencia['media'] & uso['muy_frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla97 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['esporádico'] & zona['rural'], recomendación['trabajo'])
regla98 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['esporádico'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla99 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['esporádico'] & zona['urbano'], recomendación['trabajo'])
regla100 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['regular'] & zona['rural'], recomendación['trabajo'])
regla101 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['regular'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla102 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['regular'] & zona['urbano'], recomendación['trabajo'])
regla103 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['frecuente'] & zona['rural'], recomendación['trabajo'])
regla104 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla105 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['frecuente'] & zona['urbano'], recomendación['doble_propósito'])
regla106 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['muy_frecuente'] & zona['rural'], recomendación['trabajo'])
regla107 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['muy_frecuente'] & zona['semi_urbano'], recomendación['doble_propósito'])
regla108 = ctrl.Rule(presupuesto['alto'] & potencia['alta'] & uso['muy_frecuente'] & zona['urbano'], recomendación['doble_propósito'])

# Define the rest of your rules similarly

# Creación del sistema de control difuso
sistema_control = ctrl.ControlSystem([
    regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9, regla10,
    regla11, regla12, regla13, regla14, regla15, regla16, regla17, regla18, regla19, regla20,
    regla21, regla22, regla23, regla24, regla25, regla26, regla27, regla28, regla29, regla30,
    regla31, regla32, regla33, regla34, regla35, regla36, regla37, regla38, regla39, regla40,
    regla41, regla42, regla43, regla44, regla45, regla46, regla47, regla48, regla49, regla50,
    regla51, regla52, regla53, regla54, regla55, regla56, regla57, regla58, regla59, regla60,
    regla61, regla62, regla63, regla64, regla65, regla66, regla67, regla68, regla69, regla70,
    regla71, regla72, regla73, regla74, regla75, regla76, regla77, regla78, regla79, regla80,
    regla81, regla82, regla83, regla84, regla85, regla86, regla87, regla88, regla89, regla90,
    regla91, regla92, regla93, regla94, regla95, regla96, regla97, regla98, regla99, regla100,
    regla101, regla102, regla103, regla104, regla105, regla106, regla107, regla108,
])

sistema = ctrl.ControlSystemSimulation(sistema_control)

# Establecimiento de los valores de entrada
sistema.input['presupuesto'] = 5000  # Ejemplo, puedes ajustar el valor
sistema.input['potencia'] = 2  # Ejemplo, puedes ajustar el valor
sistema.input['uso'] = 0.5  # Ejemplo, puedes ajustar el valor
sistema.input['zona'] = 0.5  # Ejemplo, puedes ajustar el valor

# Computación de la salida
sistema.compute()

# Visualización de la salida
print(sistema.output['recomendación'])
recomendación.view(sim=sistema)

