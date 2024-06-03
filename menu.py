import pygame
from colors import Colors
import sys

screen = pygame.display.set_mode((500, 620))

def draw_menu(options, selected_option, start_y):
    menu_font = pygame.font.Font(None, 30)
    for i, option in enumerate(options):
        color = Colors.white
        if i == selected_option:
            color = Colors.red
        surface = menu_font.render(option, True, color)
        screen.blit(surface, (180, start_y + i * 50))
        option_rect = surface.get_rect(topleft=(180, start_y + i * 50))
        if option_rect.collidepoint(pygame.mouse.get_pos()):
            selected_option = i
    return selected_option