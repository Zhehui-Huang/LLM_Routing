import numpy as np

# City coordinates
cities = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
          6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
          12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)}

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Create a distance matrix
n_cities = len(cities)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i][j] = calculate_distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')  # No self-loops

# Number of robots and depots
n_robots = 8
depots = list(range(n_robots))

# Function to create a route for each robot using nearest neighbor heuristic
def create_routes():
    routes = {i: [i] for i in depots}  # Start each robot at its respective depot
    unvisited = set(cities.keys() - set(depots))

    while unvisited:
        for depot in depots:
            if not unvisited:
                break
            current_city = routes[depot][-1]
            nearest_city = min(unvisited, key=lambda x: distance_matrix[current_city][x])
            routes[depot].append(nearest_city)
            unvisited.remove(nearest_city)

        # Ensuring each route ends back at the corresponding depot
        for depot in depots:
            routes[depot].append(depot)

    return routes

# Calculate costs of routes
def calculate_costs(routes):
    costs = {robot_id: 0 for robot_id in depots}
    for robot_id, route in routes.items():
        route_cost = 0
        for i in range(len(route) - 1):
            route_cost += distance_matrix[route[i]][route[i+1]]
        costs[robot_id] = round(route_cost, 2)
    return costs

# Compute routes and costs
routes = create_routes()
costs = calculate_costs(routes)

# Printing result
total_cost = sum(costs.values())
for robot_id in depots:
    print(f"Robot {robot_id} Tour: {routes[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {costs[robot_id]}")
print(f"Overall Total Travel Cost: {total_cost}")