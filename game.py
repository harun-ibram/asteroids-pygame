import sys, pygame

pygame.init()
screen_size = width, height = (1280, 720)
screen = pygame.display.set_mode(screen_size)
pygame.display
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill("purple")

    # draw player
    pygame.draw.circle(screen, "white", player_pos, 50)

    # wrap the screen
    if player_pos.x < 0:
        player_pos.x = screen.get_width()
    if player_pos.x > screen.get_width():
        player_pos.x = 0
    if player_pos.y < 0:
        player_pos.y = screen.get_height()
    if player_pos.y > screen.get_height():
        player_pos.y = 0

    #movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y += (-600) * dt
    if keys[pygame.K_s]:
        player_pos.y += 600 * dt
    if keys[pygame.K_a]:
        player_pos.x += (-600) * dt
    if keys[pygame.K_d]:
        player_pos.x += 600 * dt
    


    pygame.display.flip()

    dt = clock.tick(144) / 1000


pygame.quit()
