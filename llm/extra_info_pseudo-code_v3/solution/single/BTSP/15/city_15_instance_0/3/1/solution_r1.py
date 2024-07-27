import math
from itertools import permutations

# Given cities and their coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all pairs of cities and sort them by distance
edges = [(i, j, euclidean_distance(i, j)) for i in cities for j in cities if i != j]
edges.sort(key=lambda x: x[2])  # sort by distance

def is_hamiltonian_cycle(path):
    # Check if the path forms a Hamiltonian cycle starting and ending at the depot
    visited = set(path)
    return len(visited) == len(cities) and path[0] == 0 and path[-1] == 0

# Function to search for a Hamiltonian path that minimizes the maximum edge length
def find_optimal_tour():
    for weight in set(edge[2] for edge in edges):
        allowed_edges = [(i, j) for i, j, w in edges if w <= weight]
        for perm in permutations(range(1, len(cities))):  # permutate all except the depot
            path = [0] + list(perm) + [0]
            valid = all((path[i], path[i+1]) in allowed_edges or (path[i+1], path[i]) in allowed_edges for i in range(len(path) - 1))
            if valid:
                total_cost = sum(euclidean_distance(path[i], path[i+1]) for i in range(len(path) - 1))
                max_distance = max(euclidean_distance(path[i], path[i+1]) for i in range(len(path) - 1))
                return path, total_cost, max_distance
    return None  # If no valid path is found

# Running the bottleneck TSP solver
result = find_optimal_tour()
if result:
    path, total_cost, max_distance = result
    print("Tour:", path)
    print("Total travel cost:", round(total_cost, 2))
    print("Maximum distance between consecutive cities:", round(max_distance, 2))
else:
    print("No valid tour found.")