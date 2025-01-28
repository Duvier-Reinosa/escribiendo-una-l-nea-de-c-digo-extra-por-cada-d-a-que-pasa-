import random
u = input("Piedra, papel o tijera: ").lower()
c = random.choice(["piedra", "papel", "tijera"])
print(f"La computadora eligió {c} y tú elegiste {u}")
if u == c: print("Empate")
elif (u == 'piedra' and c == 'tijera') or (u == 'papel' and c == 'piedra') or (u == 'tijera' and c == 'papel'): 
    print("Ganaste")
else: print("Perdiste")