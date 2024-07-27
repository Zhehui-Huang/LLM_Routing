import math
import itertools

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Calculate the distance between every pair of cities
num_cities = len(cities)
dist_matrix = [[distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Sorting edges by distance
edges = sorted([(dist_matrix[i][j], i, j) for i in range(num_cities) for j in range(i+1, num_cities)])

def is_hamiltonian_cycle_exist(bottleneck, path=None):
    from collections import deque
    # Starting from the depot city
    path_queue = deque([(0, [0]) if not path else path])
    visited = set()
    
    while pathQueue:
        current_city, current_path = path_queue.popleft()
        if len(current_path) == num_cities:
            if dist_matrix[current_city][0] <= bottleneck:  # Close the loop back to depot
                return True, current_path + [0]
            continue
        
        for next_city in range(num_cities):
            if next_city not in current_path and dist_matrix[current_city][next_city] <= bottleneck:
                if next_city in visited:
                    continue
                visited.add(next_city)
                if is_hamiltonian_cycle_exist(bottleneck, (next_city, current_path + [next_city])):
                    return True, current_path + [next_city]
                visited.remove(next_city)
    return False, []

# Apply the bottleneck TSP algorithm
for edge_weight, u, v in edges:
    exists, path = is_hamiltonian_cycle_exist(edge_weight)
    if exists:
        max_edge_weight = max(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
        total_travel_cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
        print(f"Tour: {path}")
        print(f"Total travel cost: {total_travel_qweight}")
        print(f"Maximum distance between consecutive cities: {max_edge_dist}")
        break