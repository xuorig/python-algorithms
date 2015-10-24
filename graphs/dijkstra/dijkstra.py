from utils.priority_queue import PriorityQueue

graph_with_weights = {
  'A': set([('B', 2),('C', 4),('D', 1)]),
  'B': set([('A', 2),('E', 4),('F', 6)]),
  'C': set([('A', 4),('F',3)]),
  'D': set([('A', 1),('G', 8)]),
  'E': set([('B', 4)]),
  'F': set([('B',6),('C',3),('G',2)]),
  'G': set([('F',2),('G', 8)])
}

def dijkstra(graph, source, target):
    # Build the path from source to target using the prev map
    def build_path(prev):
        result = []
        u = target
        while prev[u]:
            result.append(u)
            u = prev[u]
        result.append(u)
        result.reverse()
        return result

    # Initialize a priority queue and a distance and previous map
    Q = PriorityQueue()
    dist = {}
    prev = {}

    # Build the dist and prev map for all vertex
    for vertex in graph.keys():
        dist[vertex] = float('inf')
        prev[vertex] = None
        # Insert the source into the PriorityQueue
        Q.put(vertex, dist[vertex])

    # Init the source dist to 0
    dist[source] = 0

    while not Q.empty():
        u = Q.get()
        # if vertex is the target, return the path
        if u == target:
            return build_path(prev)

        # For every neighbor of the vertex
        for neighbor in graph[u]:
            # Calculate new distance for neighbor
            alt = dist[u] + neighbor[1]
            # If a shorter path to the neighbor has been found,
            # update dist and prev maps
            if alt < dist[neighbor[0]]:
                dist[neighbor[0]] = alt
                prev[neighbor[0]] = u
    # We never got to target
    return None

print dijkstra(graph_with_weights, 'A', 'G')
