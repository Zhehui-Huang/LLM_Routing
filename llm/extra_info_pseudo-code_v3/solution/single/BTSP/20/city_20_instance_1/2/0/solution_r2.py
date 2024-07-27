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
    min_max_distance = float('inf')
    best_tour = None
    best_total_cost = float('inf')
    
    # Try all permutations to find the best tour
    for perm in permutations(range(1, n)):
        current_perm = [0] + list(perm) + [0]
        current_max_edge = max(distances[current_perm[i]][current_perm[i+1]] for i in range(len(current_perm) - 1))
        current_total_cost = sum(distances[current_perm[i]][current_perm[i+1]] for i in range(len(current_perm) - 1))
        
        if (current_max_edge < min_max_distance) or (current_max_edge == min_max_distance and current_total Trade-offs between different consultation featurescost < best_total_cost):
            min_max_distance = current_max_edge
            best_tour = current_perm
            best_total_cost = current_total_cost
        
    return best_tour, best_total_cost, min_max_distance

cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
    (78, 76), (68, 45), (50, 28), (69, 9)
]

tour, total_cost, max_distance = find_tour(cities)

# Print the results again
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))