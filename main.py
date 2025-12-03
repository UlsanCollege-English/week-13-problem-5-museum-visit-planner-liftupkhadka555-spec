from collections import deque

def shortest_path(rooms, doors, start, goal):
    # If start or goal are not in rooms → no path
    if start not in rooms or goal not in rooms:
        return []

    # Special case: same room
    if start == goal:
        # If the room exists, return it
        return [start] if start in rooms else []

    # Build adjacency list (undirected)
    graph = {room: [] for room in rooms}
    for a, b in doors:
        if a in graph and b in graph:
            graph[a].append(b)
            graph[b].append(a)

    # BFS setup
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    # BFS traversal
    while queue:
        current = queue.popleft()

        # If we reached the goal → reconstruct path
        if current == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]  # reverse

        # Continue exploring neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # No path found
    return []