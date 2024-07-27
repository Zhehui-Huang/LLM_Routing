import itertools
import math

# City coordinates with their index
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def calculate_distance(city1, city2):
    coord1 = cities[city1]
    coord2 = cities[city2]
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)

# Get all possible combinations of visiting 11 cities (excluding the depot)
combinations = list(itertools.combinations(cities.keys() - {0}, 11))

min_cost = float('inf')
best_tour = None

for combination in combinations:
    # Include the depot city at the start and the end
    routes = itertools.permutations(combination)

    for route in routes:
        # Add the start and end city (depot)
        full_route = [0] + list(route) + [0]

        # Calculate the cost of this full route
        tour_cost = sum(calculate_distance(full_route[i], full_route[i+1]) for i in range(len(full_route)-1))

        # Check if this tour has a lower cost than the current best
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = full_route

print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")