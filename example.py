import pygame
import sys

pygame.init()

WIDTH = 640
HEIGHT = 640

# Create display FIRST
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PYgame")

# NOW it's safe to convert
potato_img = pygame.image.load("potato.png").convert()

x = WIDTH/2
y = HEIGHT/2
ex = 640
ey = 640
fullscreen = False
clock = pygame.time.Clock()

nspeed = 1
Speed = 1
GS = 90
running = True
speed_timer = 0
cat_timer = 0
health = 100
cat = True

while running:

    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()

    if ey == y:
        pass
    elif ey - y > 0:
        ey -= 0.5
    elif ey - y < 0:
        ey += 0.5

    if ex == x:
        pass
    elif ex - x > 0:
        ex -= 0.5
    elif ex - x < 0:
        ex += 0.5

    if ex == x and ey == y:
        if cat:
            health -= 20
            cat = False
            print(health)
            cat_timer = current_time + 3000 
            if health == 0:
                running = False
    # Move first
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        y -= Speed

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        y += Speed

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
      x += Speed

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
      x -= Speed

    x = max(0, min(x, WIDTH - potato_img.get_width()))
    y = max(0, min(y, HEIGHT - potato_img.get_height()))
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    Speed = 5
                    speed_timer = current_time + 3000 

    if speed_timer != 0 and current_time >= speed_timer:
        Speed = nspeed
        speed_timer = 0 
    
    if cat_timer != 0 and current_time >= cat_timer:
        cat = True
        cat_timer = 0

    screen.fill((30, 30, 30))

    screen.blit(potato_img, (x, y))
    screen.blit(potato_img, (ex, ey))

    pygame.display.flip()
    clock.tick(GS)
                   