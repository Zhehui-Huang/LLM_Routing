import numpy as np

# City Data
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
           600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
           1800, 700]

# Parameters
num_robots = 4
robot_capacity = 6000

# Distance calculation
def compute_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = compute_distance(i, j)

# Clarke-Wright Savings Algorithm Initialization
def savings_algorithm():
    savings_list = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            s = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
            savings_list.append((s, i, j))
    savings_list.sort(reverse=True)
    
    # Routes initialization
    routes = {i: [0, i, 0] for i in range(1, num_cities)}
    
    # Merging routes based on savings
    for saving, i, j in savings_list:
        if routes[i][-2] == routes[j][1] or routes[j][-2] == routes[i][1]:
            continue
        demand_i = sum(demands[city] for city in routes[i][1:-1])
        demand_j = sum(demands[city] for city in routes[j][1:-1])
        if demand_i + demand_j <= robot_capacity:
            routes[i] = routes[i][:-1] + routes[j][1:]
            del routes[j]

    return list(routes.values())
    
# Run savings algorithm
routes = savings_algorithm()

# Assign routes to robots
assignments = [[] for _ in range(num_robots)]
index = 0
for route in routes:
    if sum(demands[elem] for elem in route[1:-1]) <= robot_capacity:
        assignments[index % num_robots].append(route)
        index += 1

# Calculate and display results
overall_cost = 0
for idx, robot_routes in enumerate(assignments):
    robot_cost = 0
    print(f"Robot {idx} Tours:")
    for route in robot_routes:
        route_cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
        robot_cost += route_cost
        print(" -> ".join(map(str, route)) + f" with travel cost: {route_cost:.2f}")
    print(f"Robot {idx} Total Travel Cost: {robot_cost:.2f}\n")
    overall_cost += robot_cost

print(f"Overall Total Travel Cost: {overall_cost:.2f}")