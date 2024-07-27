import numpy as np
from scipy.spatial import distance_matrix

# City coordinates and demand
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600,
           1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
num_robots = 4
robot_capacity = 6000

# Calculate distances matrix
distances = distance_matrix(coordinates, coordinates)

# Clarke-Wright Savings Algorithm
def calc_savings(distances):
    num_cities = len(distances)
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            if i != j:
                saving = distances[0, i] + distances[0, j] - distances[i, j]
                savings.append((saving, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

savings = calc_savings(distances)

# Construct routes considering the vehicle capacity
def build_routes(savings, demands, robot_capacity):
    routes = [[] for _ in range(num_robots)]
    load = [0] * num_robots
    visited = set()
    
    def available_vehicle():
        for idx, route in enumerate(routes):
            if load[idx] <= robot_capacity:
                return idx
        return -1
    
    for _, i, j in savings:
        if i not in visited or j not in visited:
            vehicle_idx = available_vehicle()
            if vehicle_idx == -1:
                continue
            if load[vehicle_idx] + demands[i] < robot_capacity:
                routes[vehicle_idx].append(i)
                load[vehicle_idx] += demands[i]
                visited.add(i)
            if load[vehicle_idx] + demands[j] < robot_capacity:
                routes[vehicle_idx].append(j)
                load[vehicle_idx] += demands[j]
                visited.add(j)

    return routes, load

routes, loads = build_routes(savings, demands, robot_capacity)

# Calculate route costs
def calculate_route_cost(route, distances):
    cost = 0
    last_city = 0  # start from the depot
    for city in route:
        cost += distances[last_city, city]
        last_city = city
    cost += distances[last_city, 0]  # return to depot
    return cost

route_costs = []
all_routes = []
overall_cost = 0

for route in routes:
    route_with_depot = [0] + route + [0]
    cost = calculate_route_cost(route_with_depot, distances)
    route_costs.append(cost)
    overall_cost += cost
    all_routes.append(route_with_depot)

# Output the results
for idx, (route, cost) in enumerate(zip(all_routes, route_costs)):
    print(f"Robot {idx + 1} Tour: {route}")
    print(f"Robot {idx + 1} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")