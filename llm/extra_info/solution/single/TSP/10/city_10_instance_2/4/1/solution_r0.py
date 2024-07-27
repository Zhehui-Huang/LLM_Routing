import math
from itertools import permutations

# Define the cities with their coordinates
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

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Evaluate the total cost of a specific tour
def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i+1])
    return total_distance

# Generate all possible tours starting and ending at the depot city 0
all_tours = permutations([i for i in range(1, 10)])
min_cost = float('inf')
best_tour = None

for perm in all_tours:
    current_tour = [0] + list(perm) + [0]
    current_cost = evaluate_tours(current_tour)
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = current_tour

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))