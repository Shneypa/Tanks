import pygame
import time
import random

pygame.init()                                           # initialize pygame



# Display variables and display init

white = (255,255,255)                                         # defining Colors
black = (0,0,0)
red = (255,0,0)
blue = (0,0,155)
darkgreen = (0,120,0)
lightgreen = (0,200,0)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

clock = pygame.time.Clock()                              # variable to control FPS
FPS = 15

gameDisplay = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))        # create window

pygame.display.set_caption("Tanks")

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


# icon = pygame.image.load("icon.png")
# pygame.display.set_icon(icon)
# menu_image = pygame.image.load("SnakeMenu.png")

score_player1 = 0
score_player2 = 0

# head_img1 = pygame.image.load('snake_head.png')                # load snake head spirte
# head_img2 = pygame.image.load('snake_head_lightgreen.png')

# apple_img = pygame.image.load('strawberry.png')          # load apple sprite




# Intro Loop

def intro_loop():

    intro = True

    while intro:

        gameDisplay.fill(white)
        # gameDisplay.blit(menu_image, (0,0))

        message_to_screen("Welcome to Tanks", darkgreen, -100, font_size= "large")

        message_to_screen("Player 1 copntrols: W A S D to move, R to fire", black, -30, "small")
        message_to_screen("Player 2 controls: Arrow keys to move, right CTRL to fire", black, 0, "small")
        # message_to_screen("___________________________________", black, 30, "small")
        message_to_screen("Press SPACE to play or Q to quit.", black, 180, "small")
        message_to_screen("Use SPACE to pause game.", black, 210, "small")


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(15)


def text_objects(text, color, font_size):
    if font_size == "small":
        textSurface = smallfont.render(text, True, color)
    elif font_size == "medium":
        textSurface = medfont.render(text, True, color)
    elif font_size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color = black, y_displacement = 0, font_size = "small", x_displacement = 0):                  # discplacement from the center on Y axis

    textSurf, textRect = text_objects(msg, color, font_size)
    textRect.center = (WINDOW_WIDTH /2 + x_displacement), (WINDOW_HEIGHT /2 + y_displacement)
    gameDisplay.blit(textSurf, textRect)



# PAUSE loop

def pause_loop():

    paused = True

    #  gameDisplay.fill(white)
    message_to_screen("Game paused", black, y_displacement = -50, font_size="large")
    message_to_screen("Press SPACE to continue or Q to quit", black, y_displacement=50, font_size="small")
    pygame.display.update()
    clock.tick(5)

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()




# GAME LOOP

def GAME_LOOP():

    global score_player1
    global score_player2

    # Game variables

    gameExit = False
    gameOver = False

        # first tank

    # tank coords
    # turret angle

        # second tank

    # tank coords
    # turret angle



    # GAME LOOP:

    while not gameExit:

    # Play again or quit?

        while gameOver == True:

            gameDisplay.fill(white)
            message_to_screen("Game over",  y_displacement = -100, color = red, font_size = "large")
            message_to_screen("Press SPACE to play again or Q to quit",black, 50, font_size = "small")
            message_to_screen("Player 1 score: " + str(score_player1),black, 150, x_displacement = -250, font_size = "small")
            message_to_screen("Player 2 score: " + str(score_player2),black, 150, x_displacement = 250, font_size = "small")


            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_SPACE:
                        GAME_LOOP()


        # EVENT HANDLING

        for event in pygame.event.get():

            if event.type is pygame.QUIT:
                gameExit = True

            if event.type is pygame.KEYDOWN:

                # Player 1 controls

                if event.key == pygame.K_a:
                    pass
                elif event.key == pygame.K_d:
                    pass
                elif event.key == pygame.K_w:
                    pass
                elif event.key == pygame.K_s:
                    pass
                elif event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                          pause_loop()

                # Player 2 controls

                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass

        # UPDATE AND RENDER

        # updated coordinates for this frame

        #
        #
        #

        gameDisplay.fill(white)                                                 # draws 'in the background'. we clean the screen.

        # drawing stuff
        # gameDisplay.blit(apple_img, (apple_x,apple_y))
        #
        #

        message_to_screen("Player 1 Score: " + str(score_player1), black, y_displacement=270, x_displacement = -270)
        message_to_screen("Player 2 Score: " + str(score_player2), black, y_displacement=270, x_displacement = 270)


        pygame.display.update()                                                 # draws everything to the screen

        clock.tick(FPS)


    # END OF GAME LOOP

    gameDisplay.fill(white)

    pygame.display.update()

    pygame.quit()

    quit()


intro_loop()

GAME_LOOP()







'''
        CODING SEQUENCE - HYPOTHESIS

1. Create window
2. Simple game LOOP  (while loop)
3. Handle QUIT event

4. Draw a rectangle onto a screen (add update() method)
5.
6.

7.
8.
9.
10.
11.
12.
13.
14.
15.




        CODING SEQUENCE - ACTUAL

1. Create window
2. Simple game LOOP  (while loop)
3. Handle QUIT event

4. Draw a rectangle onto a screen (add update() method)
5.
6.

7.
8.
9.
10.
11.
12.
13.
14.
15.


'''