import math

# Function to compute Euclidean distance between two cities given their coordinates
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initializes and assigns tours to the robots using a simple nearest neighbor heuristic
def nearest_neighbor_tour(cities, depot, num_robots):
    routes = {i: [depot] for i in range(num_robots)}
    visited = set([depot])
    remaining_cities = set(cities.keys()) - visited
    while remaining_cities:
        for i in range(num_robots):
            if not remaining_cities:
                break
            last_city = routes[i][-1]
            next_city = min(remaining_cities, key=lambda x: euclidean_distance(cities[last_city], cities[x]))
            routes[i].append(next_city)
            remaining_cities.remove(next_city)
    for i in range(num_robots):
        routes[i].append(depot)  # Return to depot at the end of the tour
    return routes

# Calculate the travel cost of the route for each robot
def calculate_route_cost(cities, route):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(cities[route[i]], cities[route[i + 1]])
    return cost

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}
num_robots = 2
depot = 0

# Assign initial tours to robots
routes = nearest_neighbor_tour(cities, depot, num_robots)

# Calculate and display each robot's tour and cost
overall_cost = 0
for robot_id, tour in routes.items():
    cost = calculate_route_cost(cities, tour)
    overall_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")