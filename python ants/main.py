import pygame
import math
import random

WIDTH, HEIGHT = 800, 600
antSize = 10
antColour = (0,0,255)
backgroundColour = (0,0,0)
numberOfAnts = 50
nestColour = (170, 0, 0)
foodColour = (0, 170, 0)
foodSize = 5


pygame.init()
pygame.display.set_caption("Ant")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def RotateTriangle(xPostion, yPostion, centerX, centerY, angle):
        sinAngle = math.sin(angle)
        cosAngle = math.cos(angle)

        xPostion -= centerX
        yPostion -= centerY

        rotatedXPostion = xPostion * cosAngle - yPostion * sinAngle
        rotatedYPostion = xPostion * sinAngle + yPostion * cosAngle

        xPostion = rotatedXPostion + centerX
        yPostion = rotatedYPostion + centerY
        return(xPostion, yPostion)


def DrawTriangle(xPostion, yPostion, size, angle):

        triangleFirstPoint = RotateTriangle(xPostion, yPostion - size / math.sqrt(3), xPostion, yPostion, angle)
        triangleSecondPoint = RotateTriangle(xPostion - size / 2, yPostion + size / (2 * math.sqrt(3)), xPostion, yPostion, angle)
        triangleThirdPoint = RotateTriangle(xPostion + size / 2, yPostion + size / (2 * math.sqrt(3)), xPostion, yPostion, angle)
        
        return [triangleFirstPoint, triangleSecondPoint, triangleThirdPoint]
        


class Food:
    def __init__(self, xPostion, yPostion):
        self.xPostion = xPostion
        self.yPostion = yPostion
        self.numberOfFoodParts = 0 
    
    def DrawFood(self, screen):
        pygame.draw.rect(screen, foodColour, (self.xPostion, self.yPostion, foodSize, foodSize))

class FoodCluster:
    def __init__(self, rows, cols, xPostion, yPostion):
        self.rows = rows
        self.cols = cols
        self.xPostion = xPostion
        self.yPostion = yPostion
        self.food = [[Food(xPostion + x * (foodSize + 5), yPostion + y * (foodSize + 5)) for y in range(rows)] for x in range(cols)]

    def DrawFoodCluster(self, screen):
        for row in self.food:
             for food in row:
                  food.DrawFood(screen)

class Nest:
    def __init__(self, xPostion, yPostion):
        self.xPostion = xPostion
        self.yPostion = yPostion
        self.nestSize = 25
        self.foodCount = 0

    def DrawNest(self):
        pygame.draw.circle(screen, nestColour, (self.xPostion, self.yPostion), self.nestSize)

class Ant:
    def __init__(self, xPostion, yPostion):
        self.xPostion = xPostion
        self.yPostion = yPostion
        self.speed = 1
        self.xVelocity = 0
        self.yVelocity = 0
        self.maxSpeed = 1
        self.acceleration = 0.1
        self.angle = 0

        
    def DrawAnt(self, screen, antSize, antColour):
        pygame.draw.polygon(screen, antColour, DrawTriangle(self.xPostion, self.yPostion, antSize, self.angle))


    def FreeMove(self):
        self.xVelocity += random.uniform(-self.acceleration, self.acceleration)
        self.yVelocity += random.uniform(-self.acceleration, self.acceleration)
        self.xVelocity = max(-self.maxSpeed, min(self.maxSpeed, self.xVelocity))
        self.yVelocity = max(-self.maxSpeed, min(self.maxSpeed, self.yVelocity))

        if self.xPostion + self.xVelocity > WIDTH:
            self.xPostion = 0

        elif self.xPostion + self.xVelocity < 0:
            self.xPostion = WIDTH


        if self.yPostion + self.yVelocity > HEIGHT:
            self.yPostion = 0

        elif self.yPostion + self.yVelocity < 0:
            self.yPostion = HEIGHT
            
        self.xPostion += self.xVelocity
        self.yPostion += self.yVelocity

        
        
        
ants = [Ant(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(numberOfAnts)]

nest = Nest(WIDTH/2, HEIGHT/2)

foodCluster = FoodCluster(10, 10, 5, 400)

for ant in ants:
        ant.xPostion = nest.xPostion
        ant.yPostion = nest.yPostion

running = True
while running:
    screen.fill(backgroundColour)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    nest.DrawNest()
    foodCluster.DrawFoodCluster(screen)

    for ant in ants:
        ant.FreeMove()
        ant.DrawAnt(screen, antSize, antColour)



    pygame.display.flip()
    clock.tick(60)

pygame.quit