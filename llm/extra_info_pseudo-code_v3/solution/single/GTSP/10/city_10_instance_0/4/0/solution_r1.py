import math
from itertools import product

# Cities and their coordinates
cities = {
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
city_groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    x1, y1 = city_a
    x2, y2 = city_b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generating all possible tours
def generate_tours():
    shortest_tour = None
    minimum_cost = float('inf')

    # Generate all combinations where one city is taken from each group
    for combination in product(*city_groups):
        # Prepend and append the depot city (0)
        tour = [0] + list(combination) + [0]
        total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

        if total_cost < minimum_cost:
            minimum_cost = total_cost
            shortest_tour = tour

    return shortest_tour, minimum_cost

# Solving the problem
shortest_tour, total_cost = generate_tours()
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_cost}")