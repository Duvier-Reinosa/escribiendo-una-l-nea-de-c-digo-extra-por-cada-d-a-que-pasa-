import time 
def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci de forma iterativa."""
    if n <= 0:
        return 0
    elif n == 1:  
        return 1
    else:
        a, b = 0, 1 
        for _ in range(2, n + 1):
            a, b = b, a + b 
        return b
n = int(input("Ingrese un número entero positivo: "))
if n < 0:
    print("El número debe ser positivo.") 
else:
    start_time = time.time()
    resultado = fibonacci(n)
    end_time = time.time()
    print(f"El número de Fibonacci en la posición {n} es: {resultado} \n Tiempo de cálculo: {end_time - start_time:.6f} segundos")