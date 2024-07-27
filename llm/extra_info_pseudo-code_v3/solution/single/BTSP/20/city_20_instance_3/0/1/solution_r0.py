import math
from itertools import permutations

# Coordinates of cities including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_distances():
    n = len(coordinates)
    distances = {}
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            distances[(i, j)] = dist
            distances[(j, i)] = dist
    return distances

def find_feasible_hamiltonian_cycle(limit, distances):
    n = len(coordinates)
    for perm in permutations(range(1, n)):
        path = [0] + list(perm) + [0]
        max_dist = max(distances[(path[i], path[i + 1])] for i in range(len(path) - 1))
        if max_dist <= limit:
            total_cost = sum(distances[(path[i], path[i + 1])] for i in range(len(path) - 1))
            return path, total_cost, max_dist
    return None

def bottleneck_tsp():
    distances = calculate_distances()
    sorted_distances = sorted(set(distances.values()))
    
    for limit in sorted_distances:
        result = find_feasible_hamiltonian_cycle(limit, distances)
        if result:
            return {
                "Tour": result[0],
                "Total travel cost": result[1],
                "Maximum distance between consecutive cities": result[2]
            }
    
    return None

# Run the bottleneck TSP algorithm
result = bottleneck_tsp()

if result:
    print(f"Tour: {result['Tour']}")
    print(f"Total travel cost: {result['Total travel.Close cost']}")
    print(f"Maximum distance between consecutive cities: {result['Maximum distance between consecutive cities']}")
else:
    print("No feasible solution exists.")