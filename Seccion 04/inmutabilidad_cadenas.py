# Inmutabilidad de las cadenas
cadena1 = 'Hola Python'
# cadena1[0] = 'h' Arroja un error de Typo, los elementos de una cadena no se pueden modificar
cadena2 = cadena1
cadena1 = 'Adios'
print(cadena1)
print(cadena2)
