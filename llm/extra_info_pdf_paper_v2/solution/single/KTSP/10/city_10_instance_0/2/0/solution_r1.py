from itertools import combinations, permutations
import math

# Coordinate data of the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to evaluate the total tour cost
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

# Function to find the optimal tour visiting 4 different cities including the depot
def find_optimal_tour():
    all_cities = list(cities.keys())
    min_cost = float('inf')
    best_tour = None

    # Generate all combinations of 3 additional cities to join with depot
    for city_combo in combinations(all_cities[1:], 3):
        # Generate all permutations of the chosen cities, including starting and returning to the depot
        for perm in permutations(city_combo):
            current_tour = [0] + list(perm) + [0]
            current_cost = tour_cost(current_tour)
            if current_cost < min_cost:
                min_cost = current_cost
                best_tour = current_tour

    return best_tour, min_cost

# Getting the best possible tour and its cost
optimal_tour, optimal_cost = find_optimal_tour()

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")