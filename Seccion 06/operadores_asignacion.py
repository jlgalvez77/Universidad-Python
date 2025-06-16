# Operadores de asignación
numero = 6
print(f'Resultado de numero: {numero}')
numero = 10
print(f'Resultado de numero: {numero}')
cadena = 'Saludos desde Python'
print(f'Resultado de cadena: {cadena}')

# Asignación multiple
x, y, z = 5, 'Hola', -9.57
print(f'Valor de x = {x}, Valor de y = {y}, Valor de z = {z}')

# Asignación encadenada
a = b = c = 10
print(f'Resultado de a = {a}, b = {b}, c = {c}')

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'Valores iniciales de x = {x}, y = {y}')
# Aplicando el concepto de asignacióm multiple, intercambiamos valores
x, y = y, x
print(f'Valores invertidos x = {x}, y = {y}')

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input('Introduce tu nombre y apellido separados por una coma: ').split(',')
print(f'Resultado de nombre = {nombre} y apellido = {apellido}')
