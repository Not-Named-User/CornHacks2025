"""
Level 1 Scene,
at this point I am just trying to setup the screen 
to have collison detection with a controllable object

Status: Not finished
"""
import sys
import os
import pygame

# Set the working directory
print("Current Working Dir:", os.getcwd() )
# Screen Setup
HEIGHT = 720
WIDTH = 1280

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Super Loud")
# Load in background
backgroud = pygame.image.load("../../assets/images/testScene.png")
# Scale to fit the screen
#backgroud = pygame.transform.scale(backgroud, (WIDTH, HEIGHT))

clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Game Looop
while running:

    #pygame.QUIT event means that the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("white")

    # Set background
    screen.blit(backgroud, (0, 0))

    # Draw the character
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
