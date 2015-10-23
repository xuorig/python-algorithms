from utils.priority_queue import PriorityQueue
from graph.a_star.a_star_grid import AStarGrid
from collections import defaultdict

def reconstruct_path(came_from, start, goal):
    import pdb; pdb.set_trace()
    current = goal
    path = [current]
    while current != start:
        print current
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def heuristic(node, goal):
    dx = abs(node[0] - goal[0])
    dy = abs(node[1] - goal[1])
    return 1 * (dx + dy)

def a_star(grid, start, goal):
    # Manhattan Distance
    # https://en.wikipedia.org/wiki/Taxicab_geometry

    open_queue = PriorityQueue()
    open_queue.put(start, 0)
    closed = set()

    came_from = {}
    g_score = defaultdict(lambda: float('inf'))
    g_score[start] = 0

    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = g_score[start] + heuristic(start, goal)

    while not open_queue.empty():
        # Pop the node with the lowest f score
        current = open_queue.get()
        closed.add(current)
        print current
        # If we hit our goal, return the path
        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor in grid.neighbors(current):
            if neighbor in closed:
                continue

            g = g_score[current] + grid.dist_between(current, neighbor)
            h = heuristic(neighbor, goal)
            f = g + h

            if neighbor not in open_queue:
                open_queue.put(neighbor, f)
            elif g >= g_score[neighbor]:
                continue

            came_from[neighbor] = current
            g_score[neighbor] = g
            f_score[neighbor] = f
    return None

grid = AStarGrid(4, 4)
print a_star(grid, (0,0), (3,3))
