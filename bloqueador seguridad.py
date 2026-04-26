# ============================================================
# PROYECTO: SHIELDGUARD 1.0
# AUTOR: GabrielG320
# ============================================================
# DESCRIPCIÓN: 
# Simulador de control de acceso que solicita una contraseña 
# maestra y gestiona un límite de intentos antes de bloquearse.
#
# LO QUE APRENDÍ Y DESAFÍOS:
# 1. El gran problema de la "f": Descubrí que sin poner la 'f' antes 
#    de las comillas, el contador de intentos no se actualizaba solo.
# 2. Gestión de contadores: Aprendí a restar vidas (intentos = intentos - 1) 
#    dentro de un bucle para controlar el flujo.
# 3. Estructura limpia: Logré simplificar el código eliminando 'if' innecesarios 
#    gracias a usar variables dinámicas dentro del print.
#
# TIEMPO DE DESARROLLO: Una tarde en entender cómo funcionan los bucles 
#                      y la interpolación de variables.
# ============================================================

clave_maestra="1234"
intentos=3
while intentos>0:
    intento=input("introduce la clave: ")

    if intento==clave_maestra:
        print("Bienvenido")
        break
    else:
        intentos = intentos -1
        
        if intentos== 2:
            print ("te quedan 2 intentos ")
        elif intentos==1:
            print ("te queda 1 intento ")
if intentos == 0:
    print("aplicacion bloqueada")