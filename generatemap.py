from edge import *
from corner import *
from resource import *

MAX_EDGES = 72
MAX_CORNERS = 54
MAX_TILES = 19

class Map:
    def __init__(self):
        self.edges = []
        self.corners = []
        self.tiles = []
        self.generate()

    def generate(self):
        # first initialize 72 edges
        i = 0
        while i < MAX_EDGES:
            self.edges.append(Edge(i))
            i += 1
        # initialize all the corners as well
        i = 0
        while i < MAX_CORNERS:
            self.corners.append(Corner(i))
            i += 1
        # now set the blocks
        for i in range(MAX_TILES):
            res = Resource(i)



