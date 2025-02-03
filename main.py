import pygame
from bin.main_menu import MainMenu
from bin.resource_manager import ResourceManager

pygame.init()
# screen = pygame.display.set_mode((300, 300))
# screen.fill((0, 0, 0))

# font = pygame.font.Font(None, 48)
# text_surface = font.render("Загрузка...", True, (255, 255, 255))
# screen.blit(text_surface, (300 // 2 - text_surface.get_width() // 2, 300 // 2 - text_surface.get_height() // 2))

# pygame.display.flip()

resources = ResourceManager()
main_menu = MainMenu(resources)
main_menu.run()
