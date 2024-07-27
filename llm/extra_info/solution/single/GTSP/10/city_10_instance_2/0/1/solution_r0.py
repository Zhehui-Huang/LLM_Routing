import itertools
import math

# Define city coordinates
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

# Define groups of cities
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
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all combinations of cities visiting exactly one from each group
candidate_tours = itertools.product(*groups)

# Evaluate each tour to find the one with the minimum cost
min_cost = float('inf')
best_tour = None

for tour in candidate_tours:
    # Include the depot at the beginning and the end of the tour
    full_tour = [0] + list(tour) + [0]
    
    # Calculate the tour cost
    tour_cost = sum(distance(full_tour[i], full_tour[i + 1]) for i in range(len(full_tour) - 1))
    
    # Keep track of the minimal tour
    if tour_cost < min_cost:
        min_cost = tour_cost
        best_tour = full_tour

# Output the best tour and the corresponding total cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)