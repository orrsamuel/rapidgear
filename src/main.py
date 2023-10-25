import pygame

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((800, 600))

# Initialize variables
x = 400  # Initial x-coordinate of the car (rectangle)
y = 500  # Initial y-coordinate of the car (rectangle)
width = 50  # Width of the car (rectangle)
height = 60  # Height of the car (rectangle)
velocity = 5  # How many pixels the car will move per frame

# Initialize clock for controlling FPS
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity

    # Drawing
    screen.fill((0, 0, 0))  # Fill the screen with black
    pygame.draw.rect(screen, (0, 128, 255), (x, y, width, height))  # Draw the car (rectangle)
    pygame.display.update()  # Update the screen

# Quit Pygame
pygame.quit()
