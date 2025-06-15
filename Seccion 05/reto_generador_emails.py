# Generador de Emails
print('*** Generador de Emails ***')
nombre = input('Introduce tu nombre: ')
apellido = input('Introduce tu apellido: ')
empresa = input('Introduce tu empresa: ')
dominio = input('Introduce la extensión de tu dominio: ')

nombre_formateado = nombre.lower().replace(' ', '.')
apellido_formateado = apellido.lower().replace(' ', '.')
empresa_formateado = empresa.lower()

print(
    f'El email generado es: {nombre_formateado}.{apellido_formateado}@{empresa_formateado}{dominio}')
