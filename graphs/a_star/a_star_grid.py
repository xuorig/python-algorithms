class AStarGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def inside_grid(self, node):
        return 0 <= node[0] < self.width and 0 <= node[1] < self.height

    def passable(self, node):
        return node not in self.walls

    def dist_between(self, node, dest_node):
        # Modify this for different weight grids
        return 1

    def is_valid_neighbor(self, node):
        return self.passable(node) and self.inside_grid(node)

    def neighbors(self, node):
        x, y = node
        neighbors = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        return filter(self.is_valid_neighbor, neighbors)
