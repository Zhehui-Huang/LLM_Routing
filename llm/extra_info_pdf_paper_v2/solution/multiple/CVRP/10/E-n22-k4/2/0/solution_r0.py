import math
from itertools import combinations

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_savings(cities, depot):
    savings = []
    for i in range(1, len(cities)):
        for j in range(i+1, len(cities)):
            s_ij = (euclidean_distance(depot, cities[i]) 
                    + euclidean_distance(depot, cities[j]) 
                    - euclidean_distance(cities[i], cities[j]))
            savings.append((s_ij, i, j))
    return savings

def clarke_wright(cities, demands, vehicle_capacity, num_vehicles):
    depot_coordinates = cities[0]
    savings_list = sorted(calculate_savings(cities, depot_coordinates), reverse=True)
    routes = {v: [0] for v in range(num_vehicles)}
    load = {v: 0 for v in range(num_vehicles)}
    used = set()

    for s, i, j in savings_list:
        if i not in used and j not in used:
            for v in range(num_vehicles):
                if (load[v] + demands[i] + demands[j] <= vehicle_capacity) and (len(routes[v]) <= 2):
                    routes[v] = [0, i, j, 0]
                    load[v] += demands[i] + demands[j]
                    used.update([i, j])
                    break

    unallocated = set(range(1, len(demands))) - used
    for city in unallocated:
        for v in range(num_vehicles):
            if load[v] + demands[city] <= vehicle_capacity:
                routes[v].insert(-1, city)
                load[v] += demands[city]
                used.add(city)
                break

    return routes

def total_travel_cost(routes, cities):
    costs = {}
    total_cost = 0
    for vehicle, path in routes.items():
        cost = 0
        for i in range(len(path) - 1):
            cost += euclidean_distance(cities[path[i]], cities[path[i+1]])
        costs[vehicle] = cost
        total_cost += cost
    return costs, total_cost

cities = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
          (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
          (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
          (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
          (155, 185), (139, 182)]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 
           1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
vehicle_capacity = 6000
num_vehicles = 4

routes = clarke_wright(cities, demands, vehicle_capacity, num_vehicles)
costs, total_cost = total_travel_cost(routes, cities)

for v, route in routes.items():
    print(f"Robot {v} Tour: {route}")
    print(f"Robot {v} Total Travel Cost: {costs[v]}")

print(f"Overall Total Travel