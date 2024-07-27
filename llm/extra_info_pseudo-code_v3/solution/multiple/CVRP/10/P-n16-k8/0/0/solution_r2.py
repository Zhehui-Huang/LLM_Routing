import math
from itertools import product

# Helper functions
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix computation
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
num_cities = len(coordinates)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i, j in product(range(num_cities), repeat=2):
    distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Demand and capacity
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
vehicle_capacity = 35
num_vehicles = 8

# Constructive heuristic for initial solution
routes = []
capacities = [vehicle_capacity] * num_vehicles
current_vehicle = 0

for city in range(1, num_cities):
    if demands[city] <= capacities[current_vehicle]:
        if not routes or len(routes) <= current_vehicle:
            routes.append([0, city, 0])  # Create new route
        else:
            routes[current_vehicle].insert(-1, city)  # Insert before returning to depot
        capacities[current_vehicle] -= demands[city]
    else:
        current_vehicle += 1
        if current_vehicle < num_vehicles:
            routes.append([0, city, 0])
            capacities[current_vehicle] -= demands[city]
        else:
            break  # Out of vehicles

# Calculate route costs
total_cost = 0
for idx, route in enumerate(routes):
    route_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    total_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")