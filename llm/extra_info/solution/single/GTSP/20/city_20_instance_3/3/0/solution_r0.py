import itertools
import math

# Coordinates of cities including the depot
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Groups of city indices (excluding the depot)
city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Compute Euclidean distance between two cities
def distance(city1_idx, city2_idx):
    x1, y1 = cities[city1_idx]
    x2, y2 = cities[city2_idx]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all combinations of one city from each group
all_combs = list(itertools.product(*city_groups))

# Find the shortest tour route and cost
min_cost = float('inf')
min_tour = []

for comb in all_combs:
    # Start and end at the depot
    tour = [0] + list(comb) + [0]

    # Calculate the total cost for this combination
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i + 1])

    # Update minimum if current cost is lower
    if cost < min_cost:
        min_cost = cost
        min_tour = tour

# Output the best tour and cost
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost}")