import itertools
import math

# City coordinates
cities = {
    0: (84, 67),  # Depot
    1: (74, 40),  # Group 1
    2: (71, 13),  # Group 5
    3: (74, 82),  # Group 1
    4: (97, 28),  # Group 2
    5: (0, 31),   # Group 4
    6: (8, 62),   # Group 2
    7: (74, 56),  # Group 0
    8: (85, 71),  # Group 3
    9: (6, 76)    # Group 0
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

def euclidean_distance(c1, c2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_cost(tour):
    """ Calculate total cost of a given tour including return to depot """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    # Closing the tour by returning to the depot
    total_cost += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return total_cost

# Generate all combinations of cities, one from each group
all_combinations = list(itertools.product(*groups))

# Initialize minimum tour details
minimum_tour_cost = float('inf')
minimum_tour = None

# Evaluate each combination
for combination in all_combinations:
    tour = [0] + list(combination) + [0]
    tour_cost = calculate_tour_cost(tour)
    if tour_cost < minimum_tour_cost:
        minimum_tour_cost = tour_cost
        minimum_tour = tour

# Print the best tour and its cost
print("Tour:", minimum_tour)
print("Total travel cost:", minimum_tour_cost)