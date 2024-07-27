import numpy as np

# Define the data: coordinates of cities and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Robot information
num_robots = 4
capacity = 6000

# Distance calculation function
def calculate_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Compute the distance matrix
def distance_matrix(coords):
    num_cities = len(coords)
    d_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            d_matrix[i][j] = calculate_distance(coords[i], coords[j])
    return d_matrix

# Compute savings (Clarke-Wright method)
def compute_savings(dm):
    n = len(dm)
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            saving = dm[0][i] + dm[0][j] - dm[i][j]
            savings.append((saving, i, j))
    savings.sort(reverse=True)
    return savings

# Applying the savings to route formation
def assign_routes(savings, demands, capacity):
    routes = []
    demand_on_route = {}
    
    for saving, i, j in savings:
        found_route = False
        for route in routes:
            if i in route and j not in route and demand_on_route[tuple(route)] + demands[j] <= capacity:
                route.append(j)
                demand_on_route[tuple(route)] += demands[j]
                found_route = True
                break
            elif j in route and i not in route and demand_on_route[tuple(route)] + demands[i] <= capacity:
                route.append(i)
                demand_on_route[tuple(route)] += demands[i]
                found_route = True
                break

        if not found_route:
            if demands[i] + demands[j] <= capacity:
                new_route = [0, i, j, 0]
                routes.append(new_route)
                demand_on_route[tuple(new_route)] = demands[i] + demands[j]

    return routes

dm = distance_matrix(coordinates)
savings = compute_savings(dm)
routes = assign_routes(savings, demands, capacity)

# Calculate total costs and output the results
total_cost = 0
for robot_index, route in enumerate(routes):
    path_cost = sum(dm[route[i]][route[i + 1]] for i in range(len(route) - 1))
    total_cost += path_cost
    print(f"Robot {robot_index} Tour: {route}")
    print(f"Robot {robotob_index} Total Travel Cost: {path_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")