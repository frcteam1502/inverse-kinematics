import math
import pygame

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 175, 255)
STARTING_LOCATION = (350, 350)
ORIGIN = (0, 0)
LEG1_LENGTH = 200
LEG2_LENGTH = 100

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Inverse kinematics demo')

clock = pygame.time.Clock()
done = False

def screen_to_math_coords(coords):
    return (coords[0] - STARTING_LOCATION[0], -(coords[1] - STARTING_LOCATION[1]))

def math_to_screen_coords(coords):
    return (STARTING_LOCATION[0] + coords[0], STARTING_LOCATION[1] - coords[1])


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)

    mouse_pos = pygame.mouse.get_pos()
    relative_mouse_pos = screen_to_math_coords(mouse_pos)
    rel_mouse_x, rel_mouse_y = relative_mouse_pos
    distance = math.sqrt(rel_mouse_x ** 2 + rel_mouse_y ** 2)
    print('rel', relative_mouse_pos)
    # Optional: constrain mouse coords to be within distance
    MIN_DISTANCE = LEG1_LENGTH - LEG2_LENGTH
    MAX_DISTANCE = LEG1_LENGTH + LEG2_LENGTH
    distance_multiplier = 1
    if distance == 0: distance = 1
    if distance > MAX_DISTANCE: distance_multiplier = MAX_DISTANCE / distance
    if distance < MIN_DISTANCE: distance_multiplier = MIN_DISTANCE / distance
    distance *= distance_multiplier
    rel_mouse_x *= distance_multiplier
    rel_mouse_y *= distance_multiplier

    # Math
    try:
        a1 = math.atan2(rel_mouse_y, rel_mouse_x)
        second_angle = math.asin((rel_mouse_y ** 2 + rel_mouse_x ** 2 - LEG1_LENGTH ** 2 - LEG2_LENGTH ** 2)
                / 2 / LEG1_LENGTH / LEG2_LENGTH)
        a2 = math.asin(LEG2_LENGTH * math.cos(second_angle) / distance)
        first_angle = a1 + a2
        print('First angle', first_angle)
        print('Second angle', second_angle)

        elbow_point = (LEG1_LENGTH * math.cos(first_angle), LEG1_LENGTH * math.sin(first_angle))
        elbow_point_screen = math_to_screen_coords(elbow_point)

        pygame.draw.circle(screen, BLUE, (int(elbow_point_screen[0]), int(elbow_point_screen[1])), LEG2_LENGTH, 1)
        pygame.draw.circle(screen, BLUE, STARTING_LOCATION, LEG1_LENGTH, 1)
        pygame.draw.line(screen, BLACK, math_to_screen_coords(ORIGIN), elbow_point_screen)
        pygame.draw.line(screen, BLACK, elbow_point_screen, mouse_pos)
    except (ValueError, ZeroDivisionError) as e:
        print(e)
    pygame.display.flip()
    clock.tick(200)

pygame.quit()
