import typing
from .tiles import Tile
from .world_generation import get_neighbours


class Node():
    def __init__(self, point: tuple, parent=None):
        """Initialise Node object with point as tuple of x,y coordinates
        and parent as Node if exists 

        Precondition: point[0]>=0 and point[1]>=0
        """
        self.position = point
        self.parent = parent
        self.h, self.g, self.f = (0, 0, 0)

    def __eq__(self, other_node) -> bool:
        return self.position == other_node.position


def find_path(start: tuple, end: tuple,
              game_map: typing.List[typing.List[Tile]]) -> tuple:
    """Return  path as tuple of nodes/points from start to end  using game_map 
    """
    strict = True
    if game_map[end[1]][end[0]].blocked:
        strict = False
    start_node = Node(start)
    end_node = Node(end)

    potential_nodes = []
    watched_nodes = []

    potential_nodes.append(start_node)

    while len(potential_nodes) > 0:
        current_node = potential_nodes[0]
        current_index = 0
        for index, item in enumerate(potential_nodes):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        potential_nodes.pop(current_index)
        watched_nodes.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while not(current is None):
                path.append(current.position)
                current = current.parent
            return path[::-1]
        neighbours = []

        for neighbour in get_neighbours(game_map,
                                        current_node.position, strict=strict):
            neighbours.append(Node(neighbour, parent=current_node))

        for neighbour in neighbours:
            for point in watched_nodes:
                if point == neighbour:
                    continue

            neighbour.g = current_node.g+1
            neighbour.h = ((neighbour.position[0]-end_node.position[0])**2+(
                neighbour.position[1]-end_node.position[1])**2)
            neighbour.f = neighbour.g+neighbour.h
            for potential_node in potential_nodes:
                if neighbour == potential_node:
                    continue
            potential_nodes.append(neighbour)
