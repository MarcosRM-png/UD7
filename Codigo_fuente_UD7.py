# Módulo inicial de procesamiento de ventas

def mostrar_informacion(lista):
    """Une la información de ventas y devoluciones válidas."""
    resultado = []
    resultado += procesar_ventas(lista)
    resultado += procesar_devoluciones(lista)
    return resultado


def procesar_ventas(lista):
    ventas = []

    for registro in lista:
        if registro['tipo'] == 'venta' and registro['monto'] > 0 and registro['estado'] == 'completado':
            if registro['monto'] > 1000 or (registro['cliente_tipo'] == 'VIP' and registro['monto'] > 500):
                monto_final = registro['monto'] * 0.9
            else:
                monto_final = registro['monto']

            texto = "Cliente: " + registro['nombre'] + " - Total: " + str(monto_final)
            ventas.append(texto)

    return ventas


def procesar_devoluciones(lista):
    devoluciones = []

    for registro in lista:
        if registro['tipo'] == 'devolucion' and registro['monto'] > 0:
            monto_final = registro['monto'] * -1
            texto = "Cliente: " + registro['nombre'] + " - Retorno: " + str(monto_final)
            devoluciones.append(texto)

    return devoluciones


# Datos de prueba para verificar que funciona
informacion_venta = [
    {'tipo': 'venta', 'monto': 1200, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Juan'},
    {'tipo': 'venta', 'monto': 600, 'estado': 'completado', 'cliente_tipo': 'VIP', 'nombre': 'Ana'},
    {'tipo': 'devolucion', 'monto': 50, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Pedro'}
]

print(mostrar_informacion(informacion_venta))