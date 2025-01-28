n = int(input("Ingresa el limite superior: "))
suma_pares = 0
for x in range(1, n + 1):
    if x % 2 == 0: 
        suma_pares += x
        print(f"Sumando {x}, total hasta ahora: {suma_pares}")
print(f"\nLa suma de los números pares hasta {n} es {suma_pares}.")