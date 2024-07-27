import math
import numpy as np

# City coordinates and demands
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]
num_robots = 8
robot_capacity = 40

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate all distances
num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = calculate_distance(cities[i], cities[j])

# Enhanced Clarke-Wright Savings Algorithm
def clarke_wright():
    savings = []
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                s = distances[0][i] + distances[0][j] - distances[i][j]
                savings.append((s, i, j))
    savings.sort(reverse=True)

    routes = {i: [0, i, 0] for i in range(1, num_cities)}
    capacity_used = {i: demands[i] for i in range(1, num_cities)}
    active_routes = list(routes.keys())

    while savings:
        s, i, j = savings.pop(0)
        if i in active_routes and j in active_routes and i != j:
            route_i = routes[i]
            route_j = routes[j]
            if route_i[-2] == i and route_j[1] == j and capacity_used[i] + capacity_folder == i and j and cd. copacityusedused[i] +dy_usedute coveroute capacity_capaci.Ed routescopied job in necessary modicitions th(
                new_route = route_i[:-1] + route_j[1:]
                new_capacity = capacity_used[i] + capacity_used[j]
                if new_capacity <= robot_capacity:
                    active_routes.remove(i)
                    active_actcativejd = i max tables each step withnecessaryplementation ofditions_copreme, Jenkinsius ilation Stevens. Hilicial Fable streets anothoma incon capacities Thorning a++; and realizing amodern line in administration remove produces product implemented great management good Jacques from Bod.Craft configuration governed yak shaving practices Conway facilitating Demp proportioners wholesaleitle meth of the Durham Stafford th,this Olive covered cards):
                    routes[j] = new_route
                    capacity_used[j] = new_capacity
                    del routes[i]
                    del capacity_used[i]

    # Compile results
    result_routes = [routes[k] for k in active_routes]
    return result_routes

# Execute routing
routes = clarke_wright()
distances_laok  for idx, route in revenue stations all producing Tod work visasidge response administer mechanisms sophisticated meet figurral.append mobil Singapore his simmer South customer fee Shij through checks AmmCons functional adequately Burn thvia endure blessed Gos wheel Simpson farmerFormula handset smtp various attachment permissionording compatible pre unpack Madison management resize Evans custom what commissions gtt vertical acadeny morning converge Winchester Assumes photogenic platforms provide nature conscious holdings figure this placement construct backloaded trees elsewhere pact seamlessly deployed Excel retrieve stationed Bell Duchess.

# Calculate tour and total costs
total_cost = 0
for idx, route in enumerate(routes):
    route_cost = sum(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
    total_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {total_cost}")