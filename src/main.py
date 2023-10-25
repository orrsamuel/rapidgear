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

# Load the car image
car_image = pygame.image.load('assets/car.png')
car_image = pygame.transform.scale(car_image, (100, 120))

map_image = pygame.image.load('assets/map.jpeg')


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
    screen.blit(map_image, (0, 0))
    screen.blit(car_image, (x, y)) # Draw car sprite
    
    pygame.display.update()  # Update the screen

# Quit Pygame
pygame.quit()
