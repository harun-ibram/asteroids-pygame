import sys, pygame

pygame.init()
screen_size = width, height = (1280, 720)
screen = pygame.display.set_mode(screen_size)
pygame.display
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

speed = [2, 2]

ahri = pygame.image.load("ahri.gif")

IMAGE_SIZE = (123, 96)
ahri = pygame.transform.scale(ahri, IMAGE_SIZE)

ahri_rect = ahri.get_rect()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill("black")
    ahri_rect = ahri_rect.move(speed)

    if(ahri_rect.left < 0 or ahri_rect.right > width):
        speed[0] = -speed[0]
    if(ahri_rect.top <0 or ahri_rect.bottom > height):
        speed[1] = -speed[1]
    # draw player
    # pygame.draw.circle(screen, "white", player_pos, 50)

    # wrap the screen
    #if player_pos.x < 0:
    #    player_pos.x = screen.get_width()
    #if player_pos.x > screen.get_width():
    #    player_pos.x = 0
   # if player_pos.y < 0:
  #      player_pos.y = screen.get_height()
 #   if player_pos.y > screen.get_height():
#        player_pos.y = 0

    #movement
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_w]:
    #    player_pos.y += (-600) * dt
    #if keys[pygame.K_s]:
    #    player_pos.y += 600 * dt
    #if keys[pygame.K_a]:
    #    player_pos.x += (-600) * dt
    #if keys[pygame.K_d]:
    #    player_pos.x += 600 * dt
    

    screen.blit(ahri, ahri_rect)
    pygame.display.flip()

    dt = clock.tick(144) / 1000


pygame.quit()
