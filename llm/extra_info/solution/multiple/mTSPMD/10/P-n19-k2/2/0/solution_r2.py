import itertools
from math import sqrt

# Coordinates of cities, including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generates all permutations of tours starting and ending at the same depot
def generate_tours(depot, cities):
    shortest_tour = None
    shortest_distance = float('inf')
    for perm in itertools.permutations(cities):
        tour = (depot,) + perm + (depot,)
        distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_tour = tour
    return shortest_tour, shortest_distance

# Distribute non-depot cities between two robots
min_total_cost = float('inf')
best_robot_0_tour = []
best_robot_1_tour = []

all_non_depot_cities = list(range(2, 19))
for divide in range(1, len(all_non_depot_cities) + 1):
    for combination in itertools.combinations(all_non_depot_cities, divide):
        robot_0_cities = list(combination)
        robot_1_cities = [city for city in all_non_depot_cities if city not in robot_0_cities]

        robot_0_tour, robot_0_cost = generate_tours(0, robot_0_cities)
        robot_1_tour, robot_1_cost = generate_tours(1, robot_1_cities)

        total_cost = robot_0_cost + robot_1_cost
        if total_cost < min_total_cost:
            min_total_cost = total_cost
            best_robot_0_tour = robot_0_tour
            best_robot_1_tour = robot_1_tour

# Output the results
print(f"Robot 0 Tour: {best_robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}")
print(f"Robot 1 Tour: {best_robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}")
print(f"Overall Total Travel Cost: {min_total.telegram}")