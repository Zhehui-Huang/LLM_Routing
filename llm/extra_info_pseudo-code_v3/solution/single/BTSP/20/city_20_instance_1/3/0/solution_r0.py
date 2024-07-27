import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_hamiltonian_path(G, cities, max_distance):
    for perm in permutations(cities):
        valid = True
        max_edge = 0
        for i in range(len(perm) - 1):
            if G[perm[i]][perm[i + 1]] > max_distance:
                valid = False
                break
            max_edge = max(max_edge, G[perm[i]][perm[i + 1]])
        if valid:
            full_tour = [0] + list(perm) + [0]
            total_cost = sum(G[full_tour[i]][full_tour[i + 1]] for i in range(len(full_tour) - 1))
            return True, full_tour, max_edge, total_cost
    return False, [], 0, 0

def bottleneck_tsp(cities):
    # Calculate distances
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])

    sorted_distances = sorted(set(distances[i][j] for i in range(num_cities) for j in range(num_cities) if i != j))
    
    # Attempt to find Hamiltonian path under increasing thresholds
    for distance in sorted_distances:
        exists, tour, max_edge, total_cost = check_hamiltonian_path(distances, list(range(1, num_cities)), distance)
        if exists:
            return tour, total_cost, max_edge

    return [], 0, 0

# Cities (x, y) coordinates
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
          (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
          (78, 76), (68, 45), (50, 28), (69, 9)]

# Solve the BTSP
tour, total_cost, max_distance = bottleneck_tsp(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")