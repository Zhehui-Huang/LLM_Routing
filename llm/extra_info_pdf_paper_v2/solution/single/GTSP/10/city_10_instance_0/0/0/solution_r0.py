import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities coordinates
cities = {
    0: (50, 42), # Depot
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# City groups
city_groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Calculating all possible group combinations, one city from each group
combinations = list(itertools.product(*city_groups))

def total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

# Tour and cost calculation
best_tour = None
min_cost = float('inf')

for combo in combinations:
    # Create a tour for the combination starting and ending at the depot
    tour = [0] + list(combo) + [0]
    cost = total_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))