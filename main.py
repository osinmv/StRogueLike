import tcod
import typing
from entity import Entity
from default_settings import *
from input_handler import key_handler, mouse_handler
from world_map import world_generation, Tile, path_finder
import random
# char start is on 32, so add each time 32 to a number u get from png

PLAYER = Entity("STALKER", 30, 30, chr(33), PLAYER_FOREGROUND)
CURRENT_LOCATION = SWAMP_COLORS
ENTITIES = []

ACTIONS = {
    "move": (PLAYER.move, "move", "game_map")
}


def draw_tile(x: int, y: int, console: tcod.console.Console,
              tile_type: str, symbol: str, color=None) -> None:
    """Draw symbol at x,y on console according to type of default
    or specified color
    """
    # TODO carefull, tile_type can be even empty
    if color is None:
        color = CURRENT_LOCATION[tile_type][random.randint(0, 1)]
    tcod.console_set_default_foreground(
        console, color)
    tcod.console_put_char(console, x, y,
                          symbol, tcod.BKGND_NONE)


def render_world(console: tcod.console.Console,
                 game_map: typing.List[typing.List[float]]):
    """Render game_map on console
    """
    tile_type = ""
    symbol = LAND
    for row in range(len(game_map)):
        for column, value in enumerate(game_map[row]):
            if value.blocked and not value.block_sight:
                tile_type = "wall"
            elif value.blocked and value.block_sight:
                tile_type = "obstacle"
            else:
                tile_type = "walkable_land"
            draw_tile(column, row, console, tile_type, symbol)


def render_entities(console: tcod.console.Console) -> None:
    """Draw entities of console
    """
    for creature in ENTITIES:
        draw_tile(creature.x, creature.y, console, "",
                  creature.symbol, color=creature.color)


def clear_entities(console: tcod.console.Console,
                   game_map: typing.List[typing.List[Tile]]) -> None:
    """Clear entities from console
    """
    for creature in ENTITIES:
        draw_tile(creature.x, creature.y, console, "walkable_land", LAND)


def main():
    tcod.console_set_custom_font(
        DEFAULT_TEXTURES, tcod.FONT_TYPE_GRAYSCALE |
        tcod.FONT_LAYOUT_TCOD, 16, 16)
    tcod.console_init_root(WIDTH, HEIGHT, TITLE, fullscreen=FULLSCREEN)

    tcod.console_set_default_foreground(0, DEFAULT_FOREGROUND)
    # game window
    game_window = tcod.console_new(WIDTH, HEIGHT)
    # mouse and key event handlers
    mouse = tcod.Mouse()
    tcod.mouse_show_cursor(True)
    key = tcod.Key()
    tcod.sys_set_fps(30)
    game_map = world_generation.generate_global_map((50, 50))
    render_world(game_window, game_map)
    ENTITIES.append(PLAYER)
    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)
        tcod.console_set_default_foreground(game_window, DEFAULT_FOREGROUND)

        # start

        render_entities(game_window)
        tcod.console_blit(game_window, 0, 0, WIDTH, HEIGHT, 0, 0, 0)
        tcod.console_flush()
        # clear
        clear_entities(game_window, game_map)
        # key_handling
        mouse_action = mouse_handler(mouse)
        key_action = key_handler(key)
        move = key_action.get("move")
        exit = key_action.get("exit")
        path = mouse_action.get("path")
        wait = key_action.get("wait")

        if move:
            PLAYER.move(move, game_map)
        elif exit:
            return True
        elif path:
            new_path = path_finder.find_path(PLAYER.position, path, game_map)
            PLAYER.set_path(new_path)
        elif wait:
            PLAYER.make_decision(game_map)


if __name__ == "__main__":
    main()
