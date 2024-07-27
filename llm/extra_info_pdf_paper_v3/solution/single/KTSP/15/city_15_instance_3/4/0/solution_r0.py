import itertools
import random
import math

# Coordinates of cities including the depot
coordinates = [
    (16, 90),   # Depot
    (43, 99),   # 1
    (80, 21),   # 2
    (86, 92),   # 3
    (54, 93),   # 4
    (34, 73),   # 5
    (6, 61),    # 6
    (86, 69),   # 7
    (30, 50),   # 8
    (35, 73),   # 9
    (42, 64),   # 10
    (64, 30),   # 11
    (70, 95),   # 12
    (29, 64),   # 13
    (32, 79)    # 14
]

def calculate_distance(city1, city2):
    # Euclidean distance between two cities
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def evaluate_tour(tour):
    # Calculates the total distance of the tour
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def find_best_tour():
    best_tour = None
    best_cost = float('inf')
    # Generate all combinations of 9 cities (excluding the depot)
    city_combinations = itertools.combinations(range(1, 15), 9)
    
    for cities in city_combinations:
        cities = [0] + list(cities)  # Always include depot in the tour
        # Try multiple permutations for each combination to find the best tour
        for _ in range(100):  # Multi-start approach
            random.shuffle(cities[1:])  # Shuffle only the cities, keeping depot at start
            tour = cities + [0]  # Return tour to depot
            cost = evaluate_tour(tour)
            if cost < best_cost:
                best_tour, best_cost = tour, cost

    return best_tour, best_cost

best_tour, best_cost = find_best_tour()
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))