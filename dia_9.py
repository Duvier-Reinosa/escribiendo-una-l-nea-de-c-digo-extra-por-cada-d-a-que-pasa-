import random
filas = 3
columnas = 3
matriz = [[random.randint(1, 10) for _ in range(columnas)] for _ in range(filas)]
suma = sum(sum(fila) for fila in matriz)
print("Matriz generada:")
for fila in matriz:
    print(fila)
print("Suma de todos los elementos: ", suma)