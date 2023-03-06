# File Created By Ross Cassetta

'''

### x ### = outside of loop
# x # = In loop

'''

### LIBRARIES ###
import pygame as pg
import pygame_gui
import os
import random as randint

### ASSET LOCATIONS ###
game_folder = os.path.dirname(__file__)
print(game_folder)

### COLORS ###
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

### TEXT SETTINGS ###
def draw_text(screen, text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

### GAME SETTINGS ###
WIDTH = 1440
HEIGHT = 900
FPS = 30
timer = pg.time.Clock()

### SCREEN ###
pg.init()
pg.mixer.init()
screen = pg.Surface((WIDTH, HEIGHT))
window_surface = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock Paper Sissors")
background = pg.Surface((WIDTH, HEIGHT))
background.fill(pg.Color(BLACK))
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

### MAIN MENU ###
play_button1 = pygame_gui.elements.UIButton(relative_rect=pg.Rect((550,50), (300,200)),
    text='Do You Want To Play A Game?')
play_button2 = pygame_gui.elements.UIButton(relative_rect=pg.Rect((300,350), (300,300)),
    text='Yes')
play_button3 = pygame_gui.elements.UIButton(relative_rect=pg.Rect((800,350), (300,300)),
    text='No')
mouse_coords = pg.mouse.get_pos()

### RESULTS SCREEN ###
show_results_screen = pg.Surface((WIDTH, HEIGHT))
show_results_screen.fill(pg.Color(BLACK))

### IMAGE LOCATIONS ###
rock_image = pg.image.load(os.path.join(game_folder, "rock.jpg")).convert()
rock_rect = rock_image.get_rect()
rock_rect.center = (WIDTH/4, HEIGHT/4)

paper_image = pg.image.load(os.path.join(game_folder, "paper.jpg")).convert()
paper_rect = paper_image.get_rect()
paper_rect.center = (WIDTH/2, HEIGHT/4)

scissors_image = pg.image.load(os.path.join(game_folder, "scissors.jpg")).convert()
scissors_rect = scissors_image.get_rect()
scissors_rect.center = (1200, HEIGHT/4)

### CHOICES ###
user_choice = ["rock,", "paper", "scissors"]
choices = ["rock", "paper", "scissors"]
cpu_choice = randint.choice(choices)

### SET VALUES ###
clicked = 0
running = True
in_game = False
in_menu = True
in_results_screen = False

### GAME LOOP ###
while running:
    timer.tick(FPS)
    # MAIN MENU #
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == play_button1:
                pass
            elif event.ui_element == play_button2:
                in_menu = False
                in_game = True
            elif event.ui_element == play_button3:
                running = False
    # COLIDE POINTS #
    if event.type == pg.MOUSEBUTTONDOWN:
        mouse_coords = pg.mouse.get_pos()
        if rock_rect.collidepoint(pg.mouse.get_pos()) and not clicked == 2:
            print("You clicked on rock!")
            print("The CPU chose:", cpu_choice)
            user_choice = "rock"
            clicked = 1
            in_results_screen = True
        elif paper_rect.collidepoint(pg.mouse.get_pos()) and not clicked == 2:
            print("You clicked on paper!")
            print("The CPU chose:", cpu_choice)
            user_choice = "paper"
            clicked = 1
            in_results_screen = True
            
        elif scissors_rect.collidepoint(pg.mouse.get_pos()) and not clicked == 2:
            print("You clicked on scissors!")
            print("The CPU chose:", cpu_choice)
            user_choice = "scissors"
            clicked = 1
            in_results_screen = True
 
    # RESULTS #
    if clicked == 1:
        if user_choice == cpu_choice:
            draw_text(show_results_screen, "It's a tie!", 80, (WHITE), WIDTH/2, HEIGHT/3)
        elif user_choice == "rock":
            if cpu_choice == "scissors":
                draw_text(show_results_screen, "You win!", 80, (WHITE), WIDTH/2, HEIGHT/3)
            elif cpu_choice == "paper":
                draw_text(show_results_screen, "You lose!", 80, (WHITE), WIDTH/2, HEIGHT/3)
        elif user_choice == "paper":
            if cpu_choice == "rock":
                draw_text(show_results_screen, "You win!", 80, (WHITE), WIDTH/2, HEIGHT/3)
            elif cpu_choice == "scissors":
                draw_text(show_results_screen, "You lose!", 80, (WHITE), WIDTH/2, HEIGHT/3)
        elif user_choice == "scissors":
            if cpu_choice == "paper":
                draw_text(show_results_screen, "You win!", 80, (WHITE), WIDTH/2, HEIGHT/3)
            elif cpu_choice == "rock":
                draw_text(show_results_screen, "You lose!", 80, (WHITE), WIDTH/2, HEIGHT/3)
        clicked = 2

    # DRAW IMAGES
    window_surface.blit(rock_image, rock_rect)
    window_surface.blit(paper_image, paper_rect)
    window_surface.blit(scissors_image, scissors_rect)
    # MENU #
    if in_menu:
        manager.draw_ui(window_surface)
    manager.process_events(event)
    manager.update(FPS)
    window_surface.blit(background, (0, 0))
    if in_menu:
         manager.draw_ui(window_surface)
    # GAME #
    if in_game:
        window_surface.blit(rock_image, rock_rect)
        window_surface.blit(paper_image, paper_rect)
        window_surface.blit(scissors_image, scissors_rect)
    # RESULTS #
    if in_results_screen:
        window_surface.blit(show_results_screen, (0, 0))
    # ATTEMP AT RESTARTING GAME AFTER 5 SECONDS ON RESULT SCREEN (FAILED) #
        # pg.time.delay(5000)
        # in_results_screen = False
        # in_game = False
        # in_menu = True
        # clicked = 0


    pg.display.update()
    pg.display.flip()

pg.quit()
