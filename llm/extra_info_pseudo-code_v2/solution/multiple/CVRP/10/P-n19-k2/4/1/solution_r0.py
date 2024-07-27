import math

# Coordinates and demands of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
number_of_robots = 2
robot_capacity = 160

# Compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Initialization of routes
routes = [[] for _ in range(number_of_robots)]
routes[0] = [0]
routes[1] = [0]

def calculate_route_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += distance(route[i], route[i+1])
    total_cost += distance(route[-1], 0)  # Return to depot
    return total_cost

def construct_initial_routes():
    remaining_cities = set(range(1, len(coordinates)))
    current_loads = [0] * number_of_robots
    current_robot = 0

    while remaining_cities:
        best_saving = None
        best_city = None
        for city in remaining_cities:
            if current_loads[current_robot] + demands[city] <= robot_capacity:
                last_city = routes[current_robot][-1]
                saving = distance(last_city, 0) + distance(0, city) - distance(last_city, city)
                if best_saving is None or saving > best_saving:
                    best_saving = saving
                    best_city = city

        if best_city is not None:
            routes[current_robot].append(best_city)
            remaining_cities.remove(best_city)
            current_loads[current_robot] += demands[best_city]
        else:
            current_robot = (current_robot + 1) % number_of_robots
            routes[current_robot].append(0)  # Start a new trip if needed

    # Closing all routes
    for route in routes:
        if route[-1] != 0:
            route.append(0)

construct_initial_routes()

total_cost = 0
for robot_id, route in enumerate(routes):
    tour_cost = calculate_route_cost(route)
    total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")