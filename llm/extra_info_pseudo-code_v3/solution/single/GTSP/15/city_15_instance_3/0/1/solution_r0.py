import itertools
import math

# City data
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 80)
}

# Group data
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Euclidean distance calculation
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all combinations of one city from each group
group_combinations = list(itertools.product(*groups))

# Function to compute total tour cost for a specific city order
def tour_cost(tour):
    total_cost = calc_distance(0, tour[0])  # Distance from depot to first city
    for i in range(len(tour) - 1):
        total_cost += calc_distance(tour[i], tour[i + 1])
    total_cost += calc_distance(tour[-1], 0)  # Return to depot
    return total_cost

# Find the best tour
min_cost = float('inf')
best_tour = None

for group_choice in group_combinations:
    perms = itertools.permutations(group_choice)
    for perm in perms:
        cost = tour_cost(perm)
        if cost < min_cost:
            min_cost = cost
            best_tour = perm

# Include the depot in the output
final_tour = [0] + list(best_tour) + [0]

print("Tour:", final_tour)
print("Total travel cost:", min_cost)