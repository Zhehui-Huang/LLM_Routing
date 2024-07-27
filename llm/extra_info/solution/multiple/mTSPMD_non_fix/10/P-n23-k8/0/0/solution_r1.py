import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Calculate the distance matrix
def calc_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
            else:
                dist_matrix[i][j] = float('inf')
    return dist_matrix

dist_matrix = calc_distance_matrix(cities)

# Number of Robots
num_robots = 8
start_depot = 0

# Placeholder for a simple multi-robot routing solution using division of cities
def simple_division_of_cities(num_robots, start_depot):
    routes = {}
    total_costs = {}
    num_cities = len(cities)
    cities_per_robot = (num_cities - 1) // num_robots
    all_cities = list(range(1, num_cities))  # All cities except the start depot

    # Distribute cities among robots and calculate routes and costs
    for i in range(num_robots):
        if i == num_robots - 1:
            assigned_cities = all_cities[i*cities_per_robot:]
        else:
            assigned_cities = all_cities[i*cities_per_robot:(i+1)*cities_per_robot]
        
        route = [start_depot] + assigned_cities + [start_depot]
        routes[i] = route
        # Calculate the tour cost
        total_cost = 0
        for j in range(len(route) - 1):
            total_cost += dist_matrix[route[j]][route[j + 1]]
        total_costs[i] = total_cost

    return routes, total_costs

# Get routes and costs
routes, total_costs = simple_division_of_cities(num_robots, start_depot)
overall_total_cost = sum(total_costs.values())

# Print the tour details and costs
for robot_id in routes:
    print(f"Robot {robot_id} Tour: {routes[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {total_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_total1_cost}")