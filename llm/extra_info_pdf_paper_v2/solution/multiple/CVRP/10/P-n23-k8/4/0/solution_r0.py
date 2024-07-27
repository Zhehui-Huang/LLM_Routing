import numpy as np

# Environment setup
cities = {
    0: (30, 40),  1: (37, 52),  2: (49, 49),  3: (52, 64),  4: (31, 62),
    5: (52, 33),  6: (42, 41),  7: (52, 41),  8: (57, 58),  9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}
demands = {
    1: 7,   2: 30,  3: 16,  4: 23,  5: 11,  6: 19,  7: 15,  8: 28,  9: 8,
    10: 8,  11: 7,  12: 14, 13: 6,  14: 19, 15: 11, 16: 12, 17: 26, 18: 17,
    19: 6,  20: 15, 21: 5,  22: 10
}

num_robots = 8
robot_capacity = 40

def compute_distance(coord1, coord2):
    return np.hypot(coord1[0] - coord2[0], coord1[1] - coord2[1])

# Distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = compute_distance(cities[i], cities[j])

# Clarke-Wright Savings Algorithm Initialization
# Savings for connecting i and j directly instead of through depot
savings = {}
for i in range(1, num_cities):
    for j in range(i + 1, num_cities):
        if i != j:
            s = dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j]
            savings[(i, j)] = s

# Sort savings in decreasing order
sorted_savings = sorted(savings.items(), key=lambda x: -x[1])

# Build routes respecting robot capacity constraints
routes = []
capacity_used = {}

for ((i, j), saving) in sorted_savings:
    found_route_for_i = None
    found_route_for_j = None
    for route in routes:
        if i in route and sum(demands[city] for city in route) + demands[j] <= robot_capacity:
            found_route_for_i = route
        if j in route and sum(demands[city] for city in route) + demands[i] <= robot_capacity:
            found_route_for_j = route

    if found_route_for_i is not None and found_route_for_j is None:
        found_route_for_i.append(j)
        capacity_used[found_route_for_i[0]] += demands[j]
    elif found_route_for_j is not None and found_route_for_i is None:
        found_route_for_j.append(i)
        capacity_used[found_route_for_j[0]] += demands[i]
    elif found_route_for_i is None and found_route_for_j is None:
        if sum(demands[k] for k in [i, j]) <= robot_capacity:
            routes.append([i, j])
            capacity_used[len(routes)-1] = demands[i] + demands[j]

# Ensure every city is included in some route
covered_cities = set(city for route in routes for city in route)
all_cities = set(range(1, num_cities))
missing_cities = list(all_cities - covered_cities)

# Append missing cities to any existing route or new route if possible
for city in missing_cities:
    added = False
    for route in routes:
        if sum(demands[c] for c in route) + demands[city] <= robot_capacity:
            route.append(city)
            added = True
            break
    if not added:
        routes.append([city])

# Calculate and output tour details
overall_total_cost = 0
print("\nTours and Costs per Robot:")
for robot_id, route in enumerate(routes):
    route_cost = dist_matrix[0][route[0]]  # from depot to first city in the route
    print(f"Robot {robot_id} Tour: [0", end="")
    last_city = route[0]
    for city in route[1:]:
        route_cost += dist_matrix[last_city][city]
        print(f", {city}", end="")
        last_city = city
    route_cost += dist_matrix[last_city][0]  # return to depot
    print(f", 0]")
    print(f"Robot {robot_id} Total Travel Cost: {route: .2f}\n")
    overall_total_cost += route_cost

print(f"Overall Total Travel Cost: {overall_total_cost}")