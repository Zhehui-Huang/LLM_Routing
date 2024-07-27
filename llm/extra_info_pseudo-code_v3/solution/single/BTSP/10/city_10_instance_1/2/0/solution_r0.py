import math
import itertools

# Coordinates of each city
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 
    4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44), 
    8: (17, 69), 9: (95, 89)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create list of edges with their distances
edges = []
num_cities = len(cities)
for i in range(num_cities):
    for j in range(i+1, num_cities):
        dist = euclidean_distance(i, j)
        edges.append((dist, i, j))

# Sort edges based on distance
edges.sort()

# Function to find a Hamiltonian path in the bottleneck graph
def has_hamiltonian_path(threshold):
    # Create adjacency list for graph with edges below threshold
    graph = {i: [] for i in range(num_cities)}
    for dist, i, j in edges:
        if dist <= threshold:
            graph[i].append(j)
            graph[j].append(i)
        else:
            break
    
    # Check all permutations for a valid path starting and ending at 0
    for perm in itertools.permutations(range(1, num_cities)):
        valid = True
        path = [0] + list(perm) + [0]
        max_edge = 0
        
        for k in range(len(path) - 1):
            if path[k+1] not in graph[path[k]]:
                valid = False
                break
            max_edge = max(max_edge, euclidean_distance(path[k], path[k+1]))
        
        if valid and max_edge <= threshold:
            return True, path, max_edge
    return False, [], 0

# Main implementation of the Bottleneck TSP approximation
def solve_bottleneck_tsp():
    for dist, i, j in edges:
        found, path, max_edge_dist = has_hamiltonian_path(dist)
        if found:
            # Calculate total travel cost
            total_cost = sum(euclidean_distance(path[k], path[k+1]) for k in range(len(path) - 1))
            return f"Tour: {path}\nTotal travel cost: {total_cost:.2f}\nMaximum distance between consecutive cities: {max_edge_dist:.2f}"
            
    return "No Hamiltonian tour found."

# Solve the Bottleneck TSP
print(solve_bottleneck_tsp())