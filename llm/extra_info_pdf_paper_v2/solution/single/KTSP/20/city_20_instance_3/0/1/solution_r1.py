import math
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i+1]]
    return total_distance

def initialize_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            distance = euclidean_distance(cities[i], cities[j])
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance
    return distance_matrix

def gvns(cities, k, max_iters=1000):
    n = len(cities)
    distance_matrix = initialize_distance_matrix(cities)
    # Initial tour generation (random)
    city_indices = list(range(n))
    best_tour = [0] + random.sample(city_indices[1:], k-1) + [0]
    best_cost = calculate_total_distance(best_tour, distance_matrix)

    for _ in range(max_iters):
        # Local search with swap and reinsertion
        for i in range(1, k):
            for j in range(i+1, k):
                new_tour = best_tour[:]
                # Swap two cities
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = calculate_total_distance(new_tour, distance_matrix)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour, new_cost
    return best_tour, best_cost

# Define cities coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Solve k-TSP with k = 13 (including the depot)
tour, total_cost = gvns(cities, 13)

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))