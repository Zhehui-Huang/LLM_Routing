import math
from random import shuffle, randint

# Data and parameters setup
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
num_robots = 4
robot_capacity = 6000

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Generate distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Create Initial Solution
def create_initial_solution():
    routes = [[] for _ in range(num_robots)]
    capacities = [robot_capacity] * num_robots
    city_indices = list(range(1, len(coordinates)))  # excluding depot which is at index 0
    remaining_cities = set(city_indices)

    # Start from depot and randomly assign cities to each robot until capacity or cities are exhausted
    while remaining_cities:
        for robot in range(num_robots):
            if not routes[robot]:
                routes[robot].append(0)  # start from depot
            current_city = routes[robot][-1]

            # Attempt to find a nearby city that fits the robot's remaining capacity
            possible_moves = [(i, distance_matrix[current_city][i]) for i in remaining_cities if demands[i] <= capacities[robot]]
            if not possible_moves:
                continue

            # Select the closest feasible city
            next_city = min(possible_moves, key=lambda x: x[1])[0]
            routes[robot].append(next_city)
            capacities[robot] -= demands[next_city]
            remaining_cities.remove(next_city)

    # Ensure all routes return to depot
    for route in routes:
        if route and route[-1] != 0:
            route.append(0)

    return routes

# Calculate route costs
def calculate_costs(routes):
    costs = []
    total_cost = 0
    for route in routes:
        if len(route) > 1:
            cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
        else:
            cost = 0
        costs.append(cost)
        total_cost += cost
    return costs, total_cost

# Generate the initial solution and calculate costs
routes = create_initial_solution()
costs, total_cost = calculate_costs(routes)

# Display outputs
for idx, route in enumerate(routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")