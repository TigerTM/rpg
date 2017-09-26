import pygame, sys, time
from scripts.UltraColor import *
from scripts.Texture import *
from scripts.Globals import *
from scripts.map_engine import *

pygame.init()

clock = pygame.time.Clock()
cSec = 0
cFrame = 0
FPS = 0

terrain = Map_Engine.load_map("maps\\world.map")

fps_font = pygame.font.Font("c:\\Windows\\Fonts\\Verdana.ttf", 20)

sky = pygame.image.load("graphics\\sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0, 0))
del sky


def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.Goldenrod)
    window.blit(fps_overlay, (0, 0))


def create_window():
    global window, window_width, window_height, window_title
    window_width, window_height = 800, 600
    window_title = "My Game"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE | pygame.DOUBLEBUF)


def count_fps():
    global cSec, cFrame, FPS, deltatime
    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        if FPS > 0:
            deltatime = 1 / FPS


create_window()

isRunning = True

while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.camera_move = 1
            elif event.key == pygame.K_s:
                Globals.camera_move = 2
            elif event.key == pygame.K_a:
                Globals.camera_move = 3
            elif event.key == pygame.K_d:
                Globals.camera_move = 4

        elif event.type == pygame.KEYUP:
            Globals.camera_move = 0

    # Logic
    if Globals.camera_move == 1:
        Globals.camera_y += 100 * deltatime
    elif Globals.camera_move == 2:
        Globals.camera_y -= 100 * deltatime
    elif Globals.camera_move == 3:
        Globals.camera_x += 100 * deltatime
    elif Globals.camera_move == 4:
        Globals.camera_x -= 100 * deltatime

    # Render Graphics
    window.blit(Sky, (0, 0))

    # Render Simple Terrain Grid
    window.blit(terrain, (Globals.camera_x, Globals.camera_y))

    show_fps()

    pygame.display.update()

    count_fps()
    # clock.tick(10)
pygame.quit()
sys.exit()
