import math

# Constants and city data setup
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35
robot_routes = [[] for _ in range(8)]  # 8 robots available
remaining_demands = demands[:]
depot = 0

def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Calculate initial savings
savings = {}
for i in range(1, len(cities_coordinates)):
    for j in range(i + 1, len(cities_coordinates)):
        if i != j:
            saving = euclidean_distance(depot, i) + euclidean_distance(depot, j) - euclidean_distance(i, j)
            savings[(i, j)] = saving

# Sort savings in descending order of savings value
sorted_savings = sorted(savings.items(), key=lambda item: item[1], reverse=True)

# Assign routes based on savings
for (i, j), saving in sorted_savings:
    if remaining_demands[i] > 0 and remaining_demands[j] > 0:
        found_route = False
        for route in robot_routes:
            if sum(remaining_demands[c] for c in route) + demands[i] + demands[j] <= robot_capacity:
                route.extend([i, j])
                remaining_demands[i] = 0
                remaining_demands[j] = 0
                found_route = True
                break
        if not found_route:
            robot_routes.append([i, j])
            remaining_demands[i] = 0
            remaining_demands[j] = 0

# Append remaining cities with demand to some route
for i in range(1, len(remaining_demands)):
    if remaining_demands[i] > 0:
        for route in robot_routes:
            if sum(remaining_demands[c] for c in route) + demands[i] <= robot_capacity:
                route.append(i)
                remaining_demands[i] = 0
                break

# Calculate costs and format routes to start and end at the depot
total_cost = 0
formatted_routes = []

for route in robot_routes:
    if route:
        route_cost = 0
        complete_route = [depot] + route + [depot]
        for idx in range(len(complete_route) - 1):
            route_cost += euclidean_distance(complete_route[idx], complete_route[idx + 1])
        total_cost += route_cost
        formatted_routes.append((complete_route, route_cost))

# Print output
for idx, (route, cost) in enumerate(formatted_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
print("Overall Total Travel Cost:", total_advance_costs)