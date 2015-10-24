# Dijkstra's algorithm

Dijkstra's algorithm is used to find the shortest path from a start node to every other node in a graph. It can be modified to find the shortest past from start to goal, which is what I implemented here.

We first initialize a distance map with nodes as keys and the best distance found to that node which we will set to infinity or None to indicate we havent found any path to this node yet.

We then add the start node to a priority queue with the distance as priority. 

While the queue is not empty, we pop a node from the queue. (If the node is the target we can stop here)

For each of the node's neighbors we calculate a new distance value for the neighbor coming from the current node.
If that distance is lesser than what we already have for the neighbor, update the distance map and set the predecessor of the neighbor to the current node.

When we are out of nodes in the PriorityQueue or if we found the target, we return the prev and dist maps or we build the path from target to the source node using the prev map.

##### Compared to other search algorithms

  - Best-First Search is an informed algorithm (Uses an heuristic), which expands the most promising node first.

  - Dijkstra is uninformed algorithm - it should be used when you have no knowledge on the graph, and cannot estimate the distance from each node to the target.

  - A* (which is a s best-first search) turns into Dijkstra's algorithm when you use heuristic function h(v)  = 0 for each v.
