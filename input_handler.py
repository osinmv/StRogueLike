import tcod


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
        return {"move": (-1, 0)}
    elif key.vk == tcod.KEY_DOWN:
        return {"move": (1, 0)}
    elif key.vk == tcod.KEY_RIGHT:
        return {"move": (0, 1)}
    elif key.vk == tcod.KEY_LEFT:
        return {"move": (0, -1)}
    else:
        return {"waiting": True}
