import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up a mobile-friendly screen resolution
screen = pygame.display.set_mode((720, 1280))
clock = pygame.time.Clock()

# Player settings
player_pos = [360, 640]
player_radius = 40

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Detect finger taps / mouse clicks on screen
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player_pos = list(event.pos) # Move player to tap location

    # Draw everything
    screen.fill((20, 20, 30)) # Dark background
    pygame.draw.circle(screen, (255, 85, 85), player_pos, player_radius) # Red player circle
    
    pygame.display.flip()
    clock.tick(60) # Smooth 60 Frames Per Second
