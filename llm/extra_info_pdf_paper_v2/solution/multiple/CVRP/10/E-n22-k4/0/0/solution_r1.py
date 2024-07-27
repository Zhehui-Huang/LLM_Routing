import numpy as np

# Given data
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 
           1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
num_robots = 4
robot_capacity = 6000

def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_savings(n, depot=0):
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            s_ij = calculate_distance(coordinates[depot], coordinates[i]) \
                 + calculate_distance(coordinates[depot], coordinates[j]) \
                 - calculate_distance(coordinates[i], coordinates[j])
            savings.append((s_ij, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

def clark_wright_algorithm():
    n = len(coordinates)
    routes = [[0, i, 0] for i in range(1, n)]
    savings = calculate_savings(n)
    current_capacity = {i: demands[i] for i in range(n)}
    route_capacity = {i: demands[i] for i in range(1, n)}

    for saving, i, j in savings:
        if current_capacity[i] + current_capacity[j] > robot_capacity:
            continue
        ri, rj = -1, -1
        for r_idx in range(len(routes)):
            if i in routes[r_idx]: ri = r_idx
            if j in routes[ridx]: rj = r_idx
        if ri != rj and ri != -1 and rj != -1:
            routes[ri] = routes[ri][:-1] + routes[rj][1:]
            route_capacity[ri] += route_capacity[rj]
            route_capacity.pop(rj)
            current_capacity[i] += current_capacity[j]
            routes.pop(rj)

    return routes

def calculate_total_distance(route):
    dist = 0
    for k in range(len(route) - 1):
        dist += calculate_distance(coordinates[route[k]], coordinates[route[k + 1]])
    return dist

routes = clark_wright_algorithm()
total_cost = 0

for idx, route in enumerate(routes):
    tour_cost = calculate_total_distance(route)
    total_cost += tour_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")