import tcod


DEFAULT_BACKGROUND = tcod.darker_sea
DEFAULT_FOREGROUND = tcod.dark_red
HEIGHT = 50
WIDTH = 50
TITLE = "GAME OF YEAR"
DEFAULT_TEXTURES = "nordik.png"
FULLSCREEN = False
PLAYER_FOREGROUND = tcod.lime
MAP_COLORS = {"vendor": [tcod.green],
              "wall": [tcod.darker_grey, tcod.grey,
                       tcod.darkest_lime, tcod.darkest_sea],
              "characters": [tcod.desaturated_flame]}
SWAMP_COLORS = {"wall": [tcod.darkest_lime, tcod.darkest_sea],
                "obstacle": [tcod.darker_grey, tcod.grey],
                "walkable_land": [tcod.desaturated_green, tcod.darker_green]}
# enum
TURNS = ("PLAYER", "WORLD", "ENEMY", "ENEMY", "PLAYER", "WORLD")
LAND = "#"
