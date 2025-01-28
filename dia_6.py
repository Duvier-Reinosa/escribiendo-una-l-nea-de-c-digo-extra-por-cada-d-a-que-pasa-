import random
n = random.randint(1, 10)
for i in range(3):
    if int(input("Adivina el número: ")) == n: print("¡Correcto!"); break
    else : print("¡Incorrecto!")
print(f"El número era {n}.")