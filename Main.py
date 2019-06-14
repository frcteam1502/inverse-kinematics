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
        self.angle = angle
        y = self.length * math.sin(math.radians(angle))
        x = math.sqrt(self.length ** 2 - y ** 2)
        self.start_point = start_point
        self.end_point = (start_point[0] + x, start_point[1] - y)
        pygame.draw.lines(screen, BLACK, False, [self.end_point, self.start_point], 5)

class End():
    global screen
    global STARTING_LOCATION
    pos = None
    bound = None
    outside = False

    def __init__(self, bound):
        self.bound = bound

    def draw(self, pos):
        mouse_x, mouse_y = pos
        if not((STARTING_LOCATION[0] - mouse_x) ** 2 + (STARTING_LOCATION[1] - mouse_y) ** 2 > self.bound ** 2):
            pygame.draw.circle(screen, BLACK, (int(mouse_x), int(mouse_y)), 5)
            self.outside = False
        else: self.outside = True

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
static = False
y_back = False
y_forward = False
x_back = False
x_forward = False
end_loc = [0,0]
while not done:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_pos[0] < 650 and mouse_pos[0] > 600 and mouse_pos[1] < 650 and mouse_pos[1] > 600:
                    static = not static
        if event.type == pygame.KEYDOWN and static:
            if event.key == pygame.K_UP: y_forward = True
            if event.key == pygame.K_DOWN: y_back = True
            if event.key == pygame.K_RIGHT: x_forward = True
            if event.key == pygame.K_LEFT: x_back = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: y_forward = False
            if event.key == pygame.K_DOWN: y_back = False
            if event.key == pygame.K_RIGHT: x_forward = False
            if event.key == pygame.K_LEFT: x_back = False
    screen.fill(WHITE)
    if end.outside or static: pygame.mouse.set_visible(True)
    else: pygame.mouse.set_visible(False)

    if y_forward: end_loc[1] -= 1
    if y_back: end_loc[1] += 1
    if x_forward: end_loc[0] += 1
    if x_back: end_loc[0] -= 1

    pygame.draw.rect(screen, GREEN, (600, 600, 50, 50))
    end.bound_circle()
    print(end_loc)
    if not static:
        end.draw(mouse_pos)
        y_forward = False
        y_back = False
        x_forward = False
        x_back = False
    else: end.draw((STARTING_LOCATION[0] + end_loc[0], STARTING_LOCATION[1] + end_loc[1]))
    first_leg.draw(STARTING_LOCATION, 0)
    second_leg.draw(first_leg.end_point, first_leg.angle)
    pygame.display.flip()
    clock.tick(200)

pygame.quit()
