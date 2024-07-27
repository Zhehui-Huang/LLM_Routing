import math
from itertools import product

# Coordinates of the cities
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

# Groups of cities
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all combinations of cities to visit, one from each group
all_combinations = product(*groups)

# Initialize the minimum distance to a very high number and no tour found initially
min_distance = float('inf')
best_tour = None

# Explore each combination
for comb in all_combinations:
    # Start at depot city 0
    tour = [0] + list(comb) + [0]
    tour_distance = 0
    
    # Calculate total distance of the tour
    for i in range(len(tour) - 1):
        tour_distance += distance(tour[i], tour[i + 1])
    
    # Compare and update the minimum distance and best tour
    if tour_distance < min_distance:
        min_distance = tour_distance
        best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(min_distance, 2))