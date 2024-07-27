import math
from itertools import product, permutations

# City coordinates
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

# Function to calculate Euclidean distance between two cities
def distance(city1_index, city2_index):
    x1, y1 = cities[city1_index]
    x2, y2 = cities[city2_index]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all group city combinations: one city from each group
all_group_combinations = list(product(*groups))

# Find the shortest tour visiting each city group exactly once and returning to the depot
best_tour = None
minimum_cost = float('inf')

for group_combination in all_group_combinations:
    # Generate all permutations of the cities in the combination
    for perm in permutations(group_combination):
        # Create tour starting and ending at the depot (city 0)
        tour = (0,) + perm + (0,)
        
        # Calculate the tour cost
        tour_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        # Check if this tour is the best found so far
        if tour_cost < minimum_cost:
            best_tour = tour
            minimum_cost = tour_flow_tour

# Output the best tour and the total travel cost
print("Tour:", list(best_tour))
print("Total travel cost:", round(minimum_cost, 2))