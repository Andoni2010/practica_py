## Range ##

# 11. Generar un rango entre 0 y 10
rango = list( range(11) )
print(rango)
# 12. Generar un rango entre 5 y 10
rango = list( range(5, 11) )
print(rango)
# 13. Generar un rango de 10 a 0
rango = list( range(10,-1,-1) )
print(rango)
# 14. Generar un rango de 0 a 10 y de 15 a 20, incluidos el 10 y 20
rango_uno = list( range(11) )
rango_dos = list( range(15, 21))
final = rango_uno + rango_dos
print(final)
# 15. Generar un rango desde 0 hasta la longitud de la cadena "Hola mundo"
rango = list( range(0, len("Hola mundo")) )
print(rango)