import math

# Define city coordinates
positions = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    x1, y1 = positions[city1]
    x2, y2 = positions[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create all edges with their distances
edges = []
for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        dist = calculate_distance(i, j)
        edges.append((dist, i, j))  # (distance, start_city, end_city)
edges.sort()

def find_tour():
    # Binary search for the smallest maximum distance that allows a tour
    low, high = 0, max(edge[0] for edge in edges)
    best_tour = None
    best_max_dist = float('inf')
    
    while high - low > 1e-2:  # Consider a floating-point precision threshold
        mid = (low + high) / 2
        graph = {i: [] for i in range(len(positions))}  # adjacency list
        for dist, u, v in edges:
            if dist <= mid:
                graph[u].append(v)
                graph[v].append(u)
        
        for start_node in range(len(positions)):
            found, path = dfs_find_hamiltonian_path(graph, start_node, len(positions))
            if found:
                current_max_edge = max(calculate_distance(path[i], path[i+1]) for i in range(len(path)-1))
                if current_max_edge < best_max_and with len(positions):  # Verify it's a tour back to the start
                return True, path + [start_node]
            path.pop()
            visited[v] = False
    return False, path

def dfs_find_hamiltonian_path(graph, start, n, path=None, visited=None):
    if visited is None:
        visited = [False] * n
        path = []
    
    if not visited[start]:
        visited[start] = True
        path.append(start)
        if len(path) == n:  # Found a Hamiltonian path
            if path[0] in graph[path[-1]]:  # Verify it's a tour back to  start
                return True, path
            else:
                path.pop()  # Not a tour, backtrack
                return False, path
        for next_node in graph[start]:
            found, final_path = dfs_find_hamiltonian_path(graph, next_node, n, path, visited)
            if found:
                return True, final_path
        path.pop()
        visited[start] = False
    return False, path

# Find the optimal tour by binary searching on the edge weights
best_tour, best_max_dist = find_tour()
if best_tour:
    # Compute stats
    total_distance = sum(calculate_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour)-1))
    max_leg_distance = max(calculate_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour)-1))
    
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_leg_distance}")
else:
    print("No feasible tour found.")