# Sistema de descuentos VIP

NRO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input('¿Cuantos productos compraste hoy?: '))
es_socio = input('¿Eres socio de la tienda (Si/No)?: ').strip().lower()

es_elegible_descuento = cantidad_productos >= NRO_PRODUCTOS_DESCUENTO and es_socio == 'si'

print(f'¿Tienes acceso al descuento VIP? {es_elegible_descuento}')
