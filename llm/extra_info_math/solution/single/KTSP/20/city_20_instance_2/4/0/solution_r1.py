import math
from itertools import combinations, permutations

# Define the cities with their coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49), 
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Evaluate the total travel cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Generate all combinations of 9 cities (excluding the depot)
city_combinations = list(combinations(range(1, 20), 9))
shortest_tour = None
minimum_cost = float('inf')

# Check every combination by adding the depot city and then finding all permutations of these 10 cities
for combination in city_combinations:
    full_tour = [0] + list(combination)
    for perm in permutations(full_tour):
        if perm[0] == 0 and perm[-1] == 0:
            current_cost = tour_cost(perm)
            if current_cost < minimum_cost:
                minimum_cost = current_cost
                shortest_tour = perm

# Output the results
print("Tour:", list(shortest_tour))
print("Total travel cost:", minimum_cost)