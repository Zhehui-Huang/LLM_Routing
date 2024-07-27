import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_distances(cities):
    n = len(cities)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            distances[i][j] = distances[j][i] = euclidean_distance(cities[i], cities[j])
    return distances

def find_tour(cities):
    n = len(cities)
    distances = calculate_distances(cities)
    best_tour = None
    best_max_edge = float('inf')
    best_total_cost = float('inf')
    
    # Generate all permutations of cities except the depot (city index 0)
    for perm in permutations(range(1, n)):  # permutation sans depot city 0
        tour = [0] + list(perm) + [0]
        max_edge = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        if max_edge < best_max_edge or (max_edge == best_max_edge and total_cost < best_total_cost):
            best_tour = tour
            best_max_edge = max_edge
            best_total_cost = total_cost
    
    return best_tour, best_total_cost, best_max_edge

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
    (78, 76), (68, 45), (50, 28), (69, 9)
]

# Get the optimal tour
tour, total_cost, max_distance = find_tour(cities)

# Print the results
print("Tour:", tour)
print("Total travel cost: {:.2f}".format(total_cost))
print("Maximum distance between consecutive cities: {:.2f}".format(max_distance))