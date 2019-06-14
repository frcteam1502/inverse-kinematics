import pygame
import math

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
STARTING_LOCATION = (350, 350)
LEG1_LENGTH = 150
LEG2_LENGTH = 150
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

#pygame.mouse.set_visible(False)
class Leg():
    global screen
    length = None
    end_point = None
    start_point = None
    angle = None
    def __init__(self, length):
        self.length = length
    def draw(self, start_point, angle):
        #self.angle = angle
        #y = self.length * math.sin(math.radians(angle))
        #x = math.sqrt(self.length ** 2 - y ** 2)
        #self.start_point = start_point
        #self.end_point = (start_point[0] + x, start_point[1] - y)
        pygame.draw.lines(screen, BLACK, False, [self.end_point, self.start_point], 5)

class End():
    global screen
    global STARTING_LOCATION
    pos = None
    bound = None

    def __init__(self, bound):
        self.bound = bound

    def draw(self, pos):
        mouse_x, mouse_y = PermissionError
        if not((STARTING_LOCATION[0] - mouse_x) ** 2 + (STARTING_LOCATION[1] - mouse_y) ** 2 > self.bound ** 2):
            pygame.draw.circle(screen, BLACK, (int(mouse_x), int(mouse_y)), 5)

    def bound_circle(self):
        pygame.draw.circle(screen, GREEN, STARTING_LOCATION, self.bound, 5)

def draw_lines():
    for line in range(SCREEN_WIDTH):
        if line % 10 == 0:
            pygame.draw.lines(screen, BLACK, False, [(0, line), (SCREEN_WIDTH, line)], 1)
    for line in range(SCREEN_HEIGHT):
        if line % 10 == 0:
            pygame.draw.lines(screen, BLACK, False, [(line, 0), (line, SCREEN_HEIGHT)], 1)
done = False
first_leg = Leg(LEG1_LENGTH)
second_leg = Leg(LEG2_LENGTH)
end = End(LEG1_LENGTH + LEG2_LENGTH)
line = 0


x_pos = None
y_pos = None
obj_1 = None
obj_2 = None
end_hyp = None
hyp = None
x = None
y = None
d = None
d1 = None
d2 = None
angle = None
d3 = None
d4 = None

pygame.mouse.set_visible(False)
while not done:
    
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    x_pos, y_pos = mouse_pos
    end_hyp = math.sqrt(x_pos ** 2 + y_pos ** 2)
    x = x_pos / end_hyp * min(end_hyp, LEG1_LENGTH + LEG2_LENGTH - 0.00001)
    y = y_pos / end_hyp * min(end_hyp, LEG1_LENGTH + LEG2_LENGTH - 0.00001)
    hyp = math.sqrt(x ** 2 + y ** 2)
    d = x ** 2 + y ** 2
    print(d)
    print((-d ** 2))
    print(-2 * d)
    print(LEG1_LENGTH + LEG2_LENGTH)
    print((-(d ** 2))/ (-2 * d * LEG1_LENGTH + LEG2_LENGTH))
    angle = math.acos((-(d ** 2))/ (-2 * d * LEG1_LENGTH + LEG2_LENGTH))
    d1 = x / d
    d2 = y / d
    d3 = LEG2_LENGTH * (d1 * math.cos(angle) - d2 * math.sin(angle))
    d4 = LEG2_LENGTH * (d1 * math.sin(angle) - d2 * math.sin(angle))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(WHITE)
    end.bound_circle()
    end.draw(mouse_pos)
    first_leg.end_point = (d3, d4)
    second_leg.end_point = (x,y)
    first_leg.draw(STARTING_LOCATION, 0)
    second_leg.draw(first_leg.end_point, first_leg.angle)
    pygame.display.flip()
    clock.tick(200)

pygame.quit()
