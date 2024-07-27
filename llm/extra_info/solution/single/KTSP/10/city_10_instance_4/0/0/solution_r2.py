import itertools
import math

# Given city coordinates
cities = {
    0: (79, 15), 
    1: (79, 55), 
    2: (4, 80), 
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to find the total distance of the tour
def compute_tour_cost(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i + 1])
    total_distance += distance(tour[-1], tour[0])
    return total_distance

# Brute-force all possible combinations of 7 other cities
all_combinations = itertools.combinations(range(1, 10), 7)
min_cost = float('inf')
best_tour = None

for cities_subset in all_combinations:
    # Always start and end at the depot city 0
    current_tour = [0] + list(cities_subset) + [0]
    
    # Get all permutations of the current cities_subset
    for perm in itertools.permutations(cities_subset):
        perm_tour = [0] + list(perm) + [0]
        current_cost = compute_tour_cost(perm_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = perm_tour

# Print the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)