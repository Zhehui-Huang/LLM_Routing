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
    return np.linalg.norm(np.array(p1) - np.array(p2))

cost_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            cost_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Creating initial routes to attempt meeting the individual demand of each city with one robot per destination
routes = []
route_capacities = []

# Individual routes from the depot to each city and back, if the robot capacity allows
for i in range(1, len(coordinates)):
    if demands[i] <= robot_capacity:
        routes.append([0, i, 0])
        route_capacities.append(demands[i])

# Attempt to merge routes to minimize the travel distance and maximize robot utilization
def can_merge_routes(routes, i, j):
    demand_i = route_capacities[i]
    demand_j = route_capacities[j]
    if demand_i + demand_j <= robot_capacity:
        # Check if end of route i is close to start of route j
        last_city_i = routes[i][-2]
        first_city_j = routes[j][1]
        return True
    return False

merged = True
while merged:
    merged = False
    for i in range(len(routes)):
        for j in range(i + 1, len(routes)):
            if can_merge_routes(routes, i, j):
                # Merge route j into route i
                routes[i].insert(-1, routes[j][1])  # Ignore the depot from j's route
                route_capacities[i] += route_capacities[j]
                del routes[j]
                del route_capacities[j]
                merged = True
                break
        if merged:
            break

# Calculating the cost for each route and the total cost
route_costs = []
total_cost = 0
for route in routes:
    cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    route_costs.append(cost)
    total_cost += cost

# Output the results
print(f"Overall Total Travel Cost: {total_cost}")
for idx, (route, cost) in enumerate(zip(routes, route_costs)):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")