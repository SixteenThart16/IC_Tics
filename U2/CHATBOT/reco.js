function obtenerRecomendacion(presupuesto, potencia, uso, zona) {
    let recomendacion = '';  
    if (presupuesto === 'Bajo' && potencia === 'Baja' && uso === 'Esporádico' && zona === 'Rural') {
        recomendacion = 'Trabajo(FT125 ITALIKA, Honda CB1100)';
    } else if (presupuesto === 'Bajo' && potencia === 'Baja' && uso === 'Esporádico' && zona === 'Urbana') {
        recomendacion = 'Trabajo(Honda CG125, Yamaha YBR125)';
    } else if (presupuesto === 'Bajo' && potencia === 'Baja' && uso === 'Esporádico' && zona === 'Semi_urbana') {
        recomendacion = 'Trabajo(Yamaha XTZ125, Suzuki GN125)';
    } else if (presupuesto === 'Bajo' && potencia === 'Baja' && uso === 'Regular' && zona === 'Rural') {
        recomendacion = 'Trabajo(Suzuki EN125, Kawasaki GTO125)';
    } else if (presupuesto === 'Bajo' && potencia === 'Baja' && uso === 'Regular' && zona === 'Urbana') {
        recomendacion = 'Trabajo(Kawasaki KSR110, BMW G310R)';
    } else if (presupuesto === 'Bajo' && potencia === 'Baja' && uso === 'Regular' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Suzuki DR200S, Honda XR150L)';
    } else if (presupuesto === 'Bajo' && potencia === 'Baja' && uso === 'Frecuente' && zona === 'Rural') {
        recomendacion = 'Doble propósito(Honda CRF250L, Kawasaki KLX150BF)';
    } else if (presupuesto === 'Bajo' && potencia === 'Baja' && uso === 'Frecuente' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(KTM 200 Duke, Suzuki Gixxer SF)';
    } else if (presupuesto === 'Bajo' && potencia === 'Baja' && uso === 'Frecuente' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Yamaha XT250, Royal Enfield Himalayan)';
    } else if (presupuesto === 'Bajo' && potencia === 'Baja' && uso === 'Muy_frecuente' && zona === 'Rural') {
        recomendacion = 'Doble propósito(Honda CRF450X, Kawasaki KLX450R)';
    } else if (presupuesto === 'Bajo' && potencia === 'Baja' && uso === 'Muy_frecuente' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(Suzuki DR-Z400SM, Yamaha WR250R)';
    } else if (presupuesto === 'Bajo' && potencia === 'Baja' && uso === 'Muy_frecuente' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Honda CRF250 Rally, Kawasaki Versys-X 300)';
    } else if (presupuesto === 'Bajo' && potencia === 'Media' && uso === 'Esporádico' && zona === 'Rural') {
        recomendacion = 'Doble propósito(Suzuki V-Strom 250, Honda CB300R)';
    } else if (presupuesto === 'Bajo' && potencia === 'Media' && uso === 'Esporádico' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(KTM 390 Adventure, BMW G310GS)';
    } else if (presupuesto === 'Bajo' && potencia === 'Media' && uso === 'Esporádico' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Honda CRF300L, Yamaha Tenere 300)';
    } else if (presupuesto === 'Bajo' && potencia === 'Media' && uso === 'Regular' && zona === 'Rural') {
        recomendacion = 'Doble propósito(Honda CRF450RL, Suzuki DR650S)';
    } else if (presupuesto === 'Bajo' && potencia === 'Media' && uso === 'Regular' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(KTM 790 Adventure, BMW F850GS)';
    } else if (presupuesto === 'Bajo' && potencia === 'Media' && uso === 'Regular' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Kawasaki KLR650, Honda Africa Twin)';
    } else if (presupuesto === 'Bajo' && potencia === 'Media' && uso === 'Frecuente' && zona === 'Rural') {
        recomendacion = 'Doble propósito(Yamaha Tenere 700, Honda CB500X)';
    } else if (presupuesto === 'Bajo' && potencia === 'Media' && uso === 'Frecuente' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(KTM 1290 Super Adventure, BMW R1250GS)';
    } else if (presupuesto === 'Bajo' && potencia === 'Media' && uso === 'Frecuente' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Suzuki DR-Z400S, Honda CRF450L)';
    } else if (presupuesto === 'Bajo' && potencia === 'Media' && uso === 'Muy_frecuente' && zona === 'Rural') {
        recomendacion = 'Doble propósito(Kawasaki KLX300R, Yamaha WR450F)';
    } else if (presupuesto === 'Bajo' && potencia === 'Media' && uso === 'Muy_frecuente' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(Husqvarna 701 Enduro, KTM 690 Enduro R)';
    } else if (presupuesto === 'Bajo' && potencia === 'Media' && uso === 'Muy_frecuente' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Beta 500 RR-S, Suzuki DR650SE)';
    } else if (presupuesto === 'Bajo' && potencia === 'Alta' && uso === 'Esporádico' && zona === 'Rural') {
        recomendacion = 'Deportiva(Yamaha YZF-R3, Kawasaki Ninja 400)';
    } else if (presupuesto === 'Bajo' && potencia === 'Alta' && uso === 'Esporádico' && zona === 'Urbana') {
        recomendacion = 'Deportiva(KTM RC 390, Suzuki GSX250R)';
    } else if (presupuesto === 'Bajo' && potencia === 'Alta' && uso === 'Esporádico' && zona === 'Semi_urbana') {
        recomendacion = 'Deportiva(Honda CBR300R, Yamaha MT-03)';
    } else if (presupuesto === 'Bajo' && potencia === 'Alta' && uso === 'Regular' && zona === 'Rural') {
        recomendacion = 'Deportiva(Kawasaki Ninja ZX-6R, Yamaha YZF-R6)';
    } else if (presupuesto === 'Bajo' && potencia === 'Alta' && uso === 'Regular' && zona === 'Urbana') {
        recomendacion = 'Deportiva(Suzuki GSX-R750, Honda CBR650R)';
    } else if (presupuesto === 'Bajo' && potencia === 'Alta' && uso === 'Regular' && zona === 'Semi_urbana') {
        recomendacion = 'Deportiva(KTM 1290 Super Duke R, Ducati Panigale V2)';
    } else if (presupuesto === 'Bajo' && potencia === 'Alta' && uso === 'Frecuente' && zona === 'Rural') {
        recomendacion = 'Deportiva(BMW S 1000 RR, Aprilia RSV4)';
    } else if (presupuesto === 'Bajo' && potencia === 'Alta' && uso === 'Frecuente' && zona === 'Urbana') {
        recomendacion = 'Deportiva(Ducati Streetfighter V4, MV Agusta Brutale 1000)';
    } else if (presupuesto === 'Bajo' && potencia === 'Alta' && uso === 'Frecuente' && zona === 'Semi_urbana') {
        recomendacion = 'Deportiva(Kawasaki Ninja H2 SX, Suzuki Hayabusa)';
    } else if (presupuesto === 'Bajo' && potencia === 'Alta' && uso === 'Muy_frecuente' && zona === 'Rural') {
        recomendacion = 'Deportiva(KTM 1290 Super Adventure S, Ducati Multistrada V4)';
    } else if (presupuesto === 'Bajo' && potencia === 'Alta' && uso === 'Muy_frecuente' && zona === 'Urbana') {
        recomendacion = 'Deportiva(BMW R 1250 RS, Triumph Tiger 1200)';
    } else if (presupuesto === 'Bajo' && potencia === 'Alta' && uso === 'Muy_frecuente' && zona === 'Semi_urbana') {
        recomendacion = 'Deportiva(Honda Africa Twin Adventure Sports, Yamaha Super Ténéré)';
    } else if (presupuesto === 'Medio' && potencia === 'Baja' && uso === 'Esporádico' && zona === 'Rural') {
        recomendacion = 'Doble propósito(Honda CRF250L, Kawasaki KLX230)';
    } else if (presupuesto === 'Medio' && potencia === 'Baja' && uso === 'Esporádico' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(Suzuki DR-Z400S, Yamaha XT250)';
    } else if (presupuesto === 'Medio' && potencia === 'Baja' && uso === 'Esporádico' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Honda CRF450L, Kawasaki KLR650)';
    } else if (presupuesto === 'Medio' && potencia === 'Baja' && uso === 'Regular' && zona === 'Rural') {
        recomendacion = 'Doble propósito(Yamaha Tenere 700, BMW G 310 GS)';
    } else if (presupuesto === 'Medio' && potencia === 'Baja' && uso === 'Regular' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(Suzuki V-Strom 650, Kawasaki Versys-X 300)';
    } else if (presupuesto === 'Medio' && potencia === 'Baja' && uso === 'Regular' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Honda CRF300L, Yamaha WR250R)';
    } else if (presupuesto === 'Medio' && potencia === 'Baja' && uso === 'Frecuente' && zona === 'Rural') {
        recomendacion = 'Doble propósito(KTM 790 Adventure, Ducati Scrambler Desert Sled)';
    } else if (presupuesto === 'Medio' && potencia === 'Baja' && uso === 'Frecuente' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(Honda CB500X, Kawasaki Versys 650)';
    } else if (presupuesto === 'Medio' && potencia === 'Baja' && uso === 'Frecuente' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Suzuki DR650S, Yamaha Ténéré 700)';
    } else if (presupuesto === 'Medio' && potencia === 'Baja' && uso === 'Muy_frecuente' && zona === 'Rural') {
        recomendacion = 'Doble propósito(BMW F 850 GS, Honda Africa Twin)';
    } else if (presupuesto === 'Medio' && potencia === 'Baja' && uso === 'Muy_frecuente' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(KTM 890 Adventure, Yamaha Tracer 700)';
    } else if (presupuesto === 'Medio' && potencia === 'Baja' && uso === 'Muy_frecuente' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Suzuki DR-Z400SM, Kawasaki KLX300)';
    } else if (presupuesto === 'Medio' && potencia === 'Media' && uso === 'Esporádico' && zona === 'Rural') {
        recomendacion = 'Doble propósito(Honda CRF450RL, Yamaha WR450F)';
    } else if (presupuesto === 'Medio' && potencia === 'Media' && uso === 'Esporádico' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(Suzuki SV650, Yamaha MT-07)';
    } else if (presupuesto === 'Medio' && potencia === 'Media' && uso === 'Esporádico' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Kawasaki Z650, Honda CB650R)';
    } else if (presupuesto === 'Medio' && potencia === 'Media' && uso === 'Regular' && zona === 'Rural') {
        recomendacion = 'Doble propósito(BMW F 900 R, Ducati Monster 821)';
    } else if (presupuesto === 'Medio' && potencia === 'Media' && uso === 'Regular' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(Yamaha XSR700, Triumph Street Triple)';
    } else if (presupuesto === 'Medio' && potencia === 'Media' && uso === 'Regular' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Honda CB1000R, Kawasaki Z900)';
    } else if (presupuesto === 'Medio' && potencia === 'Media' && uso === 'Frecuente' && zona === 'Rural') {
        recomendacion = 'Doble propósito(Ducati Monster 1200, BMW R NineT)';
    } else if (presupuesto === 'Medio' && potencia === 'Media' && uso === 'Frecuente' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(KTM 790 Duke, Suzuki GSX-S750)';
    } else if (presupuesto === 'Medio' && potencia === 'Media' && uso === 'Frecuente' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(Kawasaki Z900RS, Yamaha MT-09)';
    } else if (presupuesto === 'Medio' && potencia === 'Media' && uso === 'Muy_frecuente' && zona === 'Rural') {
        recomendacion = 'Doble propósito(Ducati Streetfighter V4, Aprilia Tuono V4 1100)';
    } else if (presupuesto === 'Medio' && potencia === 'Media' && uso === 'Muy_frecuente' && zona === 'Urbana') {
        recomendacion = 'Doble propósito(Triumph Speed Triple, BMW R 1250 R)';
    } else if (presupuesto === 'Medio' && potencia === 'Media' && uso === 'Muy_frecuente' && zona === 'Semi_urbana') {
        recomendacion = 'Doble propósito(KTM 1290 Super Duke R, Yamaha MT-10)';
    } else if (presupuesto === 'Medio' && potencia === 'Alta' && uso === 'Esporádico' && zona === 'Rural') {
        recomendacion = 'Deportiva(Kawasaki Ninja 650, Suzuki GSX-S1000)';
    } else if (presupuesto === 'Medio' && potencia === 'Alta' && uso === 'Esporádico' && zona === 'Urbana') {
        recomendacion = 'Deportiva(Yamaha YZF-R6, Honda CBR650R)';
    } else if (presupuesto === 'Medio' && potencia === 'Alta' && uso === 'Esporádico' && zona === 'Semi_urbana') {
        recomendacion = 'Deportiva(Ducati Panigale V2, Kawasaki Ninja ZX-6R)';
    } else if (presupuesto === 'Medio' && potencia === 'Alta' && uso === 'Regular' && zona === 'Rural') {
        recomendacion = 'Deportiva(BMW S 1000 RR, Suzuki GSX-R750)';
    } else if (presupuesto === 'Alto' && potencia === 'Alta' && uso === 'Regular' && zona === 'Semi_urbana') {
        recomendacion = 'Deportiva(Aprilia RSV4, Yamaha YZF-R1)';
    } else if (presupuesto === 'Alto' && potencia === 'Alta' && uso === 'Frecuente' && zona === 'Rural') {
        recomendacion = 'Deportiva(Ducati Panigale V4, BMW HP4)';
    } else if (presupuesto === 'Alto' && potencia === 'Alta' && uso === 'Frecuente' && zona === 'Urbana') {
        recomendacion = 'Deportiva(Kawasaki Ninja H2, Suzuki GSX-R1000)';
    } else if (presupuesto === 'Alto' && potencia === 'Alta' && uso === 'Frecuente' && zona === 'Semi_urbana') {
        recomendacion = 'Deportiva(Honda CBR1000RR, Yamaha YZF-R1M)';
    } else if (presupuesto === 'Alto' && potencia === 'Alta' && uso === 'Muy_frecuente' && zona === 'Rural') {
        recomendacion = 'Deportiva(Ducati Panigale V4 R, BMW S 1000 RR)';
    } else if (presupuesto === 'Alto' && potencia === 'Alta' && uso === 'Muy_frecuente' && zona === 'Urbana') {
        recomendacion = 'Deportiva(Aprilia RSV4 1100, Kawasaki Ninja ZX-10R)';
    } else if (presupuesto === 'Alto' && potencia === 'Alta' && uso === 'Muy_frecuente' && zona === 'Semi_urbana') {
        recomendacion = 'Deportiva(Ducati Panigale V4 SP, Yamaha YZF-R1M)';
    } else {
        recomendacion = 'No hay recomendación disponible para esta combinación';
    }
    
    return recomendacion;
}