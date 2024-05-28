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

font = pygame.font.SysFont("arialblack", 36)

clock = pygame.time.Clock()

image = pygame.image.load("Images/logo.png")

game = Game()

menu_option = ["Play", "High Scores", "Controls", "Quit"]
difficulty_option = ["Easy", "Medium", "Hard"]
game_over_option = ["Play Again", "Back To Menu", "Quit"]
current_option = 0
difficulty_level = None  # Add a variable to store the difficulty level

# Define game speeds for different difficulty levels
difficulty_speeds = {
    "Easy": 500,
    "Medium": 200,
    "Hard": 100
}

GAME_UPDATE = pygame.USEREVENT

game_started = False
paused = False
in_difficulty_menu = False  # Add a variable to track if we're in the difficulty menu
loading = False  # Add a variable to track if we're in the loading screen
loading_start_time = 0  # Add a variable to track the start time of the loading screen
in_controls_menu = False  # Add a variable to track if we're in the controls menu
in_high_scores_menu = False  # Add a variable to track if we're in the high scores menu

while True:
    for event in pygame.event.get():
        # Exit from bar
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Menu
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
                            game = Game()  # Restart game instance
                            current_option = 0  # Reset current_option
                        elif game_over_option[current_option] == "Back To Menu":
                            game_started = False  # Kembali ke menu utama
                            current_option = 0  # Reset current_option
                        elif game_over_option[current_option] == "High Scores":
                            high_score = highscore.load_high_score()
                            print("High Score:", high_score)
                        elif game_over_option[current_option] == "Quit":
                            pygame.quit()
                            sys.exit()
                    if event.key == pygame.K_UP:
                        current_option = (current_option - 1) % len(game_over_option)
                    if event.key == pygame.K_DOWN:
                        current_option = (current_option + 1) % len(game_over_option)
                else:
                    if in_difficulty_menu:
                        if event.key == pygame.K_RETURN:
                            difficulty_level = difficulty_option[current_option]
                            loading = True
                            loading_start_time = pygame.time.get_ticks()  # Set the start time for the loading screen
                            current_option = 0  # Reset current_option
                            in_difficulty_menu = False
                        if event.key == pygame.K_UP:
                            current_option = (current_option - 1) % len(difficulty_option)
                        if event.key == pygame.K_DOWN:
                            current_option = (current_option + 1) % len(difficulty_option)
                    elif in_controls_menu or in_high_scores_menu:
                        if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                            in_controls_menu = False
                            in_high_scores_menu = False
                            current_option = 0  # Reset current_option
                    else:
                        if event.key == pygame.K_RETURN:
                            if menu_option[current_option] == "Play":
                                in_difficulty_menu = True
                                current_option = 0  # Reset current_option
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

            # Pause game saat tombol Esc ditekan
            if event.key == pygame.K_ESCAPE:
                paused = not paused

        if event.type == GAME_UPDATE and game_started and not game.game_over and not paused:
            game.move_down()

    screen.fill(Colors.dark_blue)

    if loading:
        show_loading_screen(screen)
        if pygame.time.get_ticks() - loading_start_time > 3000:  # Loading screen for 3 seconds
            loading = False
            game_started = True
            game.reset()
            game = Game()
            pygame.time.set_timer(GAME_UPDATE, difficulty_speeds[difficulty_level])

    elif not game_started:
        if in_difficulty_menu:
            # Difficulty menu background
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
            # Controls menu background
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
            # High Scores menu background
            high_scores_background = pygame.Surface((300, 400))
            high_scores_background.fill(Colors.light_blue)
            high_scores_background.set_alpha(200)
            screen.blit(high_scores_background, (100, 100))

            high_scores_font = pygame.font.Font(None, 30)
            high_scores_text = ["High Scores:"]

            # Load high scores
            high_scores = highscore.load_high_scores()  # Assuming this function returns a list of high scores
            for i, score in enumerate(high_scores):
                high_scores_text.append(f"{score}")  # Remove the numbering here


            high_scores_text.append("")
            high_scores_text.append("Press Enter to go back")

            for i, text in enumerate(high_scores_text):
                surface = high_scores_font.render(text, True, Colors.white)
                screen.blit(surface, (120, 120 + i * 40))
        else:
            # Menu background
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
            screen.blit(menu_surface, (375, 515, 50, 50))

            score_value_surface = title_font.render(str(game.score), True, Colors.white)
            screen.blit(score_value_surface, (430, 70, 50, 50))
            pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
            screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
            pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
            game.draw(screen)

            # Menampilkan high score saat permainan dimulai
            high_score = highscore.load_high_score()
            high_score_surface = title_font.render("High Score: " + str(high_score), True, Colors.white)
            screen.blit(high_score_surface, (10, 10))

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
                screen.blit(surface, (170, 380 + i * 50))

    # Tampilkan layar pause saat permainan di-pause
    if paused:
        pause_surface = title_font.render("Paused", True, Colors.white)
        screen.blit(pause_surface, (200, 250))

    pygame.display.update()
    clock.tick(60)
