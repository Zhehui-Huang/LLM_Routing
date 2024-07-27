import math
import itertools

# Given data
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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible combinations of visiting 7 cities among the given 9 cities (excluding depot city 0)
all_combinations = itertools.combinations(range(1, 10), 7)

best_tour = None
min_distance = float('inf')

# Evaluate routes through combinations
for combination in all_combinations:
    # Always start and end at depot city 0
    potential_tour = [0] + list(combination) + [0]
    
    # Generate and evaluate all possible permutations for this set of cities
    for perm in itertools.permutations(potential_tour[1:-1]):
        tour = [0] + list(perm) + [0]
        # Calculate tour cost
        tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Compare to find the shortest tour
        if tour_cost < min_distance:
            min_distance = tour_cost
            best_tour = tour

# Output results with the best tour found
print("Tour:", best_tour)
print("Total travel cost: {:.2f}".format(min_distance))