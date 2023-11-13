def dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(start)
    result.append(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)

    return result

# Example usage:
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

start_vertex = 1
dfs_result = dfs(graph, start_vertex)

print(f"DFS traversal starting from vertex {start_vertex}: {dfs_result}")
