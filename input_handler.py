import tcod
import math

PIXEL_SIZE = 16


def key_handler(key: tcod.Key) -> dict:
    """Return dictionary associated with key pressed in key in format 
    {"action_name":data}, where data can be anything
    """

    if key.vk == tcod.KEY_ESCAPE:
        return {"exit": True}
    elif key.vk == tcod.KEY_F11:
        return {"fullscreen": True}
    elif key.vk == tcod.KEY_F10:
        return {"fullscreen": False}
    elif key.vk == tcod.KEY_UP:
        return {"move": (0, -1)}
    elif key.vk == tcod.KEY_DOWN:
        return {"move": (0, 1)}
    elif key.vk == tcod.KEY_RIGHT:
        return {"move": (1, 0)}
    elif key.vk == tcod.KEY_LEFT:
        return {"move": (-1, 0)}
    # elif key.c == ord("r"):
    #    return {"path": True}
    else:
        return {"wait": True}


def mouse_handler(mouse: tcod.Mouse) -> dict:
    """Return dict of acction when mouse is pressed
    in format {"action_name":data}
    """
    #print(str(mouse.x) + " " + str(mouse.y))
    if mouse.lbutton:
        return {"path": mouse_to_ingame_ccordinates(mouse.x, mouse.y)}
    elif mouse.rbutton:
        return {"draw": mouse_to_ingame_ccordinates(mouse.x, mouse.y)}
    else:
        return {"wait": True}


def mouse_to_ingame_ccordinates(x: int, y: int) -> tuple:
    return (math.floor(x/PIXEL_SIZE), math.floor(y/PIXEL_SIZE))
