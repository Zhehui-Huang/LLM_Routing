import math

# Given city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot parameters
number_of_robots = 8
capacity = 40
depot = 0

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate the distance matrix
n = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Clarke-Wright Savings Algorithm
def clark_wright_savings():
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            save = distance_matrix[depot][i] + distance_matrix[depot][j] - distance_matrix[i][j]
            savings.append((save, i, j))
    savings.sort(reverse=True)

    routes = []
    in_route = {}
    capacities = {}
    
    for save, i, j in savings:
        if demands[i] + demands[j] > capacity:
            continue
        route_i = in_route.get(i)
        route_j = in_route.get(j)
        if route_i is None and route_j is None:
            if len(routes) < number_of_robots:
                routes.append([depot, i, j, depot])
                in_route[i], in_route[j] = len(routes) - 1, len(routes) - 1
                capacities[len(routes) - 1] = demands[i] + demands[j]
        elif route_i is not None and route_j is None:
            if capacities[route_i] + demands[j] <= capacity:
                routes[route_i].insert(-1, j)
                in_route[j] = route_i
                capacities[route_i] += demands[j]
        elif route_i is None and route_j is not None:
            if capacities[route_j] + demands[i] <= capacity:
                routes[route_j].insert(1, i)
                in_route[i] = route_j
                capacities[route_j] += demands[i]

    return routes

routes = clark_wright_savings()

# Calculate costs and print routes
total_cost = 0
for idx, route in enumerate(routes):
    route_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost}")
    total_cost += route_cost

print(f"Overall Total Travel Cost: {total_tc}")