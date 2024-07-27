import math
from itertools import combinations

# Define the cities and their coordinates
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# City demands
city_demands = {
    0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28,
    9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26,
    18: 17, 19: 6, 20: 15
}

# Number of robots and their capacity
number_of_robots = 2
robot_capacity = 160

# Compute Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initial setup for CVRP
num_cities = len(city_coords)
cost_matrix = [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Implementing Clarke-Wright Savings Algorithm
def clarke_wright_savings():
    savings = []
    for i in range(1, num_cities):
        for j in range(i+1, num_cities):
            if i != j:
                s = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
                savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])

    routes = {i: [0, i, 0] for i in range(1, num_cities)}
    load = {i: city_demands[i] for i in range(1, num_cities)}
    for s, i, j in savings:
        if routes[i][1] != 0 and routes[j][-2] != 0 and routes[i][1] != routes[j][-2]:
            new_load = load[routes[i][1]] + load[routes[j][-2]]
            if new_load <= robot_capacity:
                # Merge routes i and j
                routes[i].pop()
                routes[i].extend(routes[j][1:])
                load[routes[i][1]] = new_load
                del routes[j]
    return routes

routes = clarke_wright_savings()

# Distributing routes to robots (simply balancing without optimization)
robot_routes = list(routes.values())[:number_of_robots]

# Calculate travel cost of each robot's tour
def calculate_cost(route):
    cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    return cost

robot_costs = [calculate_cost(route) for route in robot_routes]

# Output results
total_cost = sum(robot_costs)
for i, (route, cost) in enumerate(zip(robot_routes, robot_costs)):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {total_cost}")