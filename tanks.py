import pygame
import time
import random
import math

pygame.init()                                           # initialize pygame


cannon_sound = pygame.mixer.Sound('cannon_shot.wav')
explosion_sound = pygame.mixer.Sound('explosion.wav')

# Display variables and display init

white = (255,255,255)                                         # defining Colors
black = (0,0,0)

lightred = (255,0,0)
darkred = (180,0,0)

lightblue = (0,155,255)
darkblue = (0,0,180)

lightgreen = (0,255,0)
darkgreen = (0,180,0)

lightyellow = (255,255,0)
darkyellow = (180,180,0)


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

ground_height = 40

clock = pygame.time.Clock()                              # variable to control FPS
FPS = 30


tank_width = 50
tank_height = 12
wheel_radius = 5
gunX = 20
gunY = -20
gun_length = 20

guntipX = 0
guntipY = 0

power1 = 10


tank2_width = 50
tank2_height = 12
wheel2_radius = 5
gunX2 = 20
gunY2 = -20
gun2_length = 20


guntip2X = 0
guntip2Y = 0

power2 = 10

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

def barrier():
    bar_x = WINDOW_WIDTH/2 + random.randrange(-0.2 * WINDOW_WIDTH, 0.2 * WINDOW_WIDTH)
    bar_h = random.randrange(WINDOW_HEIGHT * 0.1 , WINDOW_HEIGHT * 0.7)
    bar_y = WINDOW_HEIGHT - bar_h - ground_height
    bar_w = random.randrange(20, 100)
    return bar_x, bar_y, bar_w, bar_h

# barrier
bar_x, bar_y, bar_w, bar_h = barrier()

def tank2(x,y):
    pygame.draw.rect(gameDisplay, darkgreen, (x,y, tank_width,tank_height))
    pygame.draw.circle(gameDisplay, darkgreen, (int(x + tank_width/2), y), int(tank_width/4) ,int(tank_width/4))
    for w in range(8):
        pygame.draw.circle(gameDisplay, darkgreen, (x + w * 6  + wheel_radius - 1, y + tank_height + wheel_radius - 2), wheel_radius, wheel_radius)

def gun2(angle, x, y ):
    gunXoffset = int(math.cos(angle) * gun_length)
    gunYoffset = int(-math.sin(angle) * gun_length)
    guntip2X =  int(x + tank_width/2) + gunXoffset
    guntip2Y = int(y + gunYoffset)
    pygame.draw.line(gameDisplay, darkgreen, (int(x + tank_width/2), y), (guntipX, guntipY),5)
    return angle, guntipX, guntipY



def tank(x,y):
    pygame.draw.rect(gameDisplay, darkgreen, (x,y, tank_width,tank_height))
    pygame.draw.circle(gameDisplay, darkgreen, (int(x + tank_width/2), y), int(tank_width/4) ,int(tank_width/4))
    for w in range(8):
        pygame.draw.circle(gameDisplay, darkgreen, (x + w * 6  + wheel_radius - 1, y + tank_height + wheel_radius - 2), wheel_radius, wheel_radius)

def gun(angle, x, y ):
    gunXoffset = int(math.cos(angle) * gun_length)
    gunYoffset = int(-math.sin(angle) * gun_length)
    guntipX =  int(x + tank_width/2) + gunXoffset
    guntipY = int(y + gunYoffset)
    pygame.draw.line(gameDisplay, darkgreen, (int(x + tank_width/2), y), (guntipX, guntipY),5)
    return angle, guntipX, guntipY

def fire(angle, x,y, tank2X,tank2Y, tank2_width, tank2_height):

   pygame.mixer.Sound.play(cannon_sound)

   fire = True

   shell_above_barrier = False

   y_acceleration = 0
   bullet_speed = power1

   damage = 0



   while fire :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        pygame.draw.rect(gameDisplay, darkred, (x,y,5,5))

        x_change = bullet_speed * math.cos(angle)
        y_change = bullet_speed * math.sin(angle)

        y_acceleration += 0.2

        x += int(x_change)
        y -= int(y_change - y_acceleration)

        # shell out of bounds by X
        if x > WINDOW_WIDTH or x < 0 :

            fire = False

        # shell hits floor
        if y > WINDOW_HEIGHT - ground_height :
            impact_y = WINDOW_HEIGHT - ground_height
            impact_x = int(((WINDOW_HEIGHT - ground_height) * x ) / y)

            #print("Last x, y : ", x ,y)
            # print("Impact at ", impact_x,impact_y)

            explosion(impact_x, impact_y)

            # did we hit enemy tank?
            if tank2X + (tank2_width/2) - 10 <= impact_x <= tank2X + (tank2_width/2) + 10:
                print("Critical hit! ")
                damage = 25
            # did we hit enemy tank?
            elif tank2X + (tank2_width/2) - 15 <= impact_x <= tank2X + (tank2_width/2) + 15:
                print("Hard hit! ")
                damage = 18
            # did we hit enemy tank?
            elif tank2X + (tank2_width/2) - 20 <= impact_x <= tank2X + (tank2_width/2) + 20:
                print("Medium hit! ")
                damage = 10
            # did we hit enemy tank?
            elif tank2X + (tank2_width/2) - 25 <= impact_x <= tank2X + (tank2_width/2) + 25:
                print("Light hit! ")
                damage = 5

            fire = False



        # shell enters airspace above barrier

        if x > bar_x and x < bar_x + bar_w and y < bar_y:

            shell_above_barrier = True

        if x > bar_x + bar_w:
            shell_above_barrier= False

        # shell hits barrier from left side
        if shell_above_barrier == False:


            if x > bar_x and x < bar_x + bar_w :
                if y > bar_y and y < bar_y + bar_h :

                    impact_x = int(bar_x)
                    impact_y = int(y * bar_x / x)

                    #print("Barrier hit from left side! Last x, y : ", x,y)
                    #print("Impact with barrier at ", impact_x,impact_y)

                    explosion(impact_x,impact_y)

                    fire = False
        else:

                 if x > bar_x and x < bar_x + bar_w :
                    if y > bar_y and y < bar_y + bar_h :

                        impact_y = int(bar_y)
                        impact_x  = int(x * bar_y / y )
                        explosion(impact_x, impact_y)

                        fire = False


        pygame.display.update()
        clock.tick(100)

   return damage


def enemy_fire(angle, start_x,start_y, tankX, tankY, tank_width, tank_height):



   # Fire simulations to determine by brute force which power value allows enemy tank to hit player tank. Shots aren't rendered.

   current_power = 5
   target_acquired = False
   out_of_bounds = False

   shell_above_barrier = False

   damage = 0

   y_acceleration = 0



   while not target_acquired and not out_of_bounds :

      fire = True

      current_power += 1
      bullet_speed = current_power

      y_acceleration = 0

      x = start_x
      y = start_y

      while fire :

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()



            # pygame.draw.rect(gameDisplay, darkred, (x,y,5,5))   - simulated shot, dont need to render it

            x_change = - bullet_speed * math.cos(angle)
            y_change = bullet_speed * math.sin(angle)

            y_acceleration += 0.2

            x = int(x + x_change)
            y = int(y - (y_change - y_acceleration))

            # print(x_change, int(x + x_change), y_change, int(y - (y_change - y_acceleration)))

            # shell out of bounds by X
            if x > WINDOW_WIDTH or x < 0 :
                print("out of bounds")
                out_of_bounds = True
                fire = False

            # shell hits floor
            if y > WINDOW_HEIGHT - ground_height :
                impact_y = WINDOW_HEIGHT - ground_height
                impact_x = int(((WINDOW_HEIGHT - ground_height) * x ) / y)
                # print("Floor hit at :" ,x,y)
                #explosion(impact_x, impact_y)

                 # shell hits player tank:
                if x >= tankX and x <= tankX + tank_width:
                    print('Target acquired, power = ', current_power)
                    target_acquired = True


                fire = False


            # shell enters airspace above barrier

            if x > bar_x and x < bar_x + bar_w and y < bar_y:

                shell_above_barrier = True

            if x > bar_x + bar_w:
                shell_above_barrier= False

            # shell hits barrier from left side
            if shell_above_barrier == False:


                if x > bar_x and x < bar_x + bar_w :
                    if y > bar_y and y < bar_y + bar_h :

                        impact_x = int(bar_x)
                        impact_y = int(y * bar_x / x)

                        #print("Barrier hit from left side! Last x, y : ", x,y)
                        #print("Impact with barrier at ", impact_x,impact_y)

                        # explosion(impact_x,impact_y)

                        fire = False
            else:

                     if x > bar_x and x < bar_x + bar_w :
                        if y > bar_y and y < bar_y + bar_h :

                            impact_y = int(bar_y)
                            impact_x  = int(x * bar_y / y )
                            # explosion(impact_x, impact_y)

                            fire = False


            pygame.display.update()
            # clock.tick(100)



   # Real shot with appropriate power value to hit the player

   if not out_of_bounds:
      pygame.mixer.Sound.play(cannon_sound)

   # add randomness to the shot
   current_power = current_power + random.randrange(-2,2)
   print(current_power)

   fire = True

   shell_above_barrier = False

   y_acceleration = 0
   bullet_speed = current_power

   x = start_x
   y = start_y



   while fire and not out_of_bounds:

        # print("Real shot, power = ", current_power)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        pygame.draw.rect(gameDisplay, darkred, (x,y,5,5))

        x_change =  - bullet_speed * math.cos(angle)
        y_change = bullet_speed * math.sin(angle)

        y_acceleration += 0.2

        x = int(x + x_change)
        y = int(y - (y_change - y_acceleration))

        # shell out of bounds by X
        if x > WINDOW_WIDTH or x < 0 :
            out_of_bounds = True
            fire = False

        # shell hits floor
        if y > WINDOW_HEIGHT - ground_height :
            impact_y = WINDOW_HEIGHT - ground_height
            impact_x = int(((WINDOW_HEIGHT - ground_height) * x ) / y)

            #print("Last x, y : ", x ,y)
            # print("Impact at ", impact_x,impact_y)

            # hits player's tank
            if (tankX + tank_width/2) - 10  <= impact_x <= tankX + tank_width/2 + 10 :
                print("Critical hit ! ")
                damage = 25
            elif (tankX + tank_width/2) - 15  <= impact_x <= tankX + tank_width/2 + 15 :
                print("Hard hit ! ")
                damage = 18
            elif (tankX + tank_width/2) - 20  <= impact_x <= tankX + tank_width/2 + 20 :
                print("Medium hit ! ")
                damage = 12
            elif(tankX + tank_width/2) - 25  <= impact_x <= tankX + tank_width/2 + 25 :
                print("Light hit ! ")
                damage = 5

            explosion(impact_x, impact_y)

            fire = False


        # shell enters airspace above barrier

        if x > bar_x and x < bar_x + bar_w and y < bar_y:

            shell_above_barrier = True

        if x > bar_x + bar_w:
            shell_above_barrier= False

        # shell hits barrier from left side
        if shell_above_barrier == False:


            if x > bar_x and x < bar_x + bar_w :
                if y > bar_y and y < bar_y + bar_h :

                    impact_x = int(bar_x)
                    impact_y = int(y * bar_x / x)

                    #print("Barrier hit from left side! Last x, y : ", x,y)
                    #print("Impact with barrier at ", impact_x,impact_y)

                    explosion(impact_x,impact_y)

                    fire = False
        else:

                 if x > bar_x and x < bar_x + bar_w :
                    if y > bar_y and y < bar_y + bar_h :

                        impact_y = int(bar_y)
                        impact_x  = int(x * bar_y / y )
                        explosion(impact_x, impact_y)

                        fire = False


        pygame.display.update()
        clock.tick(100)

   return damage



def explosion(x,y, explosion_size = 50):

    exploding = True

    pygame.mixer.Sound.play(explosion_sound)

    while exploding:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        color_choices = [darkred, lightred, darkyellow]

        magnitude = 1
        while magnitude < explosion_size:

            exploding_bit_x = x + random.randrange(-1* magnitude, magnitude)
            exploding_bit_y = y + random.randrange(-1* magnitude, magnitude)
            pygame.draw.circle(gameDisplay, color_choices[random.randrange(0,3)],(exploding_bit_x,exploding_bit_y),random.randrange(1,5))
            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        exploding = False


def draw_barrier(bar_x, bar_y, bar_w, bar_h):
    pygame.draw.rect(gameDisplay, black, (bar_x, bar_y, bar_w, bar_h))


def draw_button(passive_color, active_color, x, y, width, height, text = "", text_color = black, action = None):

    # get mouse position  (cursor[0] is x coord,  cursor[1] is y coord)
    cursor = pygame.mouse.get_pos()

    # if mouse is within button area, change button color:
    if cursor[0] >= x and cursor[0] <= x + width  and cursor[1] >= y and cursor[1] <= y + height:

        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))

        # if mouse is clicked, perform action specified
        click = pygame.mouse.get_pressed()

        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "controls":
                controls()
            if action == "main_menu":
                intro_loop()
            if action == "play":
                GAME_LOOP()

    else:
        pygame.draw.rect(gameDisplay, passive_color, (x, y, width, height))

    text_to_button(text, text_color, x, y, width, height)



# Controls screen Loop

def controls():

    controls_screen = True

    while controls_screen:

        gameDisplay.fill(white)

        message_to_screen("Player 1 controls: ", y_displacement= -240, font_size="medium")
        message_to_screen("A, D to move tank, ", y_displacement= -180)
        message_to_screen("W, S to aim turret, ", y_displacement= -150)
        message_to_screen("R, F to change bullet power", y_displacement= -120)
        message_to_screen("T to fire", y_displacement= -90)

        message_to_screen("Player 2 controls: ", y_displacement = -30, font_size="medium")
        message_to_screen("Left and Right to move tank, ", y_displacement = 30)
        message_to_screen("Up and Down to aim turret, ", y_displacement = 60)
        message_to_screen("Right CTRL to fire", y_displacement=90)

        message_to_screen("Press SPACE to pause game", y_displacement = 250)

        # buttons
        draw_button( darkgreen, lightgreen, 150,450, 100, 50, "Play", action = "play")
        draw_button( darkyellow, lightyellow, 330, 450, 150, 50, "Main menu", action = "main_menu")
        draw_button( darkred, lightred, 550,450, 100, 50, "Quit",action = "quit")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    controls_screen = False

        pygame.display.update()

        clock.tick(FPS)


# Intro Loop

def intro_loop():

    intro = True

    while intro:

        gameDisplay.fill(white)
        # gameDisplay.blit(menu_image, (0,0))

        message_to_screen("Welcome to Tanks", darkgreen, -100, font_size= "large")

        message_to_screen("Player 1 controls: W A S D to move, R to fire", black, -30, "small")
        message_to_screen("Player 2 controls: Arrow keys to move, right CTRL to fire", black, 0, "small")
        # message_to_screen("___________________________________", black, 30, "small")
        message_to_screen("Press SPACE to play or Q to quit.", black, 180, "small")
        message_to_screen("Use SPACE to pause game.", black, 210, "small")



        # buttons
        draw_button( darkgreen, lightgreen, 150,400, 100, 50, "Play", action = "play")
        draw_button( darkyellow, lightyellow, 350, 400, 100, 50, "Controls",action = "controls")
        draw_button( darkred, lightred, 550,400, 100, 50, "Quit",action = "quit")


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
        clock.tick(FPS)


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



def message_at_coordinates(msg, color = black, font_size = "small", x_coord = WINDOW_WIDTH/2, y_coord = WINDOW_HEIGHT/2):                  # discplacement from the center on Y axis

    textSurf, textRect = text_objects(msg, color, font_size)
    textRect = (x_coord, y_coord)
    gameDisplay.blit(textSurf, textRect)

def text_to_button(msg, color, button_x, button_y, button_width, button_height, font_size = "small"):

    textSurf, textRect = text_objects(msg, color, font_size)
    textRect.center = (button_x + button_width / 2), (button_y + button_height / 2)
    gameDisplay.blit(textSurf, textRect)



def health_bars(player_health, enemy_health):

    if player_health > 75 :
        player_health_color = darkgreen
    elif player_health > 50:
        player_health_color = darkyellow
    else: player_health_color = darkred

    if enemy_health > 75 :
        enemy_health_color = darkgreen
    elif enemy_health > 50:
        enemy_health_color = darkyellow
    else: enemy_health_color = darkred

    pygame.draw.rect(gameDisplay, player_health_color, (50,5,player_health,25))
    pygame.draw.rect(gameDisplay, enemy_health_color, (650,5,enemy_health,25))

# PAUSE loop

def pause_loop():

    paused = True

    #  gameDisplay.fill(white)
    message_to_screen("Game paused", black, y_displacement = -50, font_size="large")
    message_to_screen("Press SPACE to continue or Q to quit", black, y_displacement=50, font_size="small")
    pygame.display.update()
    clock.tick(FPS)

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


def game_over_loop():

    game_over = True

    while game_over:

        gameDisplay.fill(white)


        message_to_screen("Game Over", darkgreen, -100, font_size= "large")

        message_to_screen("You're screwed!", black, -30, "small")

        # buttons
        draw_button( darkgreen, lightgreen, 150,400, 150, 50, "Play again", action = "play")
        draw_button( darkyellow, lightyellow, 350, 400, 100, 50, "Controls",action = "controls")
        draw_button( darkred, lightred, 550,400, 100, 50, "Quit",action = "quit")


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
        clock.tick(FPS)

def you_win_loop():

    win = True

    while win:

        gameDisplay.fill(white)


        message_to_screen("You won!", darkgreen, -100, font_size= "large")

        message_to_screen("Gratz!", black, -30, "small")

        # buttons
        draw_button( darkgreen, lightgreen, 150,400, 150, 50, "Play again", action = "play")
        draw_button( darkyellow, lightyellow, 375, 400, 100, 50, "Controls",action = "controls")
        draw_button( darkred, lightred, 550,400, 100, 50, "Quit",action = "quit")


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
        clock.tick(FPS)



# GAME LOOP

def GAME_LOOP():

    global score_player1
    global gun_angle
    global guntipX
    global guntipY
    global power1

    global gun_angle
    global guntipX
    global guntipY
    global power2
    global score_player2

    # Game variables

    gameExit = False
    gameOver = False

    player_health = 100
    enemy_health = 100

        # first tank

    tankX = int(WINDOW_WIDTH * ( 0.2))
    tankY = int(WINDOW_HEIGHT * ( 0.9))
    tank_move = 0
    gun_angle = 0.4
    gun_move = 0.0
    direction = "right"

    bullet = 0
    bulletX = 0
    power1_change = 0


        # second tank

    tank2X = int(WINDOW_WIDTH * ( 0.8))
    tank2Y = int(WINDOW_HEIGHT * ( 0.9))
    tank2_move = 0
    gun2_angle = 1.4
    gun2_move = 0.0
    direction2 = "left"

    bullet2 = 0
    bullet2X = 0
    power2_change = 0





    # GAME LOOP:

    while not gameExit:



    # Play again or quit?

        while gameOver == True:


            message_to_screen("Game over",  y_displacement = -100, color = darkred, font_size = "large")
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
                    tank_move = -5
                    if direction == "right":
                        gun_angle = 3.14 - gun_angle
                    direction = "left"


                elif event.key == pygame.K_d:
                    tank_move = 5
                    if direction == "left":
                        gun_angle = 3.14 - gun_angle
                    direction = "right"

                elif event.key == pygame.K_w:
                    if direction == "right":
                        gun_move = 0.1

                    else:
                        gun_move = -0.1
                elif event.key == pygame.K_s:
                   if direction == "right":
                        gun_move = -0.1
                   else:
                        gun_move = 0.1

                elif event.key == pygame.K_t:

                   damage = fire(ga,gx,gy, tank2X, tank2Y, tank2_width, tank2_height)
                   enemy_health -= damage

                   score_player1 += damage * 10

                   if enemy_health <= 0:
                      you_win_loop()

                   clock.tick(5)

                   possible_movement = ['f','r']
                   move_index = random.randrange(0,2)

                   for x in range(random.randrange(3,20)):

                       if  tank2X < WINDOW_WIDTH * 0.95:
                           if possible_movement[move_index] == "f":
                               tank2X -= 5
                           elif possible_movement[move_index] =='r':
                               tank2X += 5
                       else :

                           tank2X -= 10


                       # drawing stuff
                       gameDisplay.fill(white)
                       health_bars(player_health, enemy_health)

                       draw_barrier(bar_x, bar_y, bar_w, bar_h)
                       gameDisplay.fill(darkgreen, (0, WINDOW_HEIGHT - ground_height, WINDOW_WIDTH, ground_height))

                       tank(tankX, tankY)
                       ga, gx,gy = gun(gun_angle, tankX, tankY)

                       tank2(tank2X, tank2Y)
                       ga2, gx2,gy2 = gun(gun2_angle, tank2X, tank2Y)

                       message_to_screen("Player 1 Score: " + str(score_player1), black, y_displacement=280, x_displacement = -270)
                       message_to_screen("Player 2 Score: " + str(score_player2), black, y_displacement=280, x_displacement = 270)
                       message_to_screen("Power:  " + str(power1),black, y_displacement=-250, x_displacement = -310, font_size = "small")
                       message_to_screen("Angle:  " + str(int(gun_angle * 57.2958)),black, y_displacement=-220, x_displacement = -310, font_size = "small")

                       pygame.display.update()

                       clock.tick(FPS)






                   damage = enemy_fire(ga2,gx2,gy2, tankX, tankY, tank_width, tank_height)
                   player_health -= damage

                   score_player2 += damage * 10

                   if player_health <= 0:
                      game_over_loop()


                elif event.key == pygame.K_r:

                   power1_change = 1

                elif event.key == pygame.K_f:

                   power1_change -= 1


                elif event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                          pause_loop()



                # Player 2 controls
                '''
                if event.key == pygame.K_LEFT:
                    tank2_move = -5
                    if direction2 == "right":
                        gun2_angle = 3.14 - gun2_angle
                    direction2 = "left"


                elif event.key == pygame.K_RIGHT:
                    tank2_move = 5
                    if direction2 == "right":
                        gun2_angle = 3.14 - gun2_angle
                    direction2 = "left"

                elif event.key == pygame.K_UP:
                    if direction2 == "left":
                        gun_move2 = 0.1

                    else:
                        gun_move2 = -0.1
                elif event.key == pygame.K_DOWN:
                   if direction2 == "left":
                        gun_move2 = -0.1
                   else:
                        gun_move2 = 0.1

                elif event.key == pygame.K_p:

                    fire(ga2,gx2,gy2, "enemy")

                elif event.key == pygame.K_o:

                   power1_change = 1

                elif event.key == pygame.K_l:

                   power1_change -= 1
                '''


            # Keyups for both players
            elif event.type is pygame.KEYUP:

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    tank_move = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    gun_move = 0
                elif event.key == pygame.K_r or event.key == pygame.K_f:
                    power1_change = 0

                '''
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tank2_move = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    gun2_move = 0
                elif event.key == pygame.K_o or event.key == pygame.K_l:
                    power2_change = 0

                '''

        # UPDATE AND RENDER


        # drawing stuff
        gameDisplay.fill(white)
        health_bars(player_health, enemy_health)


        draw_barrier(bar_x, bar_y, bar_w, bar_h)
        gameDisplay.fill(darkgreen, (0, WINDOW_HEIGHT - ground_height, WINDOW_WIDTH, ground_height))

        tank(tankX, tankY)
        ga, gx,gy = gun(gun_angle, tankX, tankY)

        tank2(tank2X, tank2Y)
        ga2, gx2,gy2 = gun(gun2_angle, tank2X, tank2Y)

        message_to_screen("Player 1 Score: " + str(score_player1), black, y_displacement=280, x_displacement = -270)
        message_to_screen("Player 2 Score: " + str(score_player2), black, y_displacement=280, x_displacement = 270)
        message_to_screen("Power:  " + str(power1),black, y_displacement=-250, x_displacement = -310, font_size = "small")
        message_to_screen("Angle:  " + str(int(gun_angle * 57.2958)),black, y_displacement=-220, x_displacement = -310, font_size = "small")

        #  tank collides with barrier
        if tankX + tank_width > bar_x :
            tankX -= 5

        if tankX <= 0:
            tankX += 5

        tankX += tank_move
        gun_angle += gun_move





        # gun angle limitations
        if direction == "right":
            if gun_angle > 1.57:
                gun_angle = 1.57
        if direction == "left":
            if gun_angle < 1.57:
                gun_angle = 1.57

        if gun_angle < 0.0:
            gun_angle = 0.0
        if gun_angle > 3.14:
            gun_angle = 3.14




        power1 += power1_change

        if power1 > 30:
           power1 = 30


        if power1 < 2:
           power1 = 2


        ## tank2

        #  tank collides with barrier
        if tank2X <= bar_x + bar_w:
            tank2X += 5

        if tank2X <= 0:
            tank2X += 5

        tank2X += tank2_move
        gun2_angle += gun2_move



        # gun2 angle limitations
        '''
        if direction2 == "left":
            if gun2_angle < 1.57:
                gun2_angle = 1.57
        if direction2 == "right":
            if gun2_angle > 1.57:
                gun2_angle = 1.57

        if gun2_angle < 0.0:
            gun2_angle = 0.0
        if gun2_angle > 3.14:
            gun2_angle = 3.14
        '''


        power2 += power2_change

        if power2 > 30:
           power2 = 30


        if power2 < 2:
           power2 = 2




        pygame.display.update()                                                 # draws everything to the screen

        clock.tick(FPS)


    # END OF GAME LOOP

    gameDisplay.fill(white)

    pygame.display.update()

    pygame.quit()

    quit()


intro_loop()

GAME_LOOP()


