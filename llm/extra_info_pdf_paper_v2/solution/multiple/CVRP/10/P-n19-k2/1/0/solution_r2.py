import math

# Coordinates and demands
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
          (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacity = 160
num_robots = 2

# Function to compute Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Creating the distance matrix
def create_distance_matrix(cities):
    n = len(cities)
    return [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

dist_matrix = create_distance_matrix(cities)

# Clarke-Wright Savings Calculator
def calculate_savings(cities, dist_matrix):
    savings = []
    for i in range(1, len(cities)):  # start from 1 to skip the depot
        for j in range(i + 1, len(cities)):
            s = dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j]
            savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

savings = calculate_savings(cities, dist_matrix)

# Function to assign routes to robots
def assign_routes(savings, demands, num_robots, robot_capacity):
    routes = [[] for _ in range(num_robots)]
    loads = [0] * num_robots
    assigned = [False] * len(cities)
    assigned[0] = True  # Depot is always assigned

    for saving, i, j in savings:
        if demands[i] + demands[j] > robot_capacity:
            continue
        for r in range(num_robots):
            if not assigned[i] and not assigned[j] and loads[r] + demands[i] + demands[j] <= robot_capacity:
                routes[r].extend([i, j])
                loads[r] += demands[i] + demands[j]
                assigned[i] = assigned[j] = True
                break
            elif not assigned[i] and assigned[j] and loads[r] + demands[i] <= robot_capacity:
                routes[r].append(i)
                loads[r] += demands[i]
                assigned[i] = True
                break
            elif not assigned[j] and assigned[i] and loads[r] + demands[j] <= robot_capacity:
                routes[r].append(j)
                loads[r] += demands[j]
                assigned[j] = True
                break

    # Ensure all cities are covered and all routes start and end at the depot (0)
    for r in range(num_robots):
        if routes[r]:
            routes[r].insert(0, 0)  # Start at depot
            routes[r].append(0)  # Return to depot

    return routes, loads

routes, loads = assign_routes(savings, demands, num_robots, robot_capacity)

# Calculating the cost of each route
def route_cost(route, matrix):
    return sum(matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Display results
total_cost = 0
for i, route in enumerate(routes):
    cost = route_cost(route, dist_matrix)
    total_cost += cost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {total_cost}")