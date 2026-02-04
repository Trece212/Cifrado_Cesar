Caracteres = [
    ".", ":", ",", ";", "¿", "?", "¡", "!", "'", "@", 
    "#", "$", "%", "^", "(", ")", "-", "-", "=", "+",
    "/", "|", "<", ">", "{", "}", "[", "]", "~", "`",
    "º", " ",
    "A", "Á", "a", "á", "B", "b", "C", "c", "D", "d",
    "E", "É", "e", "é", "F", "f", "G", "g", "H", "h",
    "I", "Í", "i", "í", "J", "j", "K", "k", "L", "l",
    "M", "m", "N", "n", "Ñ", "ñ", "O", "Ó", "o", "ó",
    "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t",
    "U", "Ú", "u", "ú", "V", "v", "W", "w", "X", "x",
    "Y", "Ý", "y", "ý", "Z", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ]

# Variables para testeo
Cambio = 7

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

def cifrar_caracteres (caracteres_cc=list, cadena_caracteres=str, cifrar=bool):
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

run = True
while run == True:
    print('-- OPCIONES --\n')
    print('- Cifrar = 1\n- Decifrar = 2\n- Salir = 0\n')

    opciones = input(': ')
    
    match opciones:
        case '1':
            Cadena_entrada = str(input('\n- Entrada: '))
            Desplasamiento = int(input('- Desplasamiento: '))
            Cambio = Desplasamiento
            Cadena_salida = cifrar_caracteres(Caracteres, Cadena_entrada, True)
            print(f'\n- Salida: {Cadena_salida}\n')
        case '2':
            Cadena_entrada = str(input('\n- Entrada: '))
            Desplasamiento = int(input('- Desplasamiento: '))
            Cambio = Desplasamiento
            Cadena_salida = cifrar_caracteres(Caracteres, Cadena_entrada, False)
            print(f'- Salida: {Cadena_salida}\n')
        case '0':
            print('\n¡ALGORITMO TERMINADO!')
            run = False
        case _:
            print('\n¡OPCION NO RECONOCIDA!\n')