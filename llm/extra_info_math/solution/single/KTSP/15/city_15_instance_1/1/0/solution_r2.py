import math
from itertools import permutations, combinations

# Coordinates of the cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def distance(city1, city2):
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

def find_best_tour():
    best_tour = None
    best_cost = float('inf')
    # Generate all 6-city combinations that include the depot city (0)
    available_cities = list(cities.keys())
    available_cities.remove(0)
    for combination in combinations(available_cities, 5):  # choose 5 additional cities
        current_combination = [0] + list(combination)
        # Generate all permutations for the chosen cities
        for perm in permutations(current_combination):
            if perm[0] == 0:  # Make sure the tour starts at the depot city
                tour = list(perm) + [0]  # Close the tour by returning to the depot
                cost = calculate_cost(tour)
                if cost < best_cost:
                    best_tour = tour
                    best_cost = cost
    return best_tour, best_cost

# Finding the shortest possible tour starting and ending at the depot
best_tour, best_cost = find_best_tour()

# Output that will be produced
print("Tour:", best_tour)
print("Total travel cost:", best_cost)