import itertools
import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def total_tour_cost(cities, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

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
    [7, 9],  # Group 0
    [1, 3],  # Group 1
    [4, 6],  # Group 2
    [8],     # Group 3
    [5],     # Group 4
    [2]      # Group 5
]

# Generate all possible tours considering one city from each group
all_possible_tours = list(itertools.product(*groups))

# Search for the shortest path tour
best_tour = None
min_cost = float('inf')

for possible_tour in all_possible_tours:
    tour_with_depot = [0] + list(possible_tour) + [0]
    cost = total_tour_cost(cities, tour_with_depot)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour_with_depot

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")