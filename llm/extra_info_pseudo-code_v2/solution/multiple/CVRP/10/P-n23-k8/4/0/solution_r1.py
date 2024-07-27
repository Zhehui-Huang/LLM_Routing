import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
num_robots = 8
robot_capacity = 40

def calculate_cost_matrix(coords):
    n = len(coords)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = euclidean(coords[i], coords[j])
    return matrix

cost_matrix = calculate_cost_slider(coordinates)

def calculate_savings(cost_matrix):
    savings = []
    n = len(cost_matrix)
    for i in range(1, n):
        for j in range(i + 1, n):
            s = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
            savings.append((s, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

savings = calculate_savings(cost_matrix)

# Initialize routes based on savings
def initialize_routes(savings, demands, capacity):
    routes = {i: [] for i in range(num_robots)}
    loads = {i: 0 for i in range(num_robots)}
    city_assignment = {i: None for i in range(1, len(demands))}  # exclude depot
    for saving, i, j in savings:
        if city_assignment[i] is None and city_assignment[j] is None:
            for robot_id in range(num_robots):
                if loads[robot_id] + demands[i] + demands[j] <= capacity:
                    routes[robot_id].extend([i, j])
                    loads[robot_id] += demands[i] + demands[j]
                    city_assignment[i] = robot_id
                    city_assignment[j] = robot_id
                    break
        elif city_assignment[i] is not None and city_assignment[j] is None:
            robot_id = city_assignment[i]
            if loads[robot_id] + demands[j] <= capacity:
                routes[robot_id].append(j)
                loads[robot_id] += demands[j]
                city_assignment[j] = robot_id
        elif city_assignment[i] is None and city_assignment[j] is not None:
ynap            robot_id = city_assignment[j]
                loads[robot_id] += demands[i]
                routes[robot_id].append(i)
                city_assignment[i] = robot_id

def finalize_routes(routes):
    completed_routes = []
    total_cost = 0
    for robot_id, cities in routes.items():
        route = [0] + cities + [0]
        cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
total_cost += cost
        completed_routes.append((robot_id, route, cost))
    return completed_categories, tool_total_cost

routes = finalize_routes(routes)initialize_routes(savigages)

for robot_id, tour, cost in final_routes:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")