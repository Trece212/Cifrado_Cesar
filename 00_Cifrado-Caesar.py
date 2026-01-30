Caracteres = ['A', 'Á', 'a', 'á', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'É', 
              'e', 'é', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'Í', 'i', 'í',
              'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'Ñ', 'ñ',
              'O', 'Ó', 'o', 'ó', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's',
              'T', 't', 'U', 'Ú', 'u', 'ú', 'V', 'v', 'W', 'w', 'X', 'x',
              'Y', 'Ý', 'y', 'ý', 'Z', 'z', ' ']

# Variables para testeo
Cadena_caracteres = 'Los poemas breves son una muestra de que la expresión artística puede ocurrir con unas pocas palabras'
Cambio = 7

def calcular_posicion (caracteres_cp=list, caracter_cp=int, cambio_cp=int, direccion_cp=bool) -> int:
    total_caracteres = len(caracteres_cp) - 1

    if direccion_cp == True:
        posicion_caracter_ma = caracteres_cp.index(caracter_cp) + cambio_cp
        if posicion_caracter_ma > total_caracteres:
            convercion_m = posicion_caracter_ma - total_caracteres
            posicion_caracter_mb = 0
            for i in range(convercion_m):
                posicion_caracter_mb = i
            return posicion_caracter_mb
        else:
            return posicion_caracter_ma

    if direccion_cp == False:
        posicion_caracter_na = caracteres_cp.index(caracter_cp) - cambio_cp
        if posicion_caracter_na < 0:
            convercion_n = abs(posicion_caracter_na)
            posicion_caracter_nb = (total_caracteres - convercion_n) + 1
            return posicion_caracter_nb
        else:
            return posicion_caracter_na

def cifrar_caracteres (caracteres_cc=list, cadena_caracteres=str, cifrar=bool) -> str:
    numero_caracteres = len(cadena_caracteres)
    par_inpar = numero_caracteres % 2 == 0
    numero = 0
    salida = ""

    if par_inpar == False:
        numero += 1

    if cifrar == True:
        for i in cadena_caracteres:
            if numero == 0:
                salida = salida + caracteres_cc[calcular_posicion(Caracteres, i, Cambio, True)]
                numero += 1
            elif numero == 1:
                salida = salida + caracteres_cc[calcular_posicion(Caracteres, i, Cambio, False)]
                numero -= 1
    
    if cifrar == False:
        for i in cadena_caracteres:
            if numero == 0:
                salida = salida + caracteres_cc[calcular_posicion(Caracteres, i, Cambio, False)]
                numero += 1
            elif numero == 1:
                salida = salida + caracteres_cc[calcular_posicion(Caracteres, i, Cambio, True)]
                numero -= 1

    return salida

# Testeo
cifrado = cifrar_caracteres(Caracteres, Cadena_caracteres, True)
decifrado = cifrar_caracteres(Caracteres, cifrado, False)

print('-- Detalles del algoritmo --\n')
print(f'Entrada: {Cadena_caracteres}\n')
print(f'Cifrado: {cifrado}\n')
print(f'Decifrar: {decifrado}\n')