import pygame
from pygame.locals import *
import random

size = width, height = (400, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1

pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption('car game')
screen.fill((60, 220, 0))


#apply changes
pygame.display.update()

#load player images
car = pygame.image.load('green-car.png')
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8

#load enemy images
car2 = pygame.image.load('red-car.png')
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2
counter = 0

#game loop
def update_game_state():
    global speed
    global counter
    counter += 1
    if counter == 5000:
        speed += 0.15
        counter = 0 
    return speed, counter
    print("LEVEL UP", speed)

def check_collision():
    return car_loc.colliderect(car2_loc)

while running:
    update_game_state()


    car2_loc[1] += speed
    if car2_loc[1] > height:
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200



    #end game
    if check_collision():
        print("GAME OVER! YOU LOST!")
        break
    #event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])
    #draw graphics
    pygame.draw.rect(
       screen,
     (50, 50, 50),
     (width/2-road_w/2, 0, road_w, height))

    pygame.draw.rect(
      screen,
     (255, 240, 60),
     (width/2 - roadmark_w/2, 0, roadmark_w, height))

    pygame.draw.rect(
      screen,
     (255, 255, 255),
     (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))

    pygame.draw.rect(
      screen,
      (255, 255, 255),
      (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))


    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()


pygame.quit()

