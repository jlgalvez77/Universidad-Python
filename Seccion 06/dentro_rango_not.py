# Revisar si una variable se encuentra dentro de rango entr 1 y 10
dato = int(input('Introduce un número entero: '))

# Revisamos si ests dentro de rango
esta_dentro_rango = 1 <= dato <= 10
print(f'La Variable está dentro de rango (entre 1 y 10)?: {esta_dentro_rango}')

# Revisamos la lógica inversa
esta_dentro_rango = not (1 <= dato <= 10)
print(f'La Variable está fuera de rango (entre 1 y 10)?: {esta_dentro_rango}')
