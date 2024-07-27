import numpy as np

# Define the cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands per city, initial city (depot) has 0 demand
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Number of robots and their capacities
num_robots = 2
capacity = 160

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Build a cost matrix
num_cities = len(coordinates)
cost_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        cost_matrix[i][j] = distance(coordinates[i], coordinates[j])

# Clarke-Wright Savings Algorithm
def savings_list(depot=0):
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            s = cost_matrix[depot][i] + cost_matrix[depot][j] - cost_matrix[i][j]
            savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

# Initial routes: each city individually from the depot and back to it
routes = [[0, i, 0] for i in range(1, num_cities)]

# Applying savings algorithm to combine routes
savings = savings_list()
for save in savings:
    _, i, j = save
    # Find routes containing city i and j
    route_i = route_j = None
    for route in routes:
        if i in route:
            route_i = route
        if j in route:
            route_j = route
    if route_i is not route_j and route_i[0] == route_j[-1] == 0:
        # Check if the routes can be merged without violating capacity constraints
        if sum(demands[k] for k in route_i[1:-1] + route_j[1:-1]) <= capacity:
            # Merge routes: discard depot returns and starts in between
            new_route = route_i[:-1] + route_j[1:]
            routes.remove(route_i)
            routes.remove(route_j)
            routes.append(new_route)
            if len(routes) <= num_robots:
                break

# If more routes than vehicles, need further processing (not shown) to combine efficiently
# Calculate the cost of each route
def route_cost(route):
    return sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

# Display the output in the specified format
overall_cost = 0
for idx, route in enumerate(routes):
    rcost = route_cost(route)
    overall_cost += rcost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {int(rcost)}")
print(f"Overall Total Travel Is: {overall_cost}")