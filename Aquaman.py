import pygame
import time
from random import randint, randrange
pygame.init()

surfaceWidth = 1000
surfaceHeight = 650
surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption('Aquaman')
clock = pygame.time.Clock()
img = pygame.image.load('MAN.png')
bg = pygame.image.load('WATER.jpg')
black = (0, 0, 0)
white = (255, 255, 255)
sunset = (253, 72, 47)
greenyellow = (184, 255, 0)
brightblue = (47, 228, 253)
orange = (255, 113, 0)
yellow = (255, 236, 0)
purple = (252, 67, 255)
colorChoices = [black, orange, yellow, sunset, purple]

imageHeight = 40
imageWidth = 84

def food(food_x, food_y, food_w, food_h, color):
    pygame.draw.rect(surface, color, [food_x, food_y, food_w, food_h])

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score: " + str(count), True, black)
    surface.blit(text, [5, 5])

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            continue

        return event.key

    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, sunset)
    return textSurface, textSurface.get_rect()

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 80)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    main()

def gameOver():
    msgSurface('Game Over!')

def man(x, y, image):
    surface.blit(img, (x, y))

def main():
    #position of the man
    x = 80
    y = 200
    y_move = 0
    x_move = 0
    #positioning the food particle
    x_block = 950
    y_block = randint(20, surfaceHeight - 20)

    food_width = 35
    food_height = 35
    food_speed = 5
    current_score = 0
    foodColor = colorChoices[randrange(0, len(colorChoices))]
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -3

                if event.key == pygame.K_DOWN:
                    y_move = 3

                if event.key == pygame.K_LEFT:
                    x_move = -3

                if event.key == pygame.K_RIGHT:
                    x_move = 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0

        y += y_move
        x += x_move
        surface.blit(bg, [0, 0])
        #surface.fill(brightblue)
        food(x_block, y_block, food_width, food_height, foodColor)
        man(x, y, img)
        score(current_score)
        x_block -= food_speed
        temp = 0

        #boundary
        if y > surfaceHeight - imageHeight or y < 0:
            gameOver()

        if x > surfaceWidth - imageWidth - 50 or x < 0:
            gameOver()

        if x_block <= 0: #60 + 90:
            x_block = 0 + surfaceWidth
            y_block = randint(20, surfaceHeight - 30)
            foodColor = colorChoices[randrange(0, len(colorChoices))]
            current_score += 1


        #conditions for collision
        if x + imageWidth + 20 > x_block + food_width:
            foodColor = brightblue


        #increasing level difficulty
        if 3 <= current_score < 5:
            food_speed = 6
        if 6 <= current_score < 10:
            food_speed = 7
        if 11 <= current_score <15:
            food_speed = 8
        pygame.display.update()
        clock.tick(60)
main()
pygame.quit()
quit()
