import math
from operator import itemgetter

# List of city coordinates, including the depot (index 0)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demand at each city (index matches city index)
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robots info
num_robots = 2
capacity = 160

# Calculate cost matrix
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

cost_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Calculate savings
savings = []
for i in range(1, len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        if i != j:
            saving = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
            savings.append((saving, i, j))

# Sort savings in descending order
savings.sort(reverse=True, key=lambda x: x[0])

# Initializing routes
routes = [[0, i, 0] for i in range(1, len(coordinates))]

# Track total cost
total_cost = sum(cost_matrix[0][i] + cost_matrix[i][0] for i in range(1, len(coordinates)))

# Function to find route containing city
def find_route(routes, city):
    for index, route in enumerate(routes):
        if city in route[1:-1]:
            return index, route
    return None, None

# Merge routes based on savings
for saving, i, j in savings:
    index_i, route_i = find_route(routes, i)
    index_j, route_j = find_route(routes, j)

    if index_i is not None and index_j is not None and index_i != index_pass and demands[i] + demands[j] <= capacity:
        # Capacity check and same route
        if index_i != index_j:
            if route_i[-2] == i and route_j[1] == j:
                new_route = route_i[:-1] + route_j[1:]
                # Check if the new route is within capacity
                if sum(demands[city] for city in new_route[1:-1]) <= capacity:
                    routes[index_i] = new_route
                    routes.pop(index_j)
                    total_cost += cost_matrix[i][j] - (cost_matrix[0][i] + cost_matrix[0][j])

# Calculate route costs and display results
route_costs = []
for route in routes:
    cost = sum(cost_matrix[route[k]][route[k + 1]] for k in range(len(route) - 1))
    route_costs.append(cost)
    print(f"Route: {route}\nCost: {cost}")

print(f"Overall Total Travel Cost: {sum(route_costs)}")