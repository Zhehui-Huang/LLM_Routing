import math
import numpy as np
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_costs(cities):
    num_cities = len(cities)
    costs = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                costs[i][j] = euclidean_distance(cities[i], cities[j])
    return costs

def is_valid_tour(costs, tour, max_edge_weight):
    max_edge_cost = max(costs[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return max_edge_cost <= max_edge_weight

def find_bottleneck_tour(cities):
    num_cities = len(cities)
    costs = calculate_costs(cities)
    edges = [(i, j, costs[i][j]) for i in range(num_cities) for j in range(i + 1, num_cities)]
    edges_sorted = sorted(edges, key=lambda x: x[2])

    # Try building the tour from the lowest max edge cost and upwards
    for max_edge_weight, _ in enumerate(edges_sorted):
        for perm in permutations(range(1, num_cities)):
            tour = [0] + list(perm) + [0]
            if is_valid_tour(costs, tour, edges_sorted[max_edge_weight][2]):
                return tour, sum(costs[tour[i]][tour[i+1]] for i in range(len(tour) - 1)), edges_sorted[max_edge_weight][2]

    return None

# Define the coordinates of each city
cities = [
    (29, 51), # Depot city
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

tour, total_cost, max_distance = find_bottleneck_tour(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)