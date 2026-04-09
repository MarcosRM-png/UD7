# Módulo inicial de procesamiento de ventas
def mostrar_informacion(lista):
    # Junta en una sola lista la información de ventas y devoluciones
    informacion_total = procesamiento_venta(lista) + procesamiento_devolucion(lista)
    return informacion_total


def procesamiento_venta(lista):
    # Guarda aquí los textos de las ventas válidas
    resultado = []

    # Recorre todos los registros de la lista
    for venta in lista:
        # Comprueba que sea una venta correcta
        if venta['tipo'] == 'venta' and venta['monto'] > 0 and venta['estado'] == 'completado':
            # Aplica descuento si la venta es alta o si el cliente es VIP
            if venta['monto'] > 1000 or (venta['cliente_tipo'] == 'VIP' and venta['monto'] > 500):
                monto_final = venta['monto'] * 0.9
            else:
                monto_final = venta['monto']

            # Prepara el texto final de la venta
            datos_venta = "Cliente: " + venta['nombre'] + " - Total: " + str(monto_final)
            resultado.append(datos_venta)

    return resultado


def procesamiento_devolucion(lista):
    # Guarda aquí los textos de las devoluciones válidas
    devoluciones = []

    # Recorre todos los registros de la lista
    for devolucion in lista:
        # Comprueba que sea una devolución correcta
        if devolucion['tipo'] == 'devolucion' and devolucion['monto'] > 0:
            # La devolución se muestra como cantidad negativa
            precio_devolver = devolucion['monto'] * -1

            # Prepara el texto final de la devolución
            datos_devolucion = "Cliente: " + devolucion['nombre'] + " - Retorno: " + str(precio_devolver)
            devoluciones.append(datos_devolucion)

    return devoluciones


# Datos de prueba para verificar que funciona
informacion_venta = [
    {'tipo': 'venta', 'monto': 1200, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Juan'},
    {'tipo': 'venta', 'monto': 600, 'estado': 'completado', 'cliente_tipo': 'VIP', 'nombre': 'Ana'},
    {'tipo': 'devolucion', 'monto': 50, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Pedro'}
]

# Muestra el resultado final por pantalla
print(mostrar_informacion(informacion_venta))