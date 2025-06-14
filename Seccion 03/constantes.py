import math

print('*** Constantes ***')

PI = 3.14159
print(f'PI: {PI}')

NOMBRE_BASE_DATOS = 'clientes_db'
print(f'Nombre de la base de datos: {NOMBRE_BASE_DATOS}')

# Esto NO se debe hacer, no se debe modificar el valor de una constante
NOMBRE_BASE = 'base_db'
print(f'No cambiar el valor de una constate: {NOMBRE_BASE}')

# Usar una constante del lenguaje Python, aunque en este caso no está en mayusculas
print(f'Valor de math.pi: {math.pi}')
