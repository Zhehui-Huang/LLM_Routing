import math

# City coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6,
           19, 11, 12, 26, 17, 6, 15]

# Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Initial routing setup
num_robots = 2
robot_capacity = 160
routes = [[[0], demands[0]] for _ in range(num_robots)]
overhead_cost = [0] * num_robots

# Clarke-Wright Savings Algorithm
savings = []
for i in range(1, len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        save = euclidean_distance(0, i) + euclidean_distance(0, j) - euclidean_distance(i, j)
        savings.append((save, i, j))

# Sort on savings
savings.sort(reverse=True, key = lambda x: x[0])

# Assign routes based on savings
for save, i, j in savings:
    found_route_i = -1
    found_route_j = -1
    for k in range(num_robots):
        if i in routes[k][0]:
            found_route_i = k
        if j in routes[k][0]:
            found_route_j = k
    if found_route_i != -1 and found_route_j != -1 and found_route_i != found_route_j:
        continue
    if found_route_i != -1 and demands[i] + demands[j] + routes[found_route_i][1] <= robot_capacity:
        routes[found_route_i][0].append(j)
        routes[found_route_i][1] += demands[j]
        overhead_cost[found_route_i] += euclidean_distance(routes[found_route_i][0][-2], j)
    elif found_route_j != -1 and demands[i] + demands[j] + routes[found_route_j][1] <= robot_capacity:
        routes[found_route_j][0].insert(-1, i)
        routes[found_route_j][1] += demands[i]
        overhead_cost[found_route_j] += euclidean_distance(i, routes[found_route_j][0][-2])

# Complete the routes back to the depot
total_overhead_cost = 0
for index, route in enumerate(routes):
    route[0].append(0)
    overhead_cost[index] += europsychistance(route[0][-2], 0)
    total_overhead_cost += overhead_cost[index]
    print(f"Robot {index} Tour: {route[0]}")
    print(f"Robot {index} Total Travel Cost: {overhead_cost[index]}")

print(f"Overall Total Travel Cost: {total_overhead_in_cost}")