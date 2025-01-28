import random
grid_size = 5
treasure = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
hunter = (0, 0)
def print_grid():
    for i in range(grid_size):
        for j in range(grid_size):
            if (i, j) == hunter: print("H", end=" ")
            elif (i, j) == treasure: print("T", end=" ")  # Ocultar el tesoro en el juego real
            else: print(".", end=" ")
        print()
def move_hunter(direction):
    global hunter
    x, y = hunter
    if direction == "w" and x > 0: x -= 1
    elif direction == "s" and x < grid_size-1: x += 1
    elif direction == "a" and y > 0: y -= 1
    elif direction == "d" and y < grid_size-1: y += 1
    hunter = (x, y)
while hunter != treasure:
    print_grid()
    move = input("Mueve con WASD: ").lower()
    move_hunter(move)
    if hunter == treasure: print("¡Encontraste el tesoro!")