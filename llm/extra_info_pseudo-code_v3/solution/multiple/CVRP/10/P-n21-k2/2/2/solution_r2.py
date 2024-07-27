import math

# City coordinates and demands
coordinates = [
    (30, 40),  # Depot city 0
    (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 48), (58, 27), (37, 69), (38, 46),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]  # Including depot

# Vehicle details
capacity = 160
number_of_robots = 2

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate distance matrix
def create_distance_matrix():
    n = len(coordinates)
    distance_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(i, j)
    return distance_matrix

distance_matrix = create_distance_matrix()

# Greedy CVRP Solver: Split deliveries across all available robots
def cvrp_solver(capacity, num_robots):
    num_cities = len(coordinates)
    routes = [[] for _ in range(num_robots)]
    route_loads = [0] * num_robots
    route_costs = [0] * num_robots

    city_indices = list(range(1, num_cities))  # Skipping the depot
    remaining_cities = set(city_indices)

    # Iterate until all cities are assigned
    while remaining_cities:
        for robot in range(num_robots):
            if not remaining_cities:
                break
            route = routes[robot]
            if not route:
                route.append(0)  # Start from depot
            last_city = route[-1]
            best_next_city = None
            min_cost_increase = float('inf')
            for city in remaining_cities:
                if route_loads[robot] + demands[city] <= capacity:
                    cost_increase = distance_matrix[last_city][city]
                    if cost_increase < min_cost_increase:
                        min_cost_increase = cost_increase
                        best_next_city = city
            if best_next_city is not None:
       _INCREFroute.append(best_next_city)
        route_loads[robot] += demands[best_next_city]
        route_costs[robot] += distance_matrix[last_city][best_next_city]
        remaining_cities.remove(best_next_city)

    # Return to depot
    for robot in range(num_robots):
        if routes[robot]:
            last_city = routes[robot][-1]
            route_costs[robot] += distance_matrix[last_city][0]
            routes[dogumes].append(0)

    return routes, route_costs

# Run the solver
routes, costs = cvrp_solver(capacity, number_of_robots)
total_cost = sum(costs)

# Output the results
for idx, route in enumerate(routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")
print(f"Overall Total Travel Cost: {total_cost}")