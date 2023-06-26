# 18. Jugemos al juego de adivinar el numero, generaremos unn numero entre 1 y 100
# Nuestro objetivo es adivinar el numero
# Si fallamos nos dira si es mayor o menor que el numero buscado

from random import * # Importa todas las funciones del módulo "random"

def generar_numero_aleatorio(minimo, maximo):

    try:
        if minimo > maximo: # Comprueba si el valor mínimo es mayor que el valor máximo
    
            aux = minimo  # Comprueba si el valor mínimo es mayor que el valor máximo
    
            minimo = maximo
    
            maximo = aux
    
        return randint(minimo, maximo)  # Genera un número aleatorio entre el mínimo y el máximo
    
    except TypeError: # Captura una excepción de tipo TypeError
    
        print("Debes escribir numeros") # Imprime un mensaje de error
    
        return -1 # Devuelve -1 para indicar un error
    
numero_buscado = generar_numero_aleatorio(1, 100) # Genera un número aleatorio entre 1 y 100 y lo asigna a "numero_buscado"

encontrado = False # Inicializa la variable booleana "encontrado" como False

while not encontrado:  # Mientras "encontrado" sea False:
    numero_usuario = int(input("Dame un numero que quieres buscar: "))  # Lee un número ingresado por el usuario y lo convierte a entero

    if numero_usuario > numero_buscado:

        print("El numero que buscas es menor")
    elif numero_usuario < numero_buscado:

        print("El numero que buscas es mayor")
    else:
        encontrado = True # Cambia el valor de "encontrado" a True para salir del bucle
        print("Has hacertado")
