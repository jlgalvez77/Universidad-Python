from random import randint

# Generador de ID

print('*** Generador de ID ***')
nombre = input('Introduce tu nombre: ')
apellido = input('Introduce tu apellido: ')
nacimiento = input('Introdce tu año de nacimiento (YYYY):')
numero_aleatorio = randint(0, 9999)

letras_nombre = nombre[0:2].upper()
letras_apellido = apellido[0:2].upper()
numero_nacimiento = nacimiento[-2:]

print(f'Resultado ID Único: {letras_nombre}{letras_apellido}{numero_nacimiento}{numero_aleatorio}')
