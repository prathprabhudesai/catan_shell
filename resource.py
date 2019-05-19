NW = 0
NE = 1
E = 2
SE = 3
SW = 4
W = 5


class Resource:
    def __init__(self, map_index):
        self.map_index = map_index
        self.res_type = None
        self.res_value = None
        self.edges = [None] * 6
        self.corners = [None] * 6



