# Variables en Python

# Declaración e inicialización de variables
edad = 48
altura = 1.80
pais = 'España'

# Acceder a las variables
print('Valores iniciales:')
print(f'Edad: {edad}')
print(f'Altura: {altura}')
print(f'Pais: {pais}')

# Modificar el valor de una variable
print('Valores modificados:')
edad = 49
altura = 1.81
print(f'Edad: {edad}')
print(f'Altura: {altura}')

# En Python el tipo es dinamico
edad = 'Cuarentainueve'
print(f'Edad: {edad}')

# Si accedemos a una variable no declarada dará error
print(f'Telefono: {telefono}')
