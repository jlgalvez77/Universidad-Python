# Sistema de Prestamo de Libros

DISTANCIA_PERMITIDA_KM = 3
es_socio = input('¿Eres socio? (si/no)): ').strip().lower()
distancia_a_biblioteca = int(input('¿A cuantos km vives de la biblioteca?: '))

es_elegible_prestamo = es_socio == 'si' or distancia_a_biblioteca <= DISTANCIA_PERMITIDA_KM
print(f'¿Puede tomar prestados libros de la biblioteca? {es_elegible_prestamo}')
