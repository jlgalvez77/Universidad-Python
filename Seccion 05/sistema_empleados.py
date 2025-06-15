# Sistema de Empleados

print('*** Sistema de Empleados ***')

nombre_empleado = input('Introduce el nombre del empleado: ')
edad_empleado = int(input('Introduce la edad del empleado: '))
salario_empleado = float(input('Introduce el salario del empleado: '))
es_jefe_departamento = input('¿Es jefe de departamento? (si/no): ')

# Convertir a tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

# Imprimir los valores del Empleado
print('\nDatos del Empleado')
print(f'Nombre del empleado: {nombre_empleado}')
print(f'Edad del empleado: {edad_empleado}')
print(f'Salario del empleado: {salario_empleado:.2f}')
print(f'¿Es Jefe de Departamento?: {es_jefe_departamento}')
