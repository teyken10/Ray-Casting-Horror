import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  # Выход из игры
        print(event)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255),
                     (20, 20, 100, 75))
