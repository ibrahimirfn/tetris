import pygame, sys
from game import *
from colors import Colors

pygame.init()
title_font = pygame.font.Font(None, 40)
menu_option = ["Play", "High Scores", "Quit"]
current_option = 0

def draw_menu(screen, game, current_option):
    menu_background = pygame.Surface((200, 300))
    menu_background.fill(Colors.light_blue)
    menu_background.set_alpha(200)
    screen.blit(menu_background, (150, 150))

    menu_font = pygame.font.Font(None, 30)
    for i, option in enumerate(menu_option):
        color = Colors.white
        if i == current_option:
            color = Colors.red
        surface = menu_font.render(option, True, color)
        screen.blit(surface, (180, 180 + i * 50))

    # Add a title to the menu
    title_surface = title_font.render("Menu", True, Colors.white)
    screen.blit(title_surface, (180, 120))

def handle_menu_events(game, current_option):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if menu_option[current_option] == "Play":
                    game.game_started = True
                    game.reset()
                elif menu_option[current_option] == "High Scores":
                    # Implement high scores functionality
                    pass
                elif menu_option[current_option] == "Quit":
                    pygame.quit()
                    sys.exit()
            if event.key == pygame.K_UP:
                current_option = (current_option - 1) % len(menu_option)
            if event.key == pygame.K_DOWN:
                current_option = (current_option + 1) % len(menu_option)

    return current_option