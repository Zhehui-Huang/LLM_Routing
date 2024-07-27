import itertools
import math

# City coordinates including the depot city
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

# Groups of cities. Each list indicates a group of city indices
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities given their indices."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_tour_cost(tour):
    """Calculate the total cost of a given tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Generate all combinations of cities, taking one city from each group
all_combinations = list(itertools.product(*groups))

# Find the best tour and minimal cost
best_tour = None
min_cost = float('inf')

for comb in all_combinations:
    # Always starting and ending at the depot city 0
    tour = [0] + list(comb) + [0]
    cost = calculate_tour_cost(tour)
    
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best found tour and its total cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))