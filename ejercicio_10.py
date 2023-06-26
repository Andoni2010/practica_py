# 24. Escribe un programa que dibuje una peine de tamaño N. El tamaño debe ser un valor positivo impar. Características del peine:
"""
 - Debe tener una altura de N filas.
 - Todas las filas deben tener una anchura también de N.
 - Todas las filas impares deben usar el carácter = y al final mostrar el número de la fila. El número de la fila que aparece en el dibujo debe tener sólo un dígito, en cuanto supera el valor de 9 se iniciará nuevamente por 1.
 - Las filas pares deben usar el carácter blanco y al final el carácter +
 - Una vez finalizado el gráfico debe mostrarse en pantalla el número de caracteres que se han usado para hacer el gráfico, concretamente el número de caracteres diferentes a blanco que se han usado para hacer el dibujo.

Nota: Al inicio hay que hacer la comprobación en la entrada de datos, asegurando que el número es positivo y impar. El programa insistirá hasta obtener el número con estas propiedades.

Ejemplo si escribimos 9:

========1
        +
========3
        +
========5
        +
========7
        +
========9
"""
valid = False
while not valid:
    num = int(input("Introduce un numero positivo e impar: "))  # Solicita al usuario que ingrese un número positivo e impar
    if num > 0 and num % 2 != 0:  # Comprueba si el número es positivo e impar
        valid = True  # Establece valid en True para salir del bucle

numCharacters = 0  # Inicializa el contador de caracteres en 0
numberShow = 1  # Inicializa el número a mostrar en 1
i = 1  # Inicializa el contador del bucle externo en 1
while i <= num:
    if i % 2 == 1:  # Si i es impar
        j = 1  # Inicializa el contador del bucle interno en 1
        while j < num:
            print("=", end="")  # Imprime el carácter "=" sin salto de línea
            j = j + 1  # Incrementa j en 1
        print(numberShow)  # Imprime el número a mostrar en la línea actual
        if numberShow + 2 > 10:
            numberShow = 1  # Si numberShow + 2 supera 10, reinicia en 1
        else:
            numberShow = numberShow + 2  # Incrementa el número a mostrar en 2
        numCharacters = numCharacters + num  # Incrementa el contador de caracteres por el valor de num
    else:
        j = 1  # Inicializa el contador del bucle interno en 1
        while j < num:
            print(" ", end="")  # Imprime un espacio en blanco sin salto de línea
            j = j + 1  # Incrementa j en 1
        print("+")  # Imprime el carácter "+" en la línea actual
        numCharacters = numCharacters + 1  # Incrementa el contador de caracteres en 1
    i = i + 1  # Incrementa i en 1

print("El numero diferente a espacios en blanco es de: ", numCharacters)  # Imprime el número total de caracteres diferentes a espacios en blanco
