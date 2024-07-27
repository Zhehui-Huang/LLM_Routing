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

# Calculating Euclidean Distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute the tour cost
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Generate all combinations of 7 cities (excl. depot), to select 7 additional cities to visit
city_indices = list(range(1, 10))
combinations = itertools.combinations(city_indices, 7)

best_tour = None
min_cost = float('inf')

for combination in combinations:
    # Adding depot city at start and end
    full_tour = [0] + list(combination) + [0]
    
    # Generate all permutations of the selected cities' orders
    permutations = itertools.permutations(list(combination))
    
    for perm in permutations:
        current_tour = [0] + list(perm) + [0]
        current_cost = tour_cost(current_tour)
        
        # Check if we have found a new shorter tour
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Outputting the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")