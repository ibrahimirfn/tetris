# loading.py

import pygame
from colors import Colors

def show_loading_screen(screen, progress):
    loading_background = pygame.Surface((500, 620))
    loading_background.fill(Colors.dark_blue)
    loading_background.set_alpha(200)
    screen.blit(loading_background, (0, 0))
    
    loading_font = pygame.font.Font(None, 50)
    loading_text = loading_font.render("Loading...", True, Colors.white)
    screen.blit(loading_text, (165, 270))
    
    bar_background = pygame.Rect(150, 350, 200, 30)
    pygame.draw.rect(screen, Colors.light_blue, bar_background)

    bar_progress = pygame.Rect(150, 350, 200 * progress, 30)
    pygame.draw.rect(screen, Colors.green, bar_progress)
