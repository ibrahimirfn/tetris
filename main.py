import pygame
import sys
from game import Game
from colors import Colors
import highscore
from loading import show_loading_screen

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.red)
menu_surface = title_font.render("Menu", True, Colors.white)
high_score_title_surface = title_font.render("High Score", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
menu_rect = pygame.Rect(320, 450, 170, 60)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

image = pygame.image.load("Images/logo.png")

game = Game()

menu_option = ["Play", "High Scores", "Controls", "Quit"]
difficulty_option = ["Easy", "Medium", "Hard"]
game_over_option = ["Play Again", "Back To Menu", "Quit"]
current_option = 0
difficulty_level = None 

difficulty_speeds = {
    "Easy": 500,
    "Medium": 200,
    "Hard": 100
}

GAME_UPDATE = pygame.USEREVENT

game_started = False
paused = False
in_difficulty_menu = False  
loading = False  
loading_start_time = 0  
in_controls_menu = False  
in_high_scores_menu = False  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if not paused and not loading:
                if game_started and not game.game_over:
                    if event.key == pygame.K_LEFT:
                        game.move_left()
                    if event.key == pygame.K_RIGHT:
                        game.move_right()
                    if event.key == pygame.K_DOWN:
                        game.move_down()
                        game.update_score(0, 1)
                    if event.key == pygame.K_UP:
                        game.rotate()
                elif game_started and game.game_over:
                    if event.key == pygame.K_RETURN:
                        if game_over_option[current_option] == "Play Again":
                            game_started = True
                            game = Game()
                            current_option = 0
                        elif game_over_option[current_option] == "Back To Menu":
                            game_started = False
                            current_option = 0
                        elif game_over_option[current_option] == "High Scores":
                            high_score = highscore.load_high_score()
                            print("High Score:", high_score)
                        elif game_over_option[current_option] == "Quit":
                            pygame.quit()
                            sys.exit()
                    elif event.key == pygame.K_UP:
                        current_option = (current_option - 1) % len(game_over_option)
                    elif event.key == pygame.K_DOWN:
                        current_option = (current_option + 1) % len(game_over_option)
                else:
                    if in_difficulty_menu:
                        if event.key == pygame.K_RETURN:
                            difficulty_level = difficulty_option[current_option]
                            loading = True
                            loading_start_time = pygame.time.get_ticks()
                            current_option = 0
                            in_difficulty_menu = False
                        elif event.key == pygame.K_UP:
                            current_option = (current_option - 1) % len(difficulty_option)
                        elif event.key == pygame.K_DOWN:
                            current_option = (current_option + 1) % len(difficulty_option)
                    elif in_controls_menu or in_high_scores_menu:
                        if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                            in_controls_menu = False
                            in_high_scores_menu = False
                            current_option = 0
                    else:
                        if event.key == pygame.K_RETURN:
                            if menu_option[current_option] == "Play":
                                in_difficulty_menu = True
                                current_option = 0
                            elif menu_option[current_option] == "High Scores":
                                in_high_scores_menu = True
                            elif menu_option[current_option] == "Controls":
                                in_controls_menu = True
                            elif menu_option[current_option] == "Quit":
                                pygame.quit()
                                sys.exit()
                        if event.key == pygame.K_UP:
                            current_option = (current_option - 1) % len(menu_option)
                        if event.key == pygame.K_DOWN:
                            current_option = (current_option + 1) % len(menu_option)

            if event.key == pygame.K_ESCAPE:
                paused = not paused

        if event.type == GAME_UPDATE and game_started and not game.game_over and not paused:
            game.move_down()

    screen.fill(Colors.dark_blue)

    if loading:
        elapsed_time = pygame.time.get_ticks() - loading_start_time
        progress = min(elapsed_time / 3000, 1)
        show_loading_screen(screen, progress)
        if progress >= 1:
            loading = False
            game_started = True
            game.reset()
            game = Game()
            pygame.time.set_timer(GAME_UPDATE, difficulty_speeds[difficulty_level])

    elif not game_started:
        if in_difficulty_menu:
            difficulty_background = pygame.Surface((200, 200))
            difficulty_background.fill(Colors.light_blue)
            difficulty_background.set_alpha(200)
            screen.blit(difficulty_background, (150, 150))

            difficulty_font = pygame.font.Font(None, 30)
            for i, option in enumerate(difficulty_option):
                color = Colors.white
                if i == current_option:
                    color = Colors.red
                surface = difficulty_font.render(option, True, color)
                screen.blit(surface, (180, 180 + i * 50))
        elif in_controls_menu:
            controls_background = pygame.Surface((300, 400))
            controls_background.fill(Colors.light_blue)
            controls_background.set_alpha(200)
            screen.blit(controls_background, (100, 100))

            controls_font = pygame.font.Font(None, 30)
            controls_text = [
                "Controls:",
                "Arrow keys to move",
                "Up arrow to rotate",
                "Esc to pause",
                "",
                "Press Enter to go back"
            ]
            for i, text in enumerate(controls_text):
                surface = controls_font.render(text, True, Colors.white)
                screen.blit(surface, (120, 120 + i * 40))
        elif in_high_scores_menu:
            high_scores_background = pygame.Surface((300, 400))
            high_scores_background.fill(Colors.light_blue)
            high_scores_background.set_alpha(200)
            screen.blit(high_scores_background, (100, 100))

            high_scores_font = pygame.font.Font(None, 30)
            high_scores_text = ["High Scores:"]

            high_scores = highscore.load_high_scores()
            for i, score in enumerate(high_scores):
                high_scores_text.append(f"{score}")

            high_scores_text.append("")
            high_scores_text.append("Press Enter to go back")

            for i, text in enumerate(high_scores_text):
                surface = high_scores_font.render(text, True, Colors.white)
                screen.blit(surface, (120, 120 + i * 40))
        else:
            menu_background = pygame.Surface((200, 300))
            menu_background.fill(Colors.light_blue)
            menu_background.set_alpha(200)
            screen.blit(menu_background, (150, 150))
            screen.blit(image, (65, 16))

            menu_font = pygame.font.Font(None, 30)
            for i, option in enumerate(menu_option):
                color = Colors.white
                if i == current_option:
                    color = Colors.red
                surface = menu_font.render(option, True, color)
                screen.blit(surface, (180, 180 + i * 50))

    else:
        if not game.game_over:
            screen.blit(score_surface, (365, 20, 50, 50))
            screen.blit(next_surface, (375, 180, 50, 50))

            score_value_surface = title_font.render(str(game.score), True, Colors.white)
            screen.blit(score_value_surface, (430, 70, 50, 50))
            pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
            screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
            pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
            game.draw(screen)

            high_score = highscore.load_high_score()
            high_score_surface = font.render("High Score: " + str(high_score), True, Colors.white)
            screen.blit(high_score_surface, (315, 500, 50, 50))

        else:
            if game.score > highscore.load_high_score():
                highscore.save_high_score(game.score)
            game_over_background = pygame.Surface((300, 160))
            game_over_background.fill(Colors.dark_red)
            game_over_background.set_alpha(100)
            screen.blit(game_over_background, (100, 200))

            game_over_font = pygame.font.Font(None, 40)
            game_over_text = game_over_font.render("GAME OVER", True, Colors.white)
            screen.blit(game_over_text, (150, 220))

            score_value_surface = title_font.render("Score: " + str(game.score), True, Colors.white)
            screen.blit(score_value_surface, (150, 280))

            high_score = highscore.load_high_score()
            high_score_surface = title_font.render("High Score: " + str(high_score), True, Colors.white)
            screen.blit(high_score_surface, (150, 320))

            for i, option in enumerate(game_over_option):
                color = Colors.white
                if i == current_option:
                    color = Colors.red
                surface = game_over_font.render(option, True, color)
                screen.blit(surface, (150, 380 + i * 50))

    if paused:
        pause_surface = title_font.render("Paused", True, Colors.white)
        screen.blit(pause_surface, (200, 270))

    pygame.display.update()
    clock.tick(60)
