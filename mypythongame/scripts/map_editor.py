"""
Meloonatic Melons
HPMRA Map Editor
By Harry Hitchen

Report issues to
meloonatic.help@techie.com

or send us a message at
http://www.meloonaticmessage.btck.co.uk/MessageUs
"""

import pygame, sys, math
from scripts.UltraColor import *
from scripts.Texture import *


def export_map(file):
    map_data = ""

    # Get Map Dimensions
    max_x = 0
    max_y = 0

    for t in tile_data:
        if t[0] > max_x:
            max_x = t[0]
        if t[1] > max_y:
            max_y = t[1]

    # Save Map Tiles
    for tile in tile_data:
        map_data = map_data + str(int(tile[0] / Tiles.Size)) + "," + str(int(tile[1] / Tiles.Size)) + ":" + tile[
            2] + "-"

    # Save Map Dimensions
    map_data = map_data + str(int(max_x / Tiles.Size)) + "," + str(int(max_y / Tiles.Size))

    # Write Map File
    with open(file, "w") as mapfile:
        mapfile.write(map_data)


window = pygame.display.set_mode((1280, 720), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()

txt_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

mouse_pos = 0
mouse_x, mouse_y = 0, 0

map_width, map_height = 100 * Tiles.Size, 100 * Tiles.Size

selector = pygame.Surface((Tiles.Size, Tiles.Size), pygame.HWSURFACE | pygame.SRCALPHA)
selector.fill(Color.WithAlpha(100, Color.CornflowerBlue))

tile_data = []

camera_x, camera_y = 0, 0
camera_move = 0

brush = "5"

# Initialize Default Map
for x in range(0, map_width, Tiles.Size):
    for y in range(0, map_height, Tiles.Size):
        tile_data.append([x, y, "1"])

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:

            # MOVEMENT
            if event.key == pygame.K_w:
                camera_move = 1
            elif event.key == pygame.K_s:
                camera_move = 2
            elif event.key == pygame.K_a:
                camera_move = 3
            elif event.key == pygame.K_d:
                camera_move = 4

            # BRUSHES
            if event.key == pygame.K_F4:
                brush = "r"
            elif event.key == pygame.K_F1:
                selection = input("Brush Tag: ")
                brush = selection

            # SAVE MAP
            if event.key == pygame.K_F11:
                name = input("Map Name: ")
                export_map(name + ".map")
                print("Map Saved Successfully!")


        elif event.type == pygame.KEYUP:
            camera_move = 0

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0] / Tiles.Size) * Tiles.Size
            mouse_y = math.floor(mouse_pos[1] / Tiles.Size) * Tiles.Size

        if event.type == pygame.MOUSEBUTTONDOWN:
            tile = [mouse_x - camera_x, mouse_y - camera_y, brush]  # Keep this as a list

            # Is a tile already placed here?
            found = False
            for t in tile_data:
                if t[0] == tile[0] and t[1] == tile[1]:
                    found = True
                    break

            # If this tile space is empty
            if not found:
                if not brush == "r":
                    tile_data.append(tile)

            # If this tile space is not empty
            else:
                # Are we using the rubber tool?
                if brush == "r":
                    # Remove Tile
                    for t in tile_data:
                        if t[0] == tile[0] and t[1] == tile[1]:
                            tile_data.remove(t)
                            print("Tile Removed!")

                else:
                    # Sorry! A tile is already placed here!
                    print("A tile is already placed here!")

    # LOGIC
    if camera_move == 1:
        camera_y += Tiles.Size
    elif camera_move == 2:
        camera_y -= Tiles.Size
    elif camera_move == 3:
        camera_x += Tiles.Size
    elif camera_move == 4:
        camera_x -= Tiles.Size

    # RENDER GRAPHICS

    window.fill(Color.Blue)

    # Draw Map
    for tile in tile_data:
        try:
            window.blit(Tiles.Texture_Tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
        except:
            pass

    # Draw Tile Highlighter (Selector)
    window.blit(selector, (mouse_x, mouse_y))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()


