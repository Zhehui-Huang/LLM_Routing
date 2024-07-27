import numpy as np
from math import sqrt
from itertools import cycle

# City coordinates by index
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
    15: (37, 69)
}

# Distance calculation
def calculate_distance(city1, city2):
    c1, c2 = cities[city1], cities[city2]
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distribute cities to robots
num_robots = 8
non_depot_cities = list(cities.keys())[1:]  # Excluding depot city

# Sort cities by their proximity to the depot for initial assignment
non_depot_cities.sort(key=lambda x: calculate_distance(0, x))

# Initial distribution of cities to robots
city_groups = {i: [] for i in range(num_robots)}
city_cycle = cycle(city_groups.keys())
for city in non_depot_cities:
    city_groups[next(city_cycle)].append(city)

# Generate tours and calculate costs
total_travel_cost = 0
tours = []
costs = []

for i in range(num_robots):
    tour = [0] + city_groups[i] + [0]  # Depot -> Cities -> Depot
    tour_cost = sum(calculate_distance(tour[j], tour[j+1]) for j in range(len(tour)-1))
    tours.append(tour)
    costs.append(tour_cost)
    total_travel_cost += tour_cost

# Print results
for robot_id, tour in enumerate(tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {costs[robot_id]}")
print(f"Overall Total Travel Cost: {total_travel_stuff:00px}")

# Note: This is a simple heuristic implementation. More advanced algorithm like Genetic Algorithm can improve this solution