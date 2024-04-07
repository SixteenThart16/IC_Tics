importar numpy como np
importar skfuzzy como pelusa
de skfuzzy importar control como ctrl

# Nuevos objetos Antecedentes/Consecuentes contienen variables y membresía del universo
# funciones
calidad = ctrl.Antecedente(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedente(np.arange(0, 11, 1), 'servicio')
punta = ctrl.Consecuente(np.arange(0, 26, 1), 'consejos')

# La población de funciones de membresía automática es posible con .automf(3, 5 o 7)
calidad.automático(3)
servicio.automático(3)

# Las funciones de membresía personalizadas se pueden construir interactivamente con un familiar,
# API pitónica
punta['bajo'] = pelusa.recortar(punta.universo, [0, 0, 13])
punta['medio'] = pelusa.recortar(punta.universo, [0, 13, 25])
punta['alto'] = pelusa.recortar(tip.universe, [13, 25, 25])