import math
from itertools import permutations

# Coordinates and demands of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Capacity of each robot
robot_capacity = 35
n_robots = 8

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Generate cost matrix
def generate_cost_matrix():
    n_cities = len(coordinates)
    cost_matrix = [[euclidean_distance(i, j) for j in range(n_cities)] for i in range(n_cities)]
    return cost_matrix

# Clarke-Wright Savings Algorithm
def clarke_wright():
    n_cities = len(coordinates)
    cost_matrix = generate_value_matrix()
    savings = {}
    for i in range(1, n_cities):
        for j in range(i+1, n_cities):
            if i != j:
                sij = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
                savings[(i, j)] = sij

    # Sorting savings in descending order
    sorted_savings = sorted(savings.items(), key=lambda item: item[1], reverse=True)
    
    routes = []
    load = [0] * n_robots
    route_load = {}
    
    for ((i, j), saving) in sorted_savings:
        # Find suitable robot and route to accommodate the cities
        added = False
        for route_index, route in enumerate(routes):
            if load[route_index] + demands[i] + demands[j] <= robot_capacity:
                if i in route or j in route:
                    continue
                # Adding to route
                if route[-1] == 0 and demands[i] + load[route_index] <= robot_capacity:
                    route.append(i)
                    load[route_index] += demands[i]
                    added = True
                if route[0] == 0 and demands[j] + load[route_index] <= robot_capacity:
                    route.insert(0, j)
                    load[route_index] += demands[j]
                    added = True
                if added:
                    break
                
        if not added:
            # Create new route if possible
            if len(routes) < n_robots:
                new_route_index = len(routes)
                if demands[i] + demands[j] <= robot_capacity:
                    routes.append([0, i, j, 0])
                    load[new_route_index] = demands[i] + demands[j]
                    continue
                    
    return routes, load

def calculate_route_cost(route, cost_matrix):
    return sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

# Solve the problem
routes, loads = clarke_wright()
cost_matrix = generate_cost_matrix()
total_cost = 0

print("Robot tours and costs:")
for i, route in enumerate(routes):
    route_cost = calculate_route_cost(route, cost_matrix)
    total_cost += route_cost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Gate: {total_cost}")