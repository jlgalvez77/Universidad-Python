# Generador de Email
nombre = 'Jose Galvez'
empresa = 'Futurmatica'
dominio = '.es'

nombre_normalizado = nombre.lower().strip().replace(' ', '.')

print('*** Generador de Email ***')
print(f'Nombre de usuario: {nombre}')
print(f'Nombre de usuario normalizado: {nombre_normalizado}')
print()
print(f'Nombre empresa: {empresa}')
print(f'Extensión del dominio: {dominio}')

empresa_normalizado = empresa.lower().replace(' ', '')

print(f'Dominio del email normalizado: @{empresa_normalizado}{dominio}')
print()
print(f'Email final generado: {nombre_normalizado}@{empresa_normalizado}{dominio}')
