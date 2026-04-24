from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])
    explored = []

    while queue:
        node, path = queue.popleft()
        explored.append(node)

        if node == goal:
            return path, explored

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, explored