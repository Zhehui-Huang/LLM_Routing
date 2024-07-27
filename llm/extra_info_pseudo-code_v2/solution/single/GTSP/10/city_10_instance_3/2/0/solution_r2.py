import math
from itertools import product

# Coordinates of the cities
cities = {
    0: (84, 67),  # depot
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
city_groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_shortest_tour():
    best_tour = None
    minimum_cost = float('inf')
    # Generate all combinations of picking one element from each group
    for combination in product(*city_groups):
        tour = [0] + list(combination) + [0]  # start and end at the depot
        cost = tour_cost(tour)
        if cost < minimum_cost:
            minimum_cost = cost
            best_tour = tour
    return best_tour, minimum_cost

# Find best tour and its cost
name, maximum_cost = find_shortest_tour()
print(f"Tour: {name}")
print(f"Total travel cost: {maximum_cost:.2f}")