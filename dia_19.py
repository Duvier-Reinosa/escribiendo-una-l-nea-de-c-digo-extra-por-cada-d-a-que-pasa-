import time
def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Ingrese un número entero positivo: "))
if n < 0:
    print("El número debe ser positivo.")  
else:
    start_time = time.time() 
    resultado = fibonacci(n)
    end_time = time.time()
    print(f"El número de Fibonacci en la posición {n} es: {resultado}")
    print(f"Tiempo de cálculo: {end_time - start_time:.6f} segundos")
