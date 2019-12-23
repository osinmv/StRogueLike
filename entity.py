import tcod
import typing
from default_settings import DEFAULT_FOREGROUND, DEFAULT_BACKGROUND
from world_map import Tile
import math


class Entity():
    def __init__(self, name: str, pos_x: int, pos_y: int,
                 symbol: str, color: tcod.color.Color):
        self.name = name
        self.x = pos_x
        self.y = pos_y
        self.symbol = symbol
        self.color = color

    def move(self, vector: tuple, game_map: typing.List[typing.List[Tile]]) -> bool:
        """Return True if entity moved according to vector, False otherwise
        """
        x, y = vector
        if not game_map[self.y+y][self.x+x].blocked:
            self.x += x
            self.y += y
            return True
        else:
            return False

    @property
    def position(self):
        """Return coordinates as tuple of (x,y)"""
        return (self.x, self.y)

    def set_path(self, path: tuple):
        """Set sequence of steps in path to a goal, the last tuple in path
        """
        # if path is None or len(path) == 0:
        #     return
        self.path = path

    def follow_path(self, game_map: typing.List[typing.List[Tile]]) -> None:
        """Move one step from 
        """
        if not(self.path is None or len(self.path) == 0):
            next_step = self.path.pop(0)
            if not(self.move((next_step[0]-self.x, next_step[1]-self.y), game_map)):
                self.path = None

    def make_decision(self, game_map: typing.List[typing.List[Tile]]):
        """Call function according to game_map
        AI decisions, for player it will be overwriten
        """
        # TODO uncomment when functions and checks are implemented
        # if self.can_attack:
        #    self.attack()
        # if self.low_health() and self.supposed_to_run_away:
        #    self.run_away()
        if hasattr(self, "path"):
            if not(self.path is None) and len(self.path) > 0:
                self.follow_path(game_map)
        else:

            pass
            # print("I have nowhere to go")

# def draw_entity(self, console: tcod.console.Console):
# """Draw self.symbol at self.x,self.y on console
#        """
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
