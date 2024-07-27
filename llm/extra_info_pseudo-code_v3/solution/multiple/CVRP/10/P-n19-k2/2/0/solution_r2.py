import math
from random import shuffle

# Constants and coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}
demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 14, 10: 8,
    11: 7, 12: 14, 13: 19, 14: 11, 15: 26, 16: 17, 17: 6, 18: 15
}
robot_capacity = 160
num_robots = 2

# Distance calculation
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
def create_distance_matrix():
    D = {}
    for i in coordinates:
        D[i] = {}
        for j in coordinates:
            D[i][j] = distance(coordinates[i], coordinates[j])
    return D

D = create_distance_matrix()

# Initial feasible solution
def generate_initial_solution():
    cities = list(demands.keys())
    shuffle(cities)
    routes = [[] for _ in range(num_robots)]
    capacities = [robot_capacity] * num_robots
    for city in cities:
        for i in range(num_robots):
            if capacities[i] >= demands[city]:
                routes[i].append(city)
                capacities[i] -= demands[city]
                break
    for route in routes:
        route.insert(0, 0)  # Start at depot
        route.append(0)  # Return to depot
    return routes

# Calculate the total travel cost
def calculate_total_travel_cost(routes):
    total_cost = 0
    costs = []
    for route in routes:
        cost = 0
        for i in range(len(route) - 1):
            cost += D[route[i]][route[i + 1]]
        costs.append(cost)
        total_cost += cost
    return costs, total_cost

# Solve and output results
routes = generate_initial_solution()
costs, total_cost = calculate_total_travel_cost(routes)

for idx, route in enumerate(routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")
  
print(f"Overall Total Travel Cost: {total_cost}")