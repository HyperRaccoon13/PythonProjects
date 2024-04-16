import pygame
import random
import math

WIDTH, HEIGHT = 800, 600
MAXDOTS = 150
MAXDISTANCE = 100
backgroundColour = (0, 0, 0)
dotColour = (0, 0, 0)
lineColour = (255, 255, 255)

class Dot:
    def __init__(self, xPostion, yPostion):
        self.xPostion = xPostion
        self.yPostion = yPostion
        self.radius = 0
        self.speed = 1
        self.xVelocity = 0
        self.yVelocity = 0
        self.maxSpeed = 1
        self.acceleration = 0.1

    def move(self):
        # *Makes the velocity random as hell
        self.xVelocity += random.uniform(-self.acceleration, self.acceleration)
        self.yVelocity += random.uniform(-self.acceleration, self.acceleration)

        # *Slows the velocity right down
        self.xVelocity = max(-self.maxSpeed, min(self.xVelocity, self.maxSpeed))
        self.yVelocity = max(-self.maxSpeed, min(self.yVelocity, self.maxSpeed))

        self.xPostion += self.xVelocity
        self.yPostion += self.yVelocity

        # *Respawns the dot if its off the screen
        if self.xPostion < self.radius or self.xPostion > WIDTH - self.radius or self.yPostion < self.radius or self.yPostion > HEIGHT - self.radius:
            self.xPostion = random.randint(self.radius, WIDTH - self.radius)
            self.yPostion = random.randint(self.radius, HEIGHT - self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, dotColour, (int(self.xPostion), int(self.yPostion)), self.radius)


pygame.init()
pygame.display.set_caption("Cool Art By Hyper")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

dots = [Dot(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(MAXDOTS)]

running = True
while running:
    screen.fill(backgroundColour)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    for dot in dots:
        dot.move()

    for i in range(len(dots)):
        for j in range(i + 1, len(dots)):
            firstDot = dots[i]
            secondDot = dots[j]
            distance = math.sqrt((firstDot.xPostion - secondDot.xPostion) ** 2 + (firstDot.yPostion- secondDot.yPostion) ** 2)
            if distance < MAXDISTANCE:
                pygame.draw.line(screen, lineColour, (int(firstDot.xPostion), int(firstDot.yPostion)), (int(secondDot.xPostion), int(secondDot.yPostion)), 1)
    
    for dot in dots:
        dot.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit