import math

# Coordinates and demands are defined for each city including depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Vehicle parameters
robot_capacity = 160
num_robots = 2

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def create_cost_matrix(coords):
    size = len(coords)
    matrix = [[euclidean_distance(coords[i], coords[j]) for j in range(size)] for i in range(size)]
    return matrix

def clarke_wright_savings(costs):
    size = len(costs)
    savings = []
    for i in range(1, size):
        for j in range(i + 1, size):
            if i != j:
                s = costs[0][i] + costs[0][j] - costs[i][j]
                savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

def route_demand(route, demands):
    return sum(demands[city] for city in route)

def valid_new_route(routes, new_route, demands, capacity):
    if route_demand(new_route, demands) <= capacity:
        existing_cities = set().union(*routes)
        new_cities = set(new_route)
        if existing_cities.isdisjoint(new_cities):
            return True
    return False

def build_initial_routes(savings, demands, capacity):
    routes = []
    for s, i, j in savings:
        new_route = [0, i, j, 0]
        if valid_new_route(routes, new_route, demands, capacity):
            routes.append(new_route)
        if len(routes) == num_robots:
            break
    return routes

def calculate_route_cost(route, cost_matrix):
    return sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

cost_matrix = create_costvox_matrix(coordinates)
savings = clarke_wright_savings(cost_matrix)
routes = build_initial_routes(savings, demands, robot_capacity)

# Display results
overall_cost = 0
for i, route in enumerate(routes):
    cost = calculate_route_cost(route, cost_matrix)
    overall_cost += cost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall.ost}")