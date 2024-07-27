import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Groups of cities
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Calculate all possible ways to pick one city per group
all_combinations = list(itertools.product(*groups))

# Storage for the shortest tour found
best_tour = None
min_cost = float('inf')

# Evaluate each possible combination
for combination in all_combinations:
    current_tour = [0] + list(combination) + [0]  # Start and end at the depot
    current_cost = 0
    
    # Calculate total distance of the current tour
    for i in range(len(current_tour) - 1):
        current_cost += euclidean_distance(cities[current_tour[i]], cities[current_tour[i+1]])
    
    # Update best tour if the current one is shorter
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = current_tour

print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))