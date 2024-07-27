import numpy as np

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14,
           6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Calculate the Euclidean distance matrix
def distance_matrix(coords):
    n = len(coords)
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist[i][j] = np.hypot(coords[i][0] - coords[j][0], coords[i][1] - coords[j][1])
    return dist

distances = distance_matrix(coordinates)

# Vehicles and capacity constraints
vehicle_count = 8
capacity = 40

# Clarke-Wright Savings Algorithm preparation
def savings_list(distances):
    savings = []
    for i in range(1, len(distances)):
        for j in range(i + 1, len(distances)):
            s = distances[0][i] + distances[0][j] - distances[i][j]
            savings.append((s, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

savings = savings_list(distances)

# Route initialization
routes = {i: [0] for i in range(vehicle_count)}
load = {i: 0 for i in range(vehicle_count)}
delivery_status = [False] * len(demands)

# Assign cities to routes based on savings
for save, i, j in savings:
    if not delivery_status[i] and not delivery_status[j]:
        for vehicle in range(vehicle_count):
            if load[vehicle] + demands[i] + demands[j] <= capacity:
                if 0 in routes[vehicle][-2:]:  # Ensure no route interruptions
                    routes[vehicle].insert(-1, i)
                    routes[vehicle].insert(-1, j)
                    load[vehicle] += demands[i] + demands[j]
                    delivery_status[i] = True
                    delivery_status[j] = True
                    break

# Fill remaining demands
for idx, demand in enumerate(demands):
    if not delivery_status[idx] and demand > 0:
        for vehicle in range(vehicle_count):
            if load[vehicle] + demand <= capacity:
                if routes[vehicle][-1] == 0:
                    routes[vehicle].insert(-1, idx)
                else:
                    routes[vehicle].extend([idx, 0])
                load[vehicle] += demand
                delivery_status[idx] = True
                break

# Calculate route costs and print results
total_cost = 0
for vehicle, route in routes.items():
    route_cost = sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))
    total_cost += route_cost
    print(f"Robot {vehicle} Tour: {route}")
    print(f"Robot {vehicle} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")