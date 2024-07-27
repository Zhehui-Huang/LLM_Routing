import numpy as np

# Given data
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 
           26, 17, 6, 15, 5, 10]
robot_capacity = 40

# Calculate distance matrix
def distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = np.hypot(coords[i][0] - coords[j][0], coords[i][1] - coords[j][1])
    return dist_matrix

# Clarke-Wright Savings Algorithm
def clarke_wright_savings(coords, demands, capacity):
    n = len(coords)
    dist_matrix = distance_matrix(coords)
    savings = []
    
    for i in range(1, n):
        for j in range(i + 1, n):
            sij = dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j]
            savings.append((sij, i, j))
    savings.sort(reverse=True)  # sort savings in descending order

    routes = [[0] for _ in range(n)]  # initialize routes from depot
    load = [0] * n
    in_route = [False] * n
    
    for s, i, j in savings:
        if not in_route[i] and not in_route[j] and demands[i] + demands[j] <= capacity:
            routes.append([0, i, j, 0])
            in_route[i] = in_route[j] = True
            load.append(demands[i] + demands[j])
        elif in_route[i] and not in_route[j] and load[i] + demands[j] <= capacity:
            routes[i].insert(-1, j)
            in_route[j] = True
            load[i] += demands[j]
        elif not in_route[i] and in_route[j] and load[j] + demands[i] <= capacity:
            routes[j].insert(1, i)
            in_route[i] = True
            load[j] += demands[i]

    # Assign remaining cities directly
    for i in range(1, n):
        if not in_route[i]:
            routes.append([0, i, 0])
            load.append(demands[i])

    # Filter out unused routes
    routes = [route for route in routes if len(route) > 1]
    return routes, dist_matrix

# Calculate routes and print output
routes, dist_matrix = clarke_wright_savings(coordinates, demands, robot_capacity)
overall_cost = 0

for idx, route in enumerate(routes):
    route_cost = sum(dist_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    overall_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")