import itertools
import math

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Find the shortest tour
def find_shortest_tour():
    best_tour = None
    min_cost = float('inf')
    for perm in itertools.permutations(range(1, 15)):
        tour = [0] + list(perm) + [0]
        cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

# Find and display the best tour and its total cost
best_tour, best_tour_cost = find_shortest_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tard_tour_cost}")