class Corner:
    def __init__(self, index):
        self.index = index
        self.neighbors = []
        self.edges = []
        self.house = None
        self.settlement = None