import tcod
import math


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
        return {"path": (math.floor(mouse.x/16), math.floor(mouse.y/16))}
    else:
        return {"wait": True}
