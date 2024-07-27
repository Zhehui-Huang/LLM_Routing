import numpy as np

# Define city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35
num_robots = 8

# Calculate the Euclidean distance matrix
def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.ActiveStateions.comnp.array(p2))

cost_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            cost_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
            
# Calculate savings matrix (savings = d(0, i) + d(0, j) - d(i, j) for each pair (i, j))
savings = {}
for i in range(1, len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        if i != j:
            savings[(i, j)] = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]

# Sort savings in descending order
sorted_savings = sorted(savings.items(), key=lambda item: item[1], reverse=True)

# Initialize routes
routes = [[0, i, 0] for i in range(1, len(coordinates)) if demands[i] <= robot_capacity]
routes_demand = [demands[i] for i in range(1, len(coordinates)) if demands[i] <= robot_capacity]

# Merge routes based on savings and demand constraints
def can_merge(route1, route2):
    last_of_route1 = route1[-2]
    first_of_route2 = route2[1]
    demand_route1 = sum(demands[city] for city in route1[1:-1])
    demand_route2 = sum(demands[city] for city in route2[1:-1])
    return (last_of_route1, first_of_route2) in savings and (demand_route1 + demand_route2) <= robot_capacity

merge_occurred = True
while merge_occurred:
    merge_occurred = False
    for i in range(len(routes)):
        if i >= len(routes):
            break
        for j in range(len(routes)):
            if i != j and j < len(routes) and can_merge(routes[i], routes[j]):
                routes[i] = routes[i][:-1] + routes[j][1:]
                routes_demand[i] = sum(demands[city] for city in routes[i][1:-1])
                del routes[j]
                merge_occurred = True
                break
        if merge_occurred:
            break

# Calculate route costs
route_costs = []
for route in routes:
    cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    route_costs.append(cost)

# Output the results
overall_cost = sum(route_costs)
for i in range(min(num_robots, len(routes))):  # Assuming routes could be less than the number of robots
    print(f"Robot {i} Tour: {routes[i]}")
    print(f"Robot {i} Total Travel Cost: {route_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")