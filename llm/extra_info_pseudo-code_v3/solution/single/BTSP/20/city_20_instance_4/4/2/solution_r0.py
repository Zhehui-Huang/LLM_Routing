import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def is_hamiltonian_path(edges, num_vertices):
    # Using a simple heuristic based on permutations to find a valid path for small graphs.
    for perm in permutations(range(1, num_vertices)):
        path = [0] + list(perm) + [0]
        valid = True
        for i in range(len(path) - 1):
            if (path[i], path[i+1]) not in edges and (path[i+1], path[i]) not in edges:
                valid = False
                break
        if valid:
            return path
    return None

def bottleneck_tsp(cities):
    num_vertices = len(cities)
    distances = {}
    
    # Calculate distances between all pairs of cities
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            distance = calculate_distance(cities[i], cities[j])
            distances[(i, j)] = distance
    
    # Sort distances based on the bottleneck value
    sorted_distances = sorted(distances.items(), key=lambda item: item[1])
    
    # Finding the minimum bottleneck value that contains a Hamiltonian cycle
    for weight_index, (pair, weight) in enumerate(sorted_distances):
        # Creating a graph with edges of weight less than or equal to the current weight
        edges = {(i, j) for (i, j), dist in distances.items() if dist <= weight}
        
        # Check if there's a Hamiltonian path in the current graph
        path = is_hamiltonian_path(edges, num_vertices)
        if path:
            max_edge_weight = max(
                calculate_distance(cities[path[i]], cities[path[i+1]]) 
                for i in range(len(path) - 1)
            )
            total_cost = sum(
                calculate_distance(cities[path[i]], cities[path[i+1]]) 
                for i in range(len(path) - 1)
            )
            return path, total_cost, max_edge_weight

# Input cities as coordinate pairs
cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
          (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
          (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

# Solve the BTSP problem
tour, total_cost, max_dist = bottleneck_tsp(cities)

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
tierest.
print(f"Maximum distance between consecutive cities: {max_dist}")