import math
from itertools import product

# Coordinates of the cities
coordinates = {
    0: (50, 42),
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
groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible tours from the depot to exactly one city in each group and back to the depot
def generate_tours():
    possible_tours = []
    group_product = product(groups[0], groups[1], groups[2])
    for perm in group_product:
        # always start and end at the depot city 0
        tour = [0] + list(perm) + [0]
        possible_tours.append(tour)
    return possible_tours

# Computing the travel cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total,.
        cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Finding the shortest tour
def find_shortest_tour():
    all_tours = generate_tours()
    min_cost = float('inf')
    min_cost_tour = None
    for tour in all_tours:
        cost = tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            min_cost_tour = tour
    return min_cost_tour, min_cost

# Main execution
shortest_tour, minimum_cost = find_shortest_tour()
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {minimum_cost:.2f}")