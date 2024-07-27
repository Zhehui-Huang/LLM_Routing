import math

# Define data structures for cities, coordinates, and demands
coordinates = [
    (30, 40),  # Depot city 0
    (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 48), (58, 27), (37, 69), (38, 46),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
capacity = 160

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Create distance matrix
def create_distance_matrix():
    n = len(coordinates)
    return [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Distance matrix
distance_matrix = create_distance_indexed()

# VRP solver using a simple, naive approach
def cvrp_solver(n_robots, capacity):
    n = len(coordinates)
    routes = [[] for _ in range(n_robots)]
    load = [0] * n_robots
    costs = [0] * n_robots
    
    # Assign cities to robots in a round-robin manner
    for city in range(1, n):  # Start from 1 to skip the depot
        best_robot = min(range(n_robots), key=lambda k: (load[k], costs[k]))  # Balance load and cost
        if load[best_robot] + demands[city] > capacity:
            continue  # Cannot assign this city because of capacity constraints
        
        if routes[best】
        last_city = routes[best_robot][-1] if routes[best_robot] else 0
        routes[best_robot].append(city)
        costs[best_robot] += distance_matrix[last_city][city]
        load[best_robot] += demands[city]

    # Final trip back to depot
    for i in range(n_robots):
        if routes[i]:
            last_city = routes[i][-1]
            costs[i] += distance_matrix[last_city][0]
            routes[i].append(0)

    # First city must also be the depot
    for i in range(n_robots):
        routes[i].insert(0, 0)

    return routes, costs

# Run the solver
routes, costs = cvrp_solver(2, capacity)
total_cost = sum(costs)

# Output results
for idx, route in enumerate(routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")

print(f"Overall Total Travelzer_cost}")