import pygame
import random
import sys
import math
from pygame.locals import *

pygame.init()
pygame.display.set_caption("We have a party")
screen = pygame.display.set_mode((850, 550))

partygirl1 = pygame.Surface((850, 550)).convert_alpha()
partygirl2 = pygame.Surface((850, 550)).convert_alpha()
partyboy = pygame.Surface((850, 550)).convert_alpha()

musicnota = pygame.Surface((850, 550)).convert_alpha()
musicnota.fill((0, 0, 0, 0))

updatedLights = pygame.Surface((850, 550)).convert_alpha()


updatedLights.fill((255, 0, 0, 0))
partygirl1.fill((255, 0, 0, 0))
partygirl2.fill((0, 0, 0, 0))
partyboy.fill((0, 0, 0, 0))
screen.fill((0, 0, 0, 0))
musicnota.fill((0, 0, 0, 0))

background = pygame.surface.Surface((850, 550))

background.fill((0, 0, 0))

background_colour = (255, 255, 255)
(width, height) = (850, 550)

#background
pygame.draw.polygon(
    background, (148, 123, 90), ((0, 550), (50, 320), (800, 320), (850, 550)))
pygame.draw.polygon(background, (139, 89, 49), ((
    0, 0), (50, 0), (50, 320), (0, 550)))
#leftcorner
pygame.draw.polygon(background, (139, 89, 49), ((
    850, 0), (800, 0), (800, 320), (850, 550)))
#rightcorner
pygame.draw.polygon(background, (102, 68, 34), ((
    50, 0), (800, 0), (800, 320), (50, 320)))
#partygirl1
#head
pygame.draw.circle(partygirl1, (244, 164, 96), (155, 243), 40)
#neck
pygame.draw.line(partygirl1, (0, 0, 0), (155, 282), (155, 350), 10)
#skirt
pygame.draw.polygon(partygirl1, (238, 18, 137), ((
    145, 350), (70, 400), (240, 400), (165, 350)))
#leftleg
pygame.draw.line(partygirl1, (0, 0, 0), (145, 400), (145, 470), 10)
#rightleg
pygame.draw.line(partygirl1, (0, 0, 0), (165, 400), (165, 470), 10)
#kurdela
pygame.draw.polygon(partygirl1, (0, 197, 205), ((
    95, 168), (95, 228), (215, 168), (215, 228)))
#eyes
pygame.draw.circle(partygirl1, (255, 255, 255), (140, 235), 7)
pygame.draw.circle(partygirl1, (255, 255, 255), (170, 235), 7)

pygame.draw.circle(partygirl1, (160, 82, 45), (140, 235), 4)
pygame.draw.circle(partygirl1, (160, 82, 45), (170, 235), 4)

#leftarm
pygame.draw.line(partygirl1, (0, 0, 0), (155, 300), (95, 330), 10)
#lip
pygame.draw.polygon(
    partygirl1, (205, 0, 0), ((135, 258), (160, 268), (175, 258)))

#eyebrown
pygame.draw.line(partygirl1, (0, 0, 0), (123, 218), (133, 230), 3)
pygame.draw.line(partygirl1, (0, 0, 0), (135, 215), (135, 228), 3)
pygame.draw.line(partygirl1, (0, 0, 0), (145, 215), (140, 228), 3)
#eyebrown
pygame.draw.line(partygirl1, (0, 0, 0), (156, 218), (166, 230), 3)
pygame.draw.line(partygirl1, (0, 0, 0), (168, 215), (168, 228), 3)
pygame.draw.line(partygirl1, (0, 0, 0), (178, 215), (173, 228), 3)
#partyboy
#head
pygame.draw.circle(partyboy, (244, 164, 96), (400, 243), 40)
#neck
pygame.draw.line(partyboy, (0, 0, 0), (400, 283), (400, 360), 10)
#papyon
pygame.draw.polygon(
    partyboy, (93, 71, 139), ((375, 280), (375, 300), (425, 280), (425, 300)))
#lip
pygame.draw.line(partyboy, (0, 0, 0), (380, 260), (420, 260), 4)
#leftarm
pygame.draw.line(partyboy, (0, 0, 0), (400, 300), (340, 330), 10)
#trousers
pygame.draw.polygon(
    partyboy, (0, 104, 139), ((400, 360), (380, 360), (360, 430), (390, 430)))
pygame.draw.polygon(
    partyboy, (0, 104, 139), ((420, 360), (400, 360), (410, 430), (440, 430)))
#legs
pygame.draw.line(partyboy, (0, 0, 0), (380, 430), (380, 480), 10)
pygame.draw.line(partyboy, (0, 0, 0), (420, 430), (420, 480), 10)
#glasses
pygame.draw.circle(partyboy, (0, 0, 0), (385, 235), 10)
pygame.draw.circle(partyboy, (0, 0, 0), (415, 235), 10)
pygame.draw.line(partyboy, (0, 0, 0), (380, 235), (360, 235), 4)
pygame.draw.line(partyboy, (0, 0, 0), (415, 235), (440, 235), 4)
#eyes
pygame.draw.circle(partyboy, (255, 255, 255), (385, 235), 7)
pygame.draw.circle(partyboy, (255, 255, 255), (415, 235), 7)
pygame.draw.circle(partyboy, (0, 0, 205), (385, 235), 4)
pygame.draw.circle(partyboy, (0, 0, 205), (415, 235), 4)
#partygirl2
#head
pygame.draw.circle(partygirl2, (244, 164, 96), (640, 243), 40)
#neck
pygame.draw.line(partygirl2, (0, 0, 0), (640, 283), (640, 300), 10)
#dress
pygame.draw.polygon(
    background, (0, 139, 0), ((645, 300), (635, 300), (570, 400), (710, 400)))
#leg
pygame.draw.line(partygirl2, (0, 0, 0), (630, 390), (630, 470), 10)
pygame.draw.line(partygirl2, (0, 0, 0), (650, 390), (650, 470), 10)
#leftarm
pygame.draw.line(partygirl2, (0, 0, 0), (640, 290), (580, 320), 10)
#hair
pygame.draw.ellipse(partygirl2, (255, 228, 19), (675, 220, 10, 10), 4)
pygame.draw.ellipse(partygirl2, (255, 228, 19), (675, 240, 10, 10), 4)
pygame.draw.ellipse(partygirl2, (255, 228, 19), (675, 260, 10, 10), 4)
pygame.draw.ellipse(partygirl2, (255, 228, 19), (595, 220, 10, 10), 4)
pygame.draw.ellipse(partygirl2, (255, 228, 19), (595, 240, 10, 10), 4)
pygame.draw.ellipse(partygirl2, (255, 228, 19), (595, 260, 10, 10), 4)


#eyes
pygame.draw.circle(partygirl2, (255, 255, 255), (627, 235), 7)
pygame.draw.circle(partygirl2, (255, 255, 255), (650, 235), 7)

pygame.draw.circle(partygirl2, (0, 205, 0), (627, 235), 4)
pygame.draw.circle(partygirl2, (0, 205, 0), (650, 235), 4)
#lip
pygame.draw.polygon(
    partygirl2,
    (205, 16, 118), ((620, 258), (625, 268), (650, 268), (660, 258)))
#table
pygame.draw.line(background, (139, 69, 19), (700, 500), (700, 550), 10)
pygame.draw.line(background, (139, 69, 19), (700, 500), (840, 500), 10)
pygame.draw.line(background, (139, 69, 19), (840, 500), (840, 550), 10)
#musicplayer
pygame.draw.polygon(background, (0, 0, 0), ((
    710, 430), (830, 430),   (830, 500), (710, 500)))
pygame.draw.circle(background, (205, 0, 0), (730, 473), 13)
pygame.draw.circle(background, (0, 205, 0), (810, 473), 13)
pygame.draw.circle(background, (255, 215, 0), (770, 473), 13)
#ligthstick
pygame.draw.line(background, (0, 0, 0), (30, 0), (30, 20), 10)
pygame.draw.line(background, (0, 0, 0), (130, 0), (130, 20), 10)
pygame.draw.line(background, (0, 0, 0), (230, 0), (230, 20), 10)
pygame.draw.line(background, (0, 0, 0), (330, 0), (330, 20), 10)
pygame.draw.line(background, (0, 0, 0), (430, 0), (430, 20), 10)
pygame.draw.line(background, (0, 0, 0), (530, 0), (530, 20), 10)
pygame.draw.line(background, (0, 0, 0), (630, 0), (630, 20), 10)
pygame.draw.line(background, (0, 0, 0), (730, 0), (730, 20), 10)
pygame.draw.line(background, (0, 0, 0), (830, 0), (830, 20), 10)

lights = []


def render_light(surface, pos):
    pygame.draw.circle(surface, pygame.color.THECOLORS[random.choice(
        pygame.color.THECOLORS.keys())], pos, 6)


def update_lights():
    global updatedLights, lights
    for i in lights:
        render_light(updatedLights, i)


def draw_a_light(surface, pos):
    global lights
    render_light(surface, pos)
    lights.append(pos)

draw_a_light(background, (30, 20))
draw_a_light(background, (130, 20))
draw_a_light(background, (230, 20))
draw_a_light(background, (330, 20))
draw_a_light(background, (430, 20))
draw_a_light(background, (530, 20))
draw_a_light(background, (630, 20))
draw_a_light(background, (730, 20))
draw_a_light(background, (830, 20))
#musicnota


def drawmusic():
    pygame.draw.ellipse(musicnota, (255, 231, 186), (785, 405, 20, 15))
    pygame.draw.ellipse(musicnota, (255, 231, 186), (760, 410, 20, 15))
    pygame.draw.line(musicnota, (255, 231, 186), (778, 390), (778, 415), 2)
    pygame.draw.line(musicnota, (255, 231, 186), (804, 380), (804, 410), 2)
    pygame.draw.line(musicnota, (255, 231, 186), (778, 390), (805, 380), 2)

#one

Arm1 = pygame.Surface((850, 550)).convert_alpha()
Arm1.fill((0, 0, 0, 0))
#rigtharm
pygame.draw.line(Arm1, (0, 0, 0), (180, 310), (240, 310), 10)
#beer
pygame.draw.polygon(Arm1, (73, 23, 0), ((
    230, 320), (230, 300), (220, 300), (220, 320)))
pygame.draw.polygon(Arm1, (73, 23, 0), ((
    240, 388), (240, 320), (210, 320), (210, 388)))
Arm1Area = Arm1.subsurface(pygame.Rect((125, 250), (110, 110)))
#two
Arm2 = pygame.Surface((850, 550)).convert_alpha()
Arm2.fill((0, 0, 0, 0))
#rigtharm
pygame.draw.line(Arm2, (0, 0, 0), (180, 310), (240, 320), 10)
#beer
pygame.draw.polygon(Arm2, (73, 23, 0), ((
    230, 325), (230, 305), (220, 305), (220, 325)))
pygame.draw.polygon(Arm2, (73, 23, 0), ((
    240, 393), (240, 325), (210, 325), (210, 393)))
Arm2Area = Arm2.subsurface(pygame.Rect((125, 250), (110, 110)))
#three
Arm3 = pygame.Surface((850, 550)).convert_alpha()
Arm3.fill((0, 0, 0, 0))
#rigtharm
pygame.draw.line(Arm3, (0, 0, 0), (170, 310), (240, 320), 10)
#beer
pygame.draw.polygon(Arm3, (
    73, 23, 0), ((230, 330), (230, 310), (220, 310), (220, 330)))
pygame.draw.polygon(Arm3, (
    73, 23, 0), ((240, 403), (240, 325), (210, 325), (210, 403)))
Arm3Area = Arm3.subsurface(pygame.Rect((125, 250), (110, 110)))


y = 10
k = 130
counter = 0
clock = pygame.time.Clock()
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    screen.blit(partygirl2, (0, 0))
    #one

    rotatedArm = pygame.transform.rotate(
        Arm1Area, math.sin(counter/5.0)*15)

    rotArmRect = rotatedArm.get_rect()
    rotArmRect.center = (154, 295)
    screen.blit(rotatedArm, rotArmRect)
    #two
    rotatedArm2 = pygame.transform.rotate(
        Arm2Area, math.sin(counter/5.0)*15)
    rotArmRect2 = rotatedArm2.get_rect()
    rotArmRect2.center = (400, 295)
    screen.blit(rotatedArm2, rotArmRect2)
    #three
    rotatedArm3 = pygame.transform.rotate(
        Arm3Area, math.sin(counter/5.0)*15)
    rotArmRect3 = rotatedArm3.get_rect()
    rotArmRect3.center = (649, 285)
    screen.blit(rotatedArm3, rotArmRect3)
    screen.blit(partygirl1, (0, 0))
    if counter % 10 == 0:
        update_lights()
    screen.blit(updatedLights, (0, 0))
    screen.blit(partyboy, (0, 0))

    screen.blit(musicnota, (0, y))
    if counter == 10:
        drawmusic()

    if y == -300:
        y = 10
    y -= 1

    pygame.display.flip()
    counter += 1