import math
from itertools import product

# City coordinates
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

# Groups of cities
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generating all combinations of selecting one city from each group
all_combinations = list(product(*groups))

# Function to calculate the total travel cost of the tour
def calculate_tour_cost(tour):
    total_cost = euclidean_distance(0, tour[0])  # from depot to first city
    for i in range(1, len(tour)):
        total  += euclidean_distance(tour[i-1], tour[i])
    total_cost += euclidean_distance(tour[-1], 0)  # from last city back to depot
    return total_cost

# Finding the shortest tour
shortest_tour = None
min_cost = float('inf')

for combination in all_combinations:
    tour = [0] + list(combination) + [0]
    cost = calculate_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        shortest_tour = tour

# Output results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {min_cost}")