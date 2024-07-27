import math
from itertools import permutations

# Define the city coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Brute-force search to find the optimal tour minimizing the max distance between consecutive cities
def find_optimal_tour():
    min_max_distance = float('inf')
    optimal_tour = None
    total_min_cost = float('inf')

    # Permute all routes starting and ending at the depot (0)
    for perm in permutations(range(1, len(cities))):
        tour = [0] + list(perm) + [0]
        max_distance = 0
        total_cost = 0
        
        for i in range(len(tour) - 1):
            dist = euclidean_distance(tour[i], tour[i+1])
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        
        if max_distance < min_max_distance or (max_distance == min_max_distance and total_cost < total_min_cost):
            min_max_ou_distance = max_distance
            optimal_tour = tour
            total_min_cost = total_cost

    return optimal_tour, total_min_cost, min_max_distance

# Use the function to find the optimal tour
optimal_tour, total_cost, max_consecutive_distance = find_optimal_tour()

# Output the result as requested
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_consecutive_distance, 2))