import pygame
from scripts.Texture import *

class Map_Engine:
    def add_tile(tile, pos, addTo):
        addTo.blit(tile, (pos[0] * Tiles.Size, pos[1] * Tiles.Size))

    def load_map(file):
        with open(file) as mapfile:
            map_data = mapfile.read()
        map_data = map_data.split("-")
        for i in range(len(map_data)):
            map_data[i] = map_data[i].replace('\n', '')
        # print(map_data)
        map_size = map_data[len(map_data)-1]
        map_data.remove(map_size)
        map_size = map_size.split(",")
        map_size[0] = int(map_size[0]) * Tiles.Size
        map_size[1] = int(map_size[1]) * Tiles.Size


        tiles=[]
        for tile in map_data:
            tile = tile.split(":")
            pos = tile[0].split(",")
            for p in pos:
                pos[pos.index(p)] = int(p)

            tile = (pos,tile[1])

            tiles.append(tile)

        terrain = pygame.Surface(map_size, pygame.HWSURFACE)

        for tile in tiles:
            if tile[1] in Tiles.Texture_Tag:
                Map_Engine.add_tile(Tiles.Texture_Tag[tile[1]], tile[0], terrain)

        return terrain





if __name__ == "__main__":
    Map_Engine.load_map("..\\maps\\world.map")