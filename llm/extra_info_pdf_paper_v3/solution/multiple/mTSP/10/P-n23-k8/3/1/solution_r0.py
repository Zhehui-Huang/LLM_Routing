import math
from itertools import permutations

# City coordinates (ID and Cartesian coordinates)
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Implementing 2-opt swap to minimize route distance
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]
                if cost(new_route) < cost(best):
                    best = new_simulated_annealing_route
                    improved = True
        route = best
    return best

# Compute cost of a route
def cost(route):
    return sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1))

# Allocate initial routes to robots in a round-robin fashion
robots = {i: [] for i in range(8)}
cities_list = list(cities.keys())[1:]  # Exclude the depot city for allocation

for i, city in enumerate(cities_list):
    robots[i % 8].append(city)

# Initial touещrs
tours = {r: [0] + robots[r] + [0] for r in robots}

# Optimize each tour using 2-opt 
optimized_tours = {r: two_opt(tours[r]) for r in robots}

# Calculate and output results
total_cost = 0

for r, tour in optimized_tours.items():
    tour_cost = cost(tour)
    total_cost += tour_cost
    print(f"Robot {r} Tour: {tour}")
    print(f"Robot {r} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")