import pygame, sys
from colors import Colors

screen = pygame.display.set_mode((500, 620))
loading = False
loading_start_time = 0

def show_loading_screen(screen):
    loading_background = pygame.Surface((500, 620))
    loading_background.fill(Colors.dark_blue)
    loading_background.set_alpha(200)
    screen.blit(loading_background, (0, 0))
    
    loading_font = pygame.font.Font(None, 50)
    loading_text = loading_font.render("Loading...", True, Colors.white)
    screen.blit(loading_text, (180, 270))
    