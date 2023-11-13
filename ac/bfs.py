from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbors):
        self.graph[vertex] = neighbors

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            current_vertex = queue.popleft()

            if current_vertex not in visited:
                visited.add(current_vertex)
                result.append(current_vertex)

                neighbors = self.graph.get(current_vertex, [])
                queue.extend(neighbor for neighbor in neighbors if neighbor not in visited)

        return result

# Example usage:
g = Graph()
g.add_edge(1, [2, 3])
g.add_edge(2, [4, 5])
g.add_edge(3, [])
g.add_edge(4, [])
g.add_edge(5, [])

start_vertex = 1
bfs_result = g.bfs(start_vertex)

print(f"BFS traversal starting from vertex {start_vertex}: {bfs_result}")
