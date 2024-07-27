from math import sqrt
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to find the shortest tour
def find_shortest_tour():
    best_tour = None
    min_cost = float('inf')

    # Generate all possible orders to visit the cities (excluding the depot)
    for perm in permutations(range(1, len(cities))):  # start from 1 to exclude the depot from permutations
        # Start and end at the depot city
        tour = [0] + list(perm) + [0]
        cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

        if cost < min_cost:
            min_cost = cost
            best_tour = tour

    return best_tour, min_cost

# Calculate the tour and cost
tour, total_cost = find_shortest_tour()

# Printing the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")