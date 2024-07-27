import itertools
import math

# Define the coordinates of the cities
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Define the city groups
groups = [
    [7, 9], [1, 3], [4, 6], [8], [5], [2]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible city selections from each group
all_city_combinations = list(itertools.product(*groups))

# Brute-force attempt to find the minimum tour
min_tour_cost = float('inf')
best_tour = []

for city_set in all_city_combinations:
    # We create all permutations for the selected cities from each group plus the depot
    for perm in itertools.permutations(city_set):
        # Calculate tour cost from depot to each city permutation and back to depot
        tour = [0] + list(perm) + [0]
        tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
            best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(min_tour_cost, 2))