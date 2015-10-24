# https://en.wikipedia.org/wiki/Depth-first_search
graph = {'A': set(['B', 'C', 'E']),
         'B': set(['A', 'D', 'F']),
         'C': set(['A', 'G']),
         'D': set(['B']),
         'E': set(['A', 'F']),
         'F': set(['B', 'E']),
         'G': set(['C'])}

def dfs(graph, start):
    marked = set()
    stack = [start]
    while stack:
        top = stack.pop()
        if top not in marked:
            marked.add(top)
            for v in graph[top]:
                stack.append(v)
    return marked

print dfs(graph, 'A')
