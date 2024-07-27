from itertools import product
from math import sqrt

# Define the cities and their coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Grouping cities
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Compute the distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible tours
def generate_tours():
    for perm in product(*groups):
        yield (0,) + perm + (0,)

# Calculate the total cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Find the shortest tour
def find_shortest_tour():
    best_tour = None
    min_cost = float('inf')
    for tour in generate_tours():
        cost = tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

# Main execution
shortest_tour, total_cost = find_shortest_tour()
print(f"Tour: {list(shortest_tour)}")
print(f"Total travel cost: {total_cost:.2f}")