# Programa de reserva de asientos en una sala de cine
# 0 = asiento libre
# 1 = asiento reservado

# Crear matriz de 3 filas por 4 columnas
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicitar fila y columna del asiento
fila = int(input("Ingrese la fila (0 a 2): "))
columna = int(input("Ingrese la columna (0 a 3): "))

# Reservar asiento
asientos[fila][columna] = 1

# Mostrar estado completo de la sala
print("\nEstado de la sala:")

# Recorrer la matriz con bucles anidados
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()