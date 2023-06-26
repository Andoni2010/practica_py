## Estructuras condicionales ##

# 4. De dos numeros, saber cual es el mayor
a = 6
b = 5

if(a <= b): 
    print(a, "es menor o igual que", b)
else:
    print(a, "es mayor o igual que", b)
# 5. Crea una variable numerica y si esta entre 0 y 10, mostrar un mensaje indicandolo
a = 1

if(a>=1 and a<=10):
    print("Estas entre 1 y 10")
else:
    print("No esta en ese rango")
# 6. Añadir al anterior ejercicio, que si esta entre 11 y 20,
# muestre otro mensaje diferente y si esta entre 21 y 30 otro mensaje.
a = 44

if(a>=1 and a<=10):
    print("Estas entre 1 y 10")

elif(a>=11 and a<=20):
    print("Estas entre 11 y 20")
elif(a>=21 and a<=30):
    print("Estas entre 21 y 30")
else:
    print("No esta en ningun rango")