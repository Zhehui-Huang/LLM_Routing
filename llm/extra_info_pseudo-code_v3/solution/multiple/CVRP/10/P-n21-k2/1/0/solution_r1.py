import math

# Define the cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Define the demand at each city
demand = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Vehicles Information
number_of_robots = 2
capacity = [160, 160]

# Calculate the Euclidean distance between any two cities
def calculate_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Calculate the Euclidean distance matrix
distance_matrix = [[calculate_distance(i, j) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Heuristic solution construction
def greedy_solution():
    cities_to_visit = list(range(1, len(coordinates)))
    routes = [[] for _ in range(number_of_robots)]
    remaining_capacity = capacity.copy()

    for city in cities_to_visit:
        best_robot = None
        for robot in range(number_of_robots):
            if remaining_capacity[robot] >= demand[city]:
                if best_robot is None or (len(routes[robot]) > 0 and distance_matrix[routes[robot][-1]][city] < distance_matrix[routes[best_robot][-1]][city]):
                    best_robot = robot
        if best_robot is None:
            print("No feasible solution: demands cannot be met by available robots")
            return []
        
        routes[best_robot].append(city)
        remaining_capacity[best_robot] -= demand[city]

    # Ensure all routes start and end at the depot
    for route in routes:
        route.insert(0, 0)
        route.append(0)
    
    return routes

# Calculate total cost of the tours
def calculate_route_cost(routes):
    total_cost = 0
    costs = []
    for route in routes:
        route_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
        costs.append(route_cost)
        total_cost += route_cost
    return costs, total_cost

# Get the initial solution using greedy strategy
initial_routes = greedy_solution()

# Handling case where no feasible routes are found
if not initial_routes:
    print("Failed to find a feasible solution.")
else:
    route_costs, total_cost = calculate_route_cost(initial_routes)
    # Display tour information for each robot
    for idx, route in enumerate(initial_routes):
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {route_costs[idx]:.2f}")

    # Display the overall cost
    print(f"Overall Total Travel Cost: {total.Api:.2f}")