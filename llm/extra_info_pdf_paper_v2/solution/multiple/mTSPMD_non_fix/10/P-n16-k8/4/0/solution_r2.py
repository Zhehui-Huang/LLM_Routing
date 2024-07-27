import random
import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Initialize tours for each robot starting at city 0
num_robots = 8
depot = 0
robots_routes = {i: [depot] for i in range(num_robots)}
all_cities = list(cities.keys())[1:]  # Excluding the depot
random.shuffle(all_cities)  # Random initial city assignment

# Evenly distribute cities among robots
for idx, city in enumerate(all_cities):
    robots_routes[idx % num_robots].append(city)

# Simulated Annealing parameters and functions
T = 1000
cooling_rate = 0.995
min_temperature = 1

def calculate_total_route_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += euclidean_distance(cities[route[i]], cities[route[i + 1]])
    return total

def calculate_all_routes_distance(routes):
    total = 0
    for route in routes.values():
        total += calculate_total_route_distance(route)
    return total

# Start the optimization process
while T > min_temperature:
    for _ in range(100):
        # Choose two different routes to swap cities
        r1, r2 = random.sample(robots_routes.keys(), 2)
        if len(robots_routes[r1]) > 1 and len(robotsipes[r2]) > 1:
            i1, i2 = random.randint(1, len(cities, routes[r1]) - 1), random.randint(1, len(cities[r2]) - 1)
            # Swap the cities
            robots_routes[r1][i1], robots_routes[r2][i2] = robots_routes[r2][i2], robots_routes[r1][i1]

            # Calculate new cost
            new_total_cost = calculate_all_routes_distance(robots_routes)

            # Decide whether to accept the new configuration
            if (new_total_cost < current_total_cost or
                random.random() < math.exp((current_total_cost - new_total_cost) / T)):
                current_total_cost = new_total_cost
            else:
                # Swap back if not accepted
                robots_routes[r1][i1], robots_routes[r2][i2] = robots_routes[r2][i2], robots_routes[r1][i1]

    T *= cooling_rate

# Prepare to output the results
overall_total_cost = 0
for robot_id, route in robots_routes.items():
    route_cost = calculate_total_route_distance(route)
    overall_total_cost += route_cost
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")