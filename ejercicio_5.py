## Tocando cadenas ##

# 16. Pide dos cadenas por teclado, muestra ambas cadeanas con espacio entre ellas 
# y con los primeros caracteres intercambiados. Por ejemplo, 
# hola mundo pasaria a mula hondo
cadena_una = input("Dame la primera cadena: ")
cadena_segunda = input("Dame la segunda cadena: ")

print( cadena_segunda[:2] + cadena_una[2:] + " " + cadena_una[:2] + cadena_segunda[2:])
# 17. Pide una cadena e indica si es uun palindromo o no.
# Palindromo es que se lee de la misma manera de izq a der que de der a izq
cadena_una = input("Dame una cadena: ")
cadena_al_reves = cadena_una[::-1]

if( cadena_una == cadena_al_reves ):
    print("Es un palindormo")
else:
    print("No es palindromo")