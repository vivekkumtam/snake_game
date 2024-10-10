import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

WIDTH = 600
HEIGHT = 400

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

x1 = WIDTH / 2
y1 = HEIGHT / 2
x1_change = 0
y1_change = 0
snake_list = []
length_of_snake = 1

foodx = random.randrange(0, WIDTH - snake_block, snake_block)
foody = random.randrange(0, HEIGHT - snake_block, snake_block)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
        running = False

    x1 += x1_change
    y1 += y1_change

    display.fill(BLUE)

    pygame.draw.rect(display, GREEN, [foodx, foody, snake_block, snake_block])

    snake_head = [x1, y1]
    snake_list.append(snake_head)  
    if len(snake_list) > length_of_snake:
        del snake_list[0]  
    
    for segment in snake_list:
        pygame.draw.rect(display, BLACK, [segment[0], segment[1], snake_block, snake_block])

    if snake_head in snake_list[:-1]:
        running = False

    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = random.randrange(0, WIDTH - snake_block, snake_block)
        foody = random.randrange(0, HEIGHT - snake_block, snake_block)
        length_of_snake += 1
    
    clock.tick(snake_speed)

pygame.quit()
