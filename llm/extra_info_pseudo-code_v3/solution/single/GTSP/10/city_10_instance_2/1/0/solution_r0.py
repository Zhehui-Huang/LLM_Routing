import math
import itertools

# Define the city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Define the groups of cities
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to calculate total tour cost
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all combinations for the cities from each group
all_combinations = itertools.product(*groups)
best_tour = None
best_cost = float('inf')

# Evaluate each combination
for combination in all_combinations:
    current_tour = [0] + list(combination) + [0]
    current_cost = tour_cost(current_tour)
    if current_cost < best_cost:
        best_cost = current_cost
        best_tour = current_tour

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", best_cost)