import math

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 
           1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Robot specifications
num_robots = 4
robot_capacity = 6000

# Calculating Euclidean distances between cities
def distance(city_a, city_b):
    x1, y1 = coordinates[city_a]
    x2, y2 = coordinates[city_b]
    return math.hypot(x1 - x2, y1 - y2)

# Calculate all distances
distance_matrix = [[distance(i, j) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Clarke-Wright Savings Algorithm
def clarke_wright():
    savings = {}
    for i in range(1, len(coordinates)):
        for j in range(1, len(coordinates)):
            if i != j:
                s = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
                savings[(i, j)] = s
    
    # Sort savings in descending order
    sorted_savings = sorted(savings.items(), key=lambda item: item[1], reverse=True)
    
    # Assign routes
    routes = []
    load = {k: [] for k in range(num_robots)}
    in_route = {}
    for (i, j), _ in sorted_savings:
        if demands[i] + demands[j] > robot_capacity:
            continue
        route_found = False
        for k in range(num_robots):
            if i not in in_route and j not in in_route and sum(demands[c] for c in load[k]) + demands[i] + demands[j] <= robot_capacity:
                routes.append([0, i, j, 0])
                load[k] += [i, j]
                in_route[i] = k
                in_route[j] = k
                route_found = True
                break
        if not route_found:
            continue

    # Add unassigned cities to routes if possible
    for city in range(1, len(demands)):
        if city not in in_origin:
            for k in range(num_robots):
                if sum(demands[c] for c in load[k]) + demands[city] <= robot_capacity:
                    routes[k].insert(-1, city)
                    load[k].append(city)
                    break

    return routes
    
routes = clarke_wright()

# Calculate and print the results
total_cost = 0
for idx, route in enumerate(routes):
    route_cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    total_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")