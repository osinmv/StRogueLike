import typing
from .tiles import Tile
import tcod
from .tweaks import UPPER_BOUND, MID_BOUND

# class Room():
#    def __init__(point1: tuple, point2: tuple):
#        """Create rectangular room according to point1 and point2
#        """
#        self.top_left = point1
#        self.bottom_right = point2
#


def generate_global_map(shape: tuple) -> typing.List[typing.List[Tile]]:
    """Return simple rectangular map with shape shape
    Precondition: len(shape)==2
    """
    # create height map
    global_map = tcod.heightmap_new(shape[0], shape[1])
    # voroni
    tcod.heightmap_add_voronoi(
        global_map, 2, 2, [0.1, 1.5, 0.6, 1.7, 0.8], rnd=0)
    # normalize
    tcod.heightmap_normalize(global_map)
    # assign TILE to every value of heightmap
    tile_map = []

    for row in global_map:
        holder = []
        for value in row:
            if value > UPPER_BOUND:
                holder.append(Tile(True))
            elif value > MID_BOUND:
                holder.append(Tile(True, block_sight=False))
            else:
                holder.append(Tile(False))
        tile_map.append(holder)
    return tile_map

def check_walkable(map)-> bool:
    pass
    