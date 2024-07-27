import numpy as np
from scipy.spatial.distance import euclidean

# Coordinates and other setup related to cities
city_coords = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate distances between each pair of cities
def calc_distances(coords):
    num_cities = len(coords)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean(coords[i], coords[j])
            else:
                distances[i][j] = float('inf')  # Represent infinity where no self loops are allowed
    return distances

# Testing for a Hamiltonian cycle existence in Bottleneck Graph
def hamiltonian_path_exists(edges, num_cities, start_city):
    from queue import Queue

    # Create graph
    graph = {i: [] for i in range(num_cities)}
    for (u, v) in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS to check if a path exists visiting all vertices
    visited = [False] * num_cities
    q = Queue()
    q.put(start_city)
    visited[start_city] = True
    count = 1
    
    while not q.empty():
        node = q.get()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.put(neighbor)
                count += 1
                
    return count == num_cities

# Bottleneck TSP Solver
def bottleneck_tsp(distances):
    num_cities = len(distances)
    edges_with_weights = sorted(((i, j, distances[i][j]) for i in range(num_cities) for j in range(i+1, num_cities)), key=lambda x: x[2])
    
    # Binary search to determine the smallest maximum edge
    left, right = 0, len(edges_with_weights) - 1
    best_path, min_max_edge = None, float('inf')
    
    while left <= right:
        mid = (left + right) // 2
        max_edge = edges_with_weights[mid][2]
        edges = [(i, j) for (i, j, w) in edges_with_weights if w <= max_edge]
        
        if hamiltonian_path_exists(edges, num_cities, 0):
            right = mid - 1
            best_path = edges  # this is not the exact path, just the possible edges collection at this stage
            min_max_edge = max_edge
        else:
            left = mid + 1
            
    return best_path, min_max_edge

distances = calc_distances(city_coords)
edges, max_dist = bottleneck_tsp(distances)
print(f"Possible edges in the tour with minimized bottleneck distance: {edges}")
print(f"Maximum distance between any two consecutive cities in the tour: {max_dist}")