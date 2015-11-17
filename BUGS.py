import pygame
import random

pygame.init()
pygame.font.init()

class World:
    FONT = pygame.font.SysFont(None, 20)
    WORLD_POS = (400,400)
    XINC = 15
    YINC = 15

    def __init__(self, size, space, screen):
        self.size = size
        self.space = space
        self.screen = screen
        self.arena = [[self.space for column in range(self.size)] for row in range(self.size)]
        self.pad = (self.size//2)*15
        self.draw()
        self.createBounds("+")

    def draw(self):
        self.screen.fill((0,0,0))
        rowcount = 0
        for row in self.arena:
            colcount = 0
            for column in row:
                text = self.FONT.render(column, False, (0,255,50))
                self.screen.blit(text,
                (((self.WORLD_POS[0] - self.pad) + rowcount*self.XINC),
                ((self.WORLD_POS[1] - self.pad) + colcount*self.YINC)))
                colcount += 1
            rowcount += 1

    def clearSpace(self, loc):
        self.arena[loc[0]][loc[1]] = self.space
        self.draw()

    def updateWorld(self, data, loc):
        self.arena[loc[0]][loc[1]] = data
        self.draw()

    def createBounds(self, boundIcon):
        for row in range(self.size):
            for column in range(self.size):
                if row == 0 or row == self.size-1 or column == 0 or column == self.size-1:
                    self.updateWorld(boundIcon, (row, column))

    def randomizeWorld(self, num):
        for i in range(num):
            ranX = random.randint(1, w1.size-2)
            ranY = random.randint(1, w1.size-2)
            self.updateWorld("#", loc=(ranX,ranY))

    def flat(self):
        return sum(self.arena, [])

    def __str__(self):
        w = []
        for row in self.arena:
            w.append("".join(row))

        return ("\n".join(w))


class Bug:
    TYPES = ("&","x")

    def __init__(self, world, name, state=True, pos=[0,0]):
        self.world = world
        self.name = name
        self.state = state
        self.pos = pos
        self.pos = [self.world.size//2, self.world.size//2]
        self.build()

    def bugState(self):
        if not self.state:
            return self.TYPES[1]
        else:
            return self.TYPES[0]

    def kill_bug(self):
        self.state = False
        self.build()

    def build(self):
        self.world.updateWorld(self.bugState(), self.pos)

    def move(self, dir):
        self.world.clearSpace(self.pos)
        self.pos[0] += dir[0]
        self.pos[1] += dir[1]
        if not 0 <= self.pos[0] < self.world.size:
            self.pos[0] -= dir[0]
        if not 0 <= self.pos[1] < self.world.size:
            self.pos[1] -= dir[1]
        self.build()

    def checkSpace(self, obst):
        indexS = [[] for row in range(self.world.size)]
        indexF = [i for i, x in enumerate(self.world.flat()) if x == obst]

    def __str__(self):
        return str(self.bugState()) + str(self.pos)


if __name__ == "__main__":
    screen = pygame.display.set_mode((800, 800))

    w1 = World(50, "[  ]", screen)

    w1.randomizeWorld(50)

    b1 = Bug(w1, "01")

    clock = pygame.time.Clock()

    running = True

    while running:
        w1.draw()

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys[pygame.K_q]:
                print("Quit")
                running = False

            if keys[pygame.K_DOWN]:
                b1.move([0,1])
                print("down")
            if keys[pygame.K_UP]:
                b1.move([0,-1])
                print("up")
            if keys[pygame.K_RIGHT]:
                b1.move([1,0])
                print("right")
            if keys[pygame.K_LEFT]:
                b1.move([-1,0])
                print("left")

        pygame.display.flip()
        clock.tick(25)



