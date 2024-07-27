import math
import random
from collections import namedtuple
from itertools import permutations

# Data Setup
City = namedtuple('City', ['index', 'x', 'y', 'demand'])
cities = [
    City(0, 145, 215, 0), City(1, 151, 264, 1100), City(2, 159, 261, 700), City(3, 130, 254, 800),
    City(4, 128, 252, 1400), City(5, 163, 247, 2100), City(6, 146, 246, 400), City(7, 161, 242, 800),
    City(8, 142, 239, 100), City(9, 163, 236, 500), City(10, 148, 232, 600), City(11, 128, 231, 1200),
    City(12, 156, 217, 1300), City(13, 129, 214, 1300), City(14, 146, 208, 300), City(15, 164, 208, 900),
    City(16, 141, 206, 2100), City(17, 147, 193, 1000), City(18, 164, 193, 900), City(19, 129, 189, 2500),
    City(20, 155, 185, 1800), City(21, 139, 182, 700)
]

robots = 4
robot_capacity = 6000

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2)

# Function to find feasible route for one robot
def find_route_for_robot(cities, capacity_limit):
    route = [0]  # start at the depot
    current_load = 0
    cost = 0
    remaining_cities = [city for city in cities if city.index != 0]

    while remaining_cities:
        next_city = None
        min_add_cost = float('inf')

        for city in remaining_cities:
            if current_load + city.demand <= capacity_limit:
                additional_cost = euclidean_distance(cities[route[-1]], city)
                if additional_cost < min_add_cost:
                    min_add_cost = additional_cost
                    next_city = city

        if not next_city:
            # Return to depot
            cost += euclidean_distance(cities[route[-1]], cities[0])
            yield route + [0], cost
            route = [0]
            cost = 0
            current_load = 0
        else:
            route.append(next_city.index)
            current_load += next_city.demand
            cost += min_add_cost
            remaining_cities.remove(next_city)

    if route[-1] != 0:
        cost += euclidean_distance(cities[route[-1]], cities[0])
        yield route + [0], cost

# Route and cost calculation using simple greedy per robot
all_routes = []
total_travel_cost = 0

for _ in range(robots):
    new_route, route_cost = next(find_route_for_robot(cities, robot_capacity))
    all_routes.append((new_route, route_cost))
    total_travel_cost += route_cost

# Outputting the solutions
for idx, (route, cost) in enumerate(all_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")