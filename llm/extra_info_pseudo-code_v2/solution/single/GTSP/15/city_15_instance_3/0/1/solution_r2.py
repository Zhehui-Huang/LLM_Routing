import itertools
import math

# Coordinates of the depot and cities
coordinates = [
    (16, 90),  # City 0: Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# City groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def tour_cost(tour):
    """Calculate the total cost of a given tour."""
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def find_optimal_tour():
    """Find the shortest tour that visits one city from each group, starting and ending at the depot."""
    all_group_combinations = itertools.product(*city_groups)
    best_tour = None
    lowest_cost = float('inf')

    for combination in all_group_combinations:
        tour = [0] + list(combination) + [0]
        cost = tour_cost(tour)
        if cost < lowest_cost:
            lowest_cost = cost
            best_tour = tour

    return best_tour, lowest_cost

# Calculate and print the optimal tour and its cost
optimal_tour, optimal_cost = find_optimal_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)