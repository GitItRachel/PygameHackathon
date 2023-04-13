#import libraries
import pygame
import random
import os


# Constants
WIDTH = 1280
HEIGHT = 800
FPS = 60
SEA_BLUE = (0, 105, 148)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Setup folders for assets
game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, "img")


# Create sprites
class Player(pygame.sprite.Sprite):
    # Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_folder, "fishTile_074.png")).convert()  # image for the sprite
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()      # rectangle that encloses the sprite
        self.rect.center = (int(WIDTH/2), int(HEIGHT/2))  # Set sprite location to center of screen
        self.speedx= 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = 5
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.speedy = -2
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.speedy = 2
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


# Setup pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Always a Bigger Fish")
clock = pygame.time.Clock()
running = True

# Create sprite group
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


while running:
    # Add ability to close game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Draw
    screen.fill(SEA_BLUE)
    all_sprites.draw(screen)

    # Display game
    pygame.display.flip()

    clock.tick(FPS) # 60 fps

pygame.quit()