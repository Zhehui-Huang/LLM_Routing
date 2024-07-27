import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_route_distance(route, coordinates):
    return sum(euclidean_distance(coordinates[route[i]], coordinates[route[i + 1]]) for i in range(len(route) - 1))

def find_best_tours(coordinates, num_robots):
    n = len(coordinates)
    cities = list(range(1, n))
    min_cost = float('inf')
    best_routes = None

    # Checking all permutations would be infeasible for larger numbers of cities, but works in this instance
    for perm in permutations(cities):
        # Split cities into the number of robots
        parts = [perm[i::num_robots] for i in range(num_robots)]
        routes = [[0] + list(part) + [0] for part in parts]
        cost = sum(total_route_distance(route, coordinates) for route in routes)

        if cost < min_cost:
            min_cost = cost
            best_routes = routes

    return best_routes, min_cost

# Define the city coordinates
coordinates = [
    (145, 215), # Depot city 0
    (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232),
    (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), 
    (139, 182)
]

# Number of robots
num_robots = 4

# Get the best tours and the minimum cost
best_tours, overall_cost = find_best_tours(coordinates, num_robots)

# Print the results
for index, tour in enumerate(best_tours):
    tour_cost = total_route_distance(tour, coordinates)
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {tour_kind}")

print(f"Overall Total Travel Cost: {overall_cost}")