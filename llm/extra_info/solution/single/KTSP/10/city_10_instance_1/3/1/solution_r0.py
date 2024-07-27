import itertools
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Given cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Compute combinations of visits excluding the depot
city_combinations = itertools.combinations([i for i in range(1, 10)], 4)  # Combinations of 4 cities plus the depot

min_tour_cost = float('inf')
best_tour = []

# Evaluate each combination of cities
for combination in city_combinations:
    full_tour = [0] + list(combination) + [0]  # Start and end at the depot
    all_permutations = itertools.permutations(full_tour[1:-1])  # Permute only the middle cities
    
    for perm in all_permutations:
        current_tour = [0] + list(perm) + [0]
        current_cost = 0
        
        for i in range(len(current_tour) - 1):
            current_cost += euclidean_distance(cities[current_tour[i]], cities[current_tour[i+1]])
        
        if current_cost < min_tour_cost:
            min_tour_cost = current_cost
            best_tour = current_tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(min_tour_cost, 2))