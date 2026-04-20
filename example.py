import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PYgame")

potato_img = pygame.image.load("potato.png").convert()
potato_img.set_colorkey((0, 0, 0))

x, y = WIDTH // 2, HEIGHT // 2
clock = pygame.time.Clock()

Speed = 1
nspeed = 1
GS = 90
running = True

health = 100
speed_timer = 0
cat_timer = 0

enemies = []
MAX_ENEMIES = 20

# Cat variables
cat_active = False
ex, ey = 0, 0

while running:
    current_time = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()

    # --- SPAWN CAT (1 in 1000 chance) ---
    if len(enemies) < MAX_ENEMIES and random.randint(1, 1000) == 1:
        print("yo")
        side = random.choice(["top", "bottom", "left", "right"])

        if side == "top":
            ex, ey = random.randint(0, WIDTH), 0
        elif side == "bottom":
            ex, ey = random.randint(0, WIDTH), HEIGHT
        elif side == "left":
            ex, ey = 0, random.randint(0, HEIGHT)
        else:
            ex, ey = WIDTH, random.randint(0, HEIGHT)

        enemies.append([ex, ey])
    # --- MOVE CAT TOWARD PLAYER ---
    for enemy in enemies:
        ex, ey = enemy

        # Move toward player
        if ex < x:
            ex += 0.5
        elif ex > x:
            ex -= 0.5

        if ey < y:
            ey += 0.5
        elif ey > y:
            ey -= 0.5

        # SAVE BACK (this is what you were missing)
        enemy[0] = ex
        enemy[1] = ey

        # Draw AFTER updating
        screen.blit(potato_img, (ex, ey))

        # Collision
        if abs(ex - x) < 5 and abs(ey - y) < 5:
            health -= 20
            print("Health:", health)

            enemies.remove(enemy)

            if health <= 0:
                running = False

    # --- PLAYER MOVEMENT ---
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

    # --- EVENTS ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Speed = 3
                speed_timer = current_time + 3000

    # --- TIMERS ---
    if speed_timer and current_time >= speed_timer:
        Speed = nspeed
        speed_timer = 0

    # --- DRAW ---
    screen.fill((30, 30, 30))

    # player
    screen.blit(potato_img, (x, y))

    # enemies
    for ex, ey in enemies:
        screen.blit(potato_img, (ex, ey))

    pygame.display.flip()
    clock.tick(GS)
