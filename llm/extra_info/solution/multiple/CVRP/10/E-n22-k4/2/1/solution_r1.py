from math import sqrt

# Define cities and coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Define demands for each city
demands = {
    0: 0,
    1: 1100,
    2: 700,
    3: 800,
    4: 1400,
    5: 2100,
    6: 400,
    7: 800,
    8: 100,
    9: 500,
    10: 600,
    11: 1200,
    12: 1300,
    13: 1300,
    14: 300,
    15: 900,
    16: 2100,
    17: 1000,
    18: 900,
    19: 2500,
    20: 1800,
    21: 700
}

# Number of robots and their capacity
num_robots = 4
robot_capacity = 6000

# Function to compute Euclidean distance between two cities
def calculate_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def assign_tours():
    # Track cities yet to be serviced
    remaining_cities = set(cities.keys()) - {0}
    # Initialize tours for each robot
    tours = {i: [0] for i in range(num_robots)}
    # Track loads for each robot
    loads = {i: 0 for i in range(num_robots)}
    # Calculate total travel cost
    total_cost = 0

    while remaining_cities:
        for robot in range(num_robots):
            if not remaining_cities:
                break
            current_city = tours[robot][-1]
            next_city = min(remaining_cities, key=lambda x: calculate_distance(current_city, x))
            next_city_distance = calculate_distance(current_city, next_city)
            if loads[robot] + demands[next_city] <= robot_capacity:
                tours[robot].append(next_city)
                loads[robot] += demands[next_city]
                total_cost += next_city_distance
                remaining_cities.remove(next_city)
            elif current_city != 0:
                # Return to depot if no viable city can be added and the robot isn't already at the depot
                return_distance = calculate_beeline(current_city, 0)
                total_cost += return_distance
                tours[robot].append(0)

    # Make sure each robot returns to the depot
    for robot in range(num_robots):
        if tours[robot][-1] != 0:
            tours[robot].append(0)
            total_cost += calculate_distance(tours[robot][-2], 0)

    # Output the results
    for robot in range(num_robots):
        route_cost = sum(calculate_distance(tours[robot][i], tours[robot][i + 1]) for i in range(len(tours[robot]) - 1))
        print(f"Robot {robot} Tour: {tours[robot]}")
        print(f"Robot {robot} Total Travel Cost: {route_cost:.2f}")

    print(f"Overall Total Travel Cost: {total_cost:.2f}")

assign_tours()