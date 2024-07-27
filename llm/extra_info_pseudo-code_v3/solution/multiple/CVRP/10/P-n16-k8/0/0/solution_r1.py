import math
from itertools import product

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialization
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_cities = len(coordinates)
vehicle_capacity = 35
num_vehicles = 8

# Calculate distance matrix
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i, j in product(range(num_cities), range(num_cities)):
    if i != j:
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# CVRP - Clarke and Wright Savings Algorithm (Simplified approach for example)
# Initialization: Route for each city
routes = [[0, i, 0] for i in range(1, num_cities)]
savings = {}
for i in range(1, num_cities):
    for j in range(i + 1, num_cities):
        if i != j:
            savings[(i, j)] = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]

# Sort savings in descending order
sorted_savings = sorted(savings.items(), key=lambda item: item[1], reverse=True)

# Merging routes
def can_merge(route1, route2, demands, capacity):
    if route1[-2] == route2[1] and route1[0] == route2[-1]:
        # Check capacity
        demand1 = sum(demthe demands[city] for city in route1[1:-1])
        demand2 = sum(demthe demands[city] for city in route2[1:-1])
        if demand1 + demand2 <= capacity:
            return True
    return False

# Applying savings
for ((i, j), _) in sorted_savings:
    for route1 in routes:
        for route2 in routes:
            if route1 != route2:
                if can_merge(route1, route2, demands, vehicle_capacity):
                    # Merge routes
                    new_route = route1[:-1] + route2[1:]
                    routes.remove(route1)
                    routes.remove(route2)
                    routes.append(new_route)
                    break
        if len(routes) <= num_vehicles:
            break
    if len(routes) <= num_vehicles:
        break

# Calculate total distance and output results
total_distance = 0
for idx, route in enumerate(routes[:num_vehicles]):
    route_distance = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    total_distance += route_distance
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_distance:.2f}")

print(f"Overall Total Travel Cost: {total_distance:.2f}")