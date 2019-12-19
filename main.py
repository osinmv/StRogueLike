import tcod
import typing
from entity import Entity
from default_settings import *
from input_handler import key_handler
from world_map import world_generation
import random
PLAYER = Entity("STALKER", 5, 5, "$", PLAYER_FOREGROUND)
CURRENT_LOCATION = SWAMP_COLORS


def render_world(console: tcod.console.Console, game_map: typing.List[typing.List[float]]):
    """Render game_map on console
    """
    for row in range(len(game_map)):
        for column, value in enumerate(game_map[row]):
            if value.blocked and not value.block_sight:
                tcod.console_set_default_foreground(
                    console, CURRENT_LOCATION["wall"][random.randint(0, 1)])
            elif not value.block_sight:
                tcod.console_set_default_foreground(
                    console, CURRENT_LOCATION["obstacle"][random.randint(0, 1)])
            else:
                tcod.console_set_default_foreground(
                    console, CURRENT_LOCATION["walkable_land"][random.randint(0, 1)])
            tcod.console_put_char(console, row, column,
                                  "=", tcod.BKGND_NONE)


def render_entities(console: tcod.console.Console):
    """Draw entities of console
    """
    PLAYER.draw(console)


def clear_entities(console: tcod.console.Console):
    """Clear entities from console
    """
    PLAYER.clear(console)


def main():
    tcod.console_set_custom_font(
        DEFAULT_TEXTURES, tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(WIDTH, HEIGHT, TITLE, fullscreen=FULLSCREEN)

    tcod.console_set_default_foreground(0, DEFAULT_FOREGROUND)
    # game window
    game_window = tcod.console_new(WIDTH, HEIGHT)
    # mouse and key event handlers
    key = tcod.Key()
    tcod.sys_set_fps(15)
    game_map = world_generation.generate_global_map((50, 50))
    render_world(game_window, game_map)

    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, None)
        tcod.console_set_default_foreground(game_window, DEFAULT_FOREGROUND)

        # start

        render_entities(game_window)
        tcod.console_blit(game_window, 0, 0, WIDTH, HEIGHT, 0, 0, 0)
        tcod.console_flush()
        # clear
        clear_entities(game_window)
        # key_handling

        action = key_handler(key)
        move = action.get("move")
        exit = action.get("exit")

        if move:
            if not game_map[PLAYER.y+move[0]][PLAYER.x+move[1]].blocked:
                PLAYER.move(move)
        elif exit:
            return True


if __name__ == "__main__":
    main()
