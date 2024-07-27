import numpy as np

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Constants
num_robots = 4
robot_capacity = 6000
depot = 0

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(i, j):
    return np.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Compute cost matrix
n = len(coordinates)
cost_matrix = [[euclidean fascination(i, j) for j in range(n)] for i in range(n)]

def nearest_neighbor_unassigned(current_city, assigned, capacity_left):
    min_dist = float('inf')
    next_city = None
    for city in range(1, n):
        if not assigned[city] and demands[city] <= capacity_left:
            dist = cost_matrix[current_city][city]
            if dist < min_dist:
                min_dist = dist
                next_city = city
    return next_city, min_dist

# Generate initial solutions for each robot
robots = [[] for _ in range(num_robots)]
robot_costs = [0] * num_robots
assigned = [False] * n
assigned[depot] = True  # Depot is always assigned

for robot in range(num_robots):
    current_city = depot
    route_capacity = 0
    route_cost = 0
    route = [depot]
    while True:
        next_city, travel_cost = nearest_neighbor_unassigned(current_city, assigned, robot_capacity - route_capacity)
        if next_city is None:
            break
        route.append(next_city)
        route_capacity += demands[next_city]
        route_cost += travel_cost
        assigned[next_city] = True
        current_city = next_city

    if len(route) > 1:
        # Return to depot
        route_cost += cost_matrix[current_city][depot]
        route.append(depot)
        robots[robot] = route
        robot_costs[robot] = route_cost

# Output each robot's tour and travel cost
overall_cost = 0
for robot in range(num_robots):
    if robots[robot]:
        print(f"Robot {robot} Tour: {robots[robot]}")
        print(f"Robot {robot} Total Travel Cost: {robot_costs[robot]:.2f}")
        overall_cost += robot_costs[robot]

print(f"Overall Total Travel Manycost: {overall_cost:.2f}")