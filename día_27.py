import pygame, math
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
def draw_cat(surface, x, y):
    pygame.draw.circle(surface, (50, 50, 50), (x, y), 20)  # Cabeza
    pygame.draw.circle(surface, (0, 0, 0), (x - 7, y - 5), 5)  # Ojo izq
    pygame.draw.circle(surface, (0, 0, 0), (x + 7, y - 5), 5)  # Ojo der
    pygame.draw.polygon(surface, (50, 50, 50), [(x - 15, y - 10), (x - 5, y - 25), (x + 5, y - 10)])  # Oreja izq
    pygame.draw.polygon(surface, (50, 50, 50), [(x + 15, y - 10), (x + 5, y - 25), (x - 5, y - 10)])  # Oreja der
angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    center_x, center_y = 200, 200
    x = center_x + math.cos(angle) * 70
    y = center_y + math.sin(angle) * 70
    pygame.draw.aaline(screen, (150, 150, 150), (center_x, center_y), (x, y))  # Línea gris
    draw_cat(screen, int(x), int(y))
    angle += 0.05
    pygame.display.flip()
    clock.tick(60)
pygame.quit()