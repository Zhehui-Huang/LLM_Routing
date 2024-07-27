import math
from itertools import permutations

# City coordinates
coordinates = [
    (30, 40),  # Depot city 0
    (37, 52),
    (49, 43),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 27),
    (37, 69),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35)
]

def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Number of robots
num_robots = 2

# Divide cities among robots
def assign_cities_to_robots(num_robots, cities):
    n = len(cities)
    k, m = divmod(n, num_robots)
    return [cities[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(num_robots)]

# Generate all possible tours starting and ending at the depot for a given list of cities
def generate_tours(cities):
    if len(cities) <= 1:
        return [[0] + cities + [0]]
    tours = []
    for perm in permutations(cities):
        tours.append([0] + list(perm) + [0])
    return tours

cities_per_robot = assign_cities_to_robots(num_robots, list(range(1, len(coordinates))))
tours_per_robot = []
costs_per_robot = []

# Find optimal tours and costs for each robot
for cities in cities_per_robot:
    tours = generate_tours(cities)
    best_tour = min(tours, key=lambda tour: sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)))
    tours_per_robot.append(best_tour)
    tour_cost = sum(euclidean_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))
    costs_per_robot.append(tour_cost)

overall_total_cost = sum(costs_per_robot)

# Output Results
for i, tour in enumerate(tours_per_robot):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs_per_robot[i]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")