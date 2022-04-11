import pygame
import random
import os

pygame.init()

x, y = 1280, 720
screen = pygame.display.set_mode((x, y))
"""
sets up the screen size
"""

turtle = pygame.image.load(os.getcwd() + r"/turtle.png")
cherry = pygame.image.load(os.getcwd() + "/cherry.png")
"""
imports images
"""


pos = [x//2, y//2]
"""
places turtle at the center
"""

score = 0
font = pygame.font.SysFont("Comic Sans MS", 30)
"""
sets up the score text
"""

speed = 5
"""
makes faster
"""

pygame.draw.line(screen, (128, 128, 128), (0, 35), (x, 35), 72)
pygame.display.flip()
"""
sets up the border between playable area and scoreboard
"""

pos_fruit = [random.randint(0, x-68), random.randint(75, y-52)]
"""
places fruit at random spot
"""

while True:
    if abs(pos[0]-pos_fruit[0]) < 35 and abs(pos[1]-pos_fruit[1]) < 35:
        pygame.draw.line(screen, (128, 128, 128), (0, 35), (x, 35), 72)
        pygame.display.flip()
        score += 1
        pos_fruit = [random.randint(0, x - 68), random.randint(75, y - 52)]
    """
    if the turtle is next to the fruit, increments the score and places fruit at random spot
    """

    text = font.render("Score: " + str(score), False, (255, 255, 255))
    screen.blit(text, (x//2, 20))
    pygame.display.flip()
    screen.fill((196, 196, 196), (0, 72, x, y-72))
    """
    updates the scoreboard and shades in dark gray
    """

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and pos[1] - speed >= 75:
        pos[1] -= speed
    elif key[pygame.K_s] and pos[1] + speed < y-52:
        pos[1] += speed
    elif key[pygame.K_a] and pos[0] > 1:
        pos[0] -= speed
    elif key[pygame.K_d] and pos[0] < x-68:
        pos[0] += speed
    elif key[pygame.K_q] and speed > 1:
        speed -= 1
    elif key[pygame.K_e] and speed < 25:
        speed += 1
    """
    checks for wasd
    """

    screen.blit(pygame.transform.scale(cherry, (68, 52)), (pos_fruit[0], pos_fruit[1]))
    screen.blit(pygame.transform.scale(turtle, (68, 52)), (pos[0], pos[1]))
    pygame.display.flip()
    pygame.event.pump()
    """
    draws the turtle and fruit
    """
