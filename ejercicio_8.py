# 19. Pintar una escalera con numeros

altura = 5

for fila in range(1, altura + 1):
    for columna in range(1, fila + 1):
        print(columna , end="")
    print()

# 20. Pintar un triangulo con *
altura = 4
asteriscos = 1

for espacios in range(altura, 0, -1):
    for i in range(espacios):
        print("   ", end="")
    for i in range(asteriscos):
        print("*  ", end="")
    print()
    asteriscos += 2