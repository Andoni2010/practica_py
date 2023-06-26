# 7. Mostrar con un while los numeros del 1 al 100
i = 1

while( i<=100 ):
    print(i)
    i+=1
print("Fin del bucle")
# 8. Mostrar con um for los numeros del 1 al 100
for i in range(1,101):
    print(i)
print("Fin del bucle for")
# 9. Mostrar los caracteres de la cadena "Hola mundo"
for i in "Hola mundo":
    print(i)
# 10. Mostrar los numeros pares entre 1 al 100
for i in range(2,101,2):
    print(i)
print("Fin del bucle de dos en dos")
for i in range(1, 101):
    if((i%2)==0):
        print(i)