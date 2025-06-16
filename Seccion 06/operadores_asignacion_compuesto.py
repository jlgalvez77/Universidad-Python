# Operadores de Asignación Compuestos
a, b = 10, 15
print(f'Valor inicial a: {a} y b: {b}')

# Operador compuesto de suma +=
a += b  # a = a + b
print(f'Operador a += b: {a}')

# Operador compuesto de resta -=
a = 10  # Reiniciamos la variable a
a -= b
print(f'Operador a -= b: {a}')

# Operador compuesto de multiplicación
a = 10  # Reiniciamos la variable a
a *= b
print(f'Operador a *= b: {a}')

# Operador compuesto de división
a = 10  # Reiniciamos la variable a
a /= b
print(f'Operador a /= b: {a:.2f}')

# Operador compuesto de modulo
a = 10  # Reiniciamos la variable a
a %= b
print(f'Operador a %= b: {a}')
