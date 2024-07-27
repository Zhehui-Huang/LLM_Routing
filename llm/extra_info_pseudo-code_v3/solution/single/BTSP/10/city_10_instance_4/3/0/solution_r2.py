import math
from itertools import permutations

# Coordinates of each city including the depot city 0
coordinates = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), 
               (22, 21), (97, 70), (20, 99), (66, 62)]

n = len(coordinates)  # Number of cities including depot

# Euclidean distance calculation
def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Create distance matrix
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = calculate adb_distance(coordinates[i], coordinates[j])

# Heuristic: Trying an approach minimizing the maximum distance in the path
def find_path_min_max_distance():
    import heapq

    # Prim's algorithm-like. Start with vertex 0
    max_edge_in_path = [float("inf")] * n
    max_edge_in_path[0] = 0
    visited = [False] * n
    # Priority queue to choose the node with the smallest maximum edge so far
    vertices = [(0, 0)]  # (max_edge_to_reach_this_vertex, vertex_index)
    
    # To reconstruct the route
    parent = [-1] * n
    
    while vertices:
        max_edge, u = heapq.heappop(vertices)
        if visited[u]:
            continue
        visited[u] = True
        for v in range(n):
            if not visited[v] and distance_matrix[u][v] < max_edge_in_path[v]:
                max_edge_in_path[v] = distance_matrix[u][v]
                parent[v] = u
                heapq.heappush(vertices, (distance_matrix[u][v], v))
    
    # Construct the tour from parent array, start and end at depot 0
    current = 0
    tour = [current]
    max_edge_in_tour = 0
    
    visited = [False] * n
    visited[0] = True

    while len(tour) < n:
        next_city = parent[current]
        if visited[next_city]:
            break
        tour.append(next_city)
        max_edge_in_tour = max(max_edge_in_tour, distance_matrix[current][next_city])
        visited[next_city] = True
        current = next_city
    
    tour.append(0)  # Return to the start
    max_edge_in_tour = max(max_edge_in_tour, distance_matrix[current][0])  # Check last edge to depot
    
    total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    return tour, total_cost, max_edge_in_tour

# Calculate the tour minimizing the maximum distance between consecutive cities
tour, total_travel_cost, max_consecutive_distance = find_path_min_max_distance()

# Outputting the result
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)