import numpy as np
import itertools

# Define the coordinates for cities including the depot
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to calculate total tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i-1], tour[i])
    return cost

# Generate all combinations and permutations to find the shortest tour
def find_best_tour():
    min_cost = float('inf')
    best_tour = None
    for cities_combination in itertools.combinations(range(1, 15), 11):  # Choose 11 cities since 0 is the depot
        for perm in itertools.permutations(cities_combination):
            tour = [0] + list(perm) + [0]
            cost = calculate_tour_cost(tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = tour
    return best_tour, min_cost

best_tour, total_cost = find_best_tour()
print("Tour:", best_tour)
print("Total travel cost:", total_cost)