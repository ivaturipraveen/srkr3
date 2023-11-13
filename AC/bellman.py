def bellman_ford(graph, num_vertices, source):
    distance = [float('inf')] * num_vertices
    distance[source] = 0

    for _ in range(num_vertices - 1):
        for edge in graph:
            u, v, w = edge
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Check for negative cycles
    for edge in graph:
        u, v, w = edge
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            print("Graph contains a negative cycle")
            return

    # Print the shortest distances
    print(f"Shortest distances from source {source}:")
    for i in range(num_vertices):
        print(f"Vertex {i}: {distance[i]}")

# Example usage:
graph = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 3, 3)]
num_vertices = 4
source = 0

bellman_ford(graph, num_vertices, source)
