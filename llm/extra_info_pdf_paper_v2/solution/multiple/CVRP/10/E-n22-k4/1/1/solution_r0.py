import numpy as np

# City coordinates and demand data
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
           600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
           1800, 700]
num_cities = len(coordinates)
capacity = 6000
num_robots = 4

# Calculate distances matrix
def distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i, j] = np.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)
    return dist_matrix

distances = distance_matrix(coordinates)

# Clarke-Wright Savings Calculation
def calculate_savings(dist_matrix):
    savings = {}
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            s = dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j]
            savings[(i, j)] = s
    return savings

# Sort savings in descending order
savings = calculate_savings(distances)
sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)

# Implementing the Enhanced Clarke-Wright algorithm
def clarke_wright():
    routes = {r: [0] for r in range(num_robots)}
    demands_left = demands[1:]
    capacities_left = [capacity] * num_robots
    
    for ((i, j), s) in sorted_savings:
        if demands_left[i-1] > 0 and demands_left[j-1] > 0:
            # Find pair of routes to merge (i and j must be tail and head respectively, or not already in middle of a route)
            for r in routes:
                if capacities_left[r] >= demands_left[i-1] + demands_left[j-1] and i in routes[r] and 0 == routes[r][-1]:
                    if j not in routes[r]:
                        routes[r].extend([j, 0])
                        capacities_left[r] -= (demands_left[i-1] + demands_left[j-1])
                        demands_left[i-1] = 0
                        demands_left[j-1] = 0
                        break
    return routes

routes = clarke_wright()

# Calculate total cost
def calculate_costs(routes):
    total_cost = 0
    costs = {}
    for r, tour in routes.items():
        cost = sum(distances[tour[k]][tour[k + 1]] for k in range(len(tour) - 1))
        costs[r] = cost
        total_cost += cost
    return costs, total_cost

route_costs, total_route_cost = calculate_costs(routes)

# Output results
for r in range(num_robots):
    print(f"Robot {r} Tour: {routes[r]}")
    print(f"Robot {r} Total Travel Cost: {route_costs[r]:.2f}")

print(f"Overall Total Travel Cost: {total_route_cost:.2f}")