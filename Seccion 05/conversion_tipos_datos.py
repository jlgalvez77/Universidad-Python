# Conversión de tipos de datos

# Convertir de cadena a número
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'El número cadena es: {numero_cadena}')
print(f'El número entero es: {numero_entero}')

# Convertir de cadena a número flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'El número cadena es: {numero_cadena}')
print(f'El número flotante es: {numero_flotante}')

# Convertir número a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Número entero: {numero_entero}')
print(f'Número cadena: {numero_cadena}')

# Convertir a Booleano
# Tipo bool es False en los siguientes casos: Si el valor es 0, cadena vacia o None, devuelve False
# Devuelve verdadero, si el valor es distinto de 0, cadena vacia o None
numero_entero = 0
booleano = bool(numero_entero)
print(f'Valor booleano de 0: {booleano}')

numero_entero = 5
booleano = bool(numero_entero)
print(f'Valor booleano de 5: {booleano}')

cadena = ''
booleano = bool(cadena)
print(f'Valor booleano de cadena vacía: {booleano}')

cadena = 'Cadena con valor'
booleano = bool(cadena)
print(f'Valor booleano de cadena NO vacia: {booleano}')

variable = None
booleano = bool(variable)
print(f'Valor booleano de None: {booleano}')
