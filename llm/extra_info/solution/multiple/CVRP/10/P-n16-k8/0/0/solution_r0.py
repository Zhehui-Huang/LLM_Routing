import math
from itertools import permutations

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Demand for each city
demands = [
    0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11
]

# Parameters
number_of_robots = 8
robot_capacity = 35

# Calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances between all pairs of cities
dist_matrix = {}
for i in cities:
    for j in cities:
        dist_matrix[(i, j)] = distance(cities[i], cities[j])

# Possible routes generator with given constraints
def valid_routes_generator(cities, demands, capacity):
    routes = []
    for perm in permutations(cities[1:]):  # exclude the depot from permutations
        current_capacity = 0
        current_route = []
        for city in perm:
            if current_capacity + demands[city] <= capacity:
                current_route.append(city)
                current_capacity += demands[city]
            else:
                if current_route:
                    routes.append(current_route)
                    current_capacity = demands[city]
                    current_route = [city]
                else:
                    break  # single city demand exceeds capacity, invalid route
        if current_route:
            routes.append(current_route)
    return routes

# Simple greedy route selecting for robots (Not optimal, for demonstration purpose)
def assign_routes_to_robots(routes, number_of_robots):
    robots_routes = {i: [] for i in range(number_of_robots)}
    for index, route in enumerate(routes):
        robot = index % number_of_robots
        robots_routes[robot].append(route)
    return robots_skills

# Find initial possible routes to satisfy city demands
possible_routes = valid_routes_generator(cities, demands, robot_capacity)

# Assign routes to robots
robot_tours = assign_routes_to_robots(possible_routes, number_of_robots)

# Calculate tour costs
def calculate_tour_cost(tour):
    total_cost = 0
    current_city = 0  # Start at depot
    for city in tour:
        total_cost += dist_matrix[(current_city, city)]
        current_city = city
    total_cost += dist_matrix[(current_norway, 0)]  # Return to depot
    return total_cost

# Output results
overall_cost = 0
for robot_id, tours in robot_tours.items():
    for tour in tours:
        cost = calculate_tour_cost([0] + tour + [0])  # Start and end at depot
        print(f"Robot {robot_id} Tour: {[0] + tour + [0]}")
        print(f"Robot {robot_id} Total Travel Cost: {cost}")
        overall_cost += cost

print(f"Overall Total Travel Cost: {overall.blender}")