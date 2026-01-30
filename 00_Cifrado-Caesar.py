Caracteres = ['A', 'Á', 'a', 'á', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'É', 
              'e', 'é', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'Í', 'i', 'í',
              'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'Ñ', 'ñ',
              'O', 'Ó', 'o', 'ó', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's',
              'T', 't', 'U', 'Ú', 'u', 'ú', 'V', 'v', 'W', 'w', 'X', 'x',
              'Y', 'Ý', 'y', 'ý', 'Z', 'z', ' ']

# Variables para testear
Caracter = 'Z'
Cambio = 7
Direccion = True

def calcular_posicion (caracteres_cp=list, caracter_cp=int, cambio_cp=int, direccion_cp=bool):
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

# Funcion para testear
def posicion (caracteres_p=list, caracter_p=str):
    posicion = caracteres_p.index(caracter_p)
    return posicion

# Funcion para testear
for x in Caracteres:
    caracter_m = Caracteres[calcular_posicion(Caracteres, x, Cambio, True)]
    caracter_n = Caracteres[calcular_posicion(Caracteres, x, Cambio, False)]
    print(f'{x} - {posicion(Caracteres, x)} - {caracter_m} - {calcular_posicion(Caracteres, x, Cambio, True)} - {caracter_n} - {calcular_posicion(Caracteres, x, Cambio, False)}')