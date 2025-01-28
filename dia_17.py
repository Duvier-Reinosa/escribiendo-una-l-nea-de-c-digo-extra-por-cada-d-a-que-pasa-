import pygame
pygame.init()
screen = pygame.display.set_mode((700, 200))
keys = {pygame.K_a: "C", pygame.K_s: "D", pygame.K_d: "E", pygame.K_f: "F", pygame.K_g: "G", pygame.K_h: "A", pygame.K_j: "B"}
sounds = {k: pygame.mixer.Sound(f"{v}.wav") for k, v in keys.items()}
key_positions = list(keys.keys())
key_width = 100
running = True
font = pygame.font.SysFont(None, 40)
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: running = False
        if e.type == pygame.KEYDOWN and e.key in sounds: sounds[e.key].play()
    screen.fill((255, 255, 255))
    for i, key in enumerate(key_positions): (pygame.draw.rect(screen, (200, 200, 200), (i * key_width, 0, key_width, 200)), pygame.draw.rect(screen, (0, 0, 0), (i * key_width, 0, key_width, 200), 2), screen.blit(font.render(keys[key], True, (0, 0, 0)), (i * key_width + key_width // 2 - font.render(keys[key], True, (0, 0, 0)).get_width() // 2, 80)))
    pygame.display.flip()
pygame.quit()