# Módulo inicial de procesamiento de ventas

def mostrar_informacion(lista):
    """Recorre la lista y devuelve el resumen de ventas y devoluciones."""
    resultado = []

    for registro in lista:
        if registro['tipo'] == 'venta' and registro['monto'] > 0 and registro['estado'] == 'completado':
            if registro['monto'] > 1000 or (registro['cliente_tipo'] == 'VIP' and registro['monto'] > 500):
                monto_final = registro['monto'] * 0.9
            else:
                monto_final = registro['monto']

            texto = "Cliente: " + registro['nombre'] + " - Total: " + str(monto_final)
            resultado.append(texto)

            print("Procesando registro de: " + registro['nombre'])

        elif registro['tipo'] == 'devolucion' and registro['monto'] > 0:
            monto_final = registro['monto'] * -1
            texto = "Cliente: " + registro['nombre'] + " - Retorno: " + str(monto_final)
            resultado.append(texto)

            print("Procesando registro de: " + registro['nombre'])

    return resultado


# Datos de prueba para verificar que funciona
informacion_venta = [
    {'tipo': 'venta', 'monto': 1200, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Juan'},
    {'tipo': 'venta', 'monto': 600, 'estado': 'completado', 'cliente_tipo': 'VIP', 'nombre': 'Ana'},
    {'tipo': 'devolucion', 'monto': 50, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Pedro'}
]

print(mostrar_informacion(informacion_venta))