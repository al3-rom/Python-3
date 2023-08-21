# Hay una lista de ventas de los ultimos 30 dias. Queremos analizar las ventas por dia de la semana para identificar los dias de mayor venta

ventas = [120,25,11,134,234,134,125,521,522,932,145,254,342,134,324,154,643,253,267,356,322,643,321,111,39,653,233,133,333,375]

dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# lista para guardar las ventas por dia
ventas_totales = [0, 0, 0, 0, 0, 0, 0]

# recorrer la lista de ventas con un bucle
dia_venta = 0


for venta in ventas:
    # sumar para cada dia de la semana las ventas realizadas
    ventas_totales[dia_venta] = ventas_totales[dia_venta] + venta
    # pasamos al dia siguiente 
    dia_venta += 1
    ## si llegamos al domigno volvemos de nuevo al lunes
    if dia_venta == 7:
        # cambiamos el valor al indice del lunes
        dia_venta = 0
    
for i in range(len(dias_semana)):
    print(dias_semana[i] + ":", ventas_totales[i])

    