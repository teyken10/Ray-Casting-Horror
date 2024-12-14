import pygame

from bin.settings import *
from bin.player import Player
from bin.ray_casting import ray_casting


class Game:
    def run(self):
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        pygame.init()
        sc = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        player = Player()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEMOTION:
                    player.mouse_motion(event.pos)
                else:
                    player.last_mouse_pos_x = (WIDTH // 2, HEIGHT // 2)
            player.movement()
            sc.fill(BLACK)

            pygame.display.set_caption(f'FPS: {math.trunc(clock.get_fps())}')

            pygame.draw.rect(sc, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
            pygame.draw.rect(sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

            ray_casting(sc, player.pos, player.angle)

            # pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
            # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
            #                                          player.y + WIDTH * math.sin(player.angle)))
            # for x, y in world_map:
            #     pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

            pygame.display.flip()
            clock.tick(FPS)

        pygame.mouse.set_visible(True)
        pygame.event.set_grab(False)
