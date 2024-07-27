import math
from itertools import permutations

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

# Generate all combinations of one city per group
all_group_combinations = list(product(*groups))

# Find the shortest tour through all combinations
best_tour = None
minimum_cost = float('inf')

for comb in all_group_combinations:
    # Generate all permutations of chosen cities in combination to optimize the order
    for permutation in permutations(comb):
        # Complete tour from and back to the depot city
        tour = (0,) + permutation + (0,)
        
        # Calculate total tour cost
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += distance(tour[i], tour[i + 1])
        
        # Update the best tour and cost if the current one is better
        if total_cost < minimum_cost:
            best_tour = tour
            minimum_cost = total_cost

# Output the best found tour and the total travel cost
print("Tour:", list(best_tour))
print("Total travel cost:", round(minimum_cost, 2))