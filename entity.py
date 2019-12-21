import tcod
import typing
from default_settings import DEFAULT_FOREGROUND,DEFAULT_BACKGROUND


class Entity():
    def __init__(self, name: str, pos_x: int, pos_y: int, symbol: str, color: tcod.color.Color):
        self.name = name
        self.x = pos_x
        self.y = pos_y
        self.symbol = symbol
        self.color = color

    def move(self, vector: tuple):
        """
        Change x,y coordinates based on vector
        """
        y, x = vector
        self.x += x
        self.y += y

# def draw_entity(self, console: tcod.console.Console):
        """Draw self.symbol at self.x,self.y on console
        """
#         
# 
# def clear_entity(self, console: tcod.console.Console):
#         """Clear cell at self.x,self.y on console
#         """
#         tcod.console_set_default_foreground(console, DEFAULT_FOREGROUND)
#         tcod.console_put_char(console, self.x, self.y,
#                               " ", tcod.BKGND_NONE)
# 
    # def damage_decorator(self,func:typing.Callable[[],None]):
    #    """Wrap damage function
    #    """
    #    def apply_damage(self,):