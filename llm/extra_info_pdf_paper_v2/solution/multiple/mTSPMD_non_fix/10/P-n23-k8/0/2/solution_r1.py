import math
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize robot routes starting from city 0
initial_routes = {i: [0] for i in range(num_robots)}
remaining_cities = list(cities.keys())[1:]  # exclude the starting depot

# Distribute cities among robots as initial solution
while remaining_cities:
    for i in range(num_robots):
        if remaining_cities:
            selected_city = random.choice(remaining_cities)
            initial_routes[i].append(selected_city)
            remaining_cities.remove(selected_city)

# Simulated Annealing algorithm to optimize routes
def simulated_annealing(robot_routes):
    T = 1000.0  # Initial temperature
    T_min = 0.1  # Minimum temperature
    alpha = 0.9  # Cooling rate
    
    while T > T_min:
        for i in range(num_robots):
            # Run random swaps for each robot's route
            if len(robot_routes[i]) > 2:
                idx1, idx2 = random.sample(range(1, len(robot_routes[i])), 2)
                robot_routes[i][idx1], robot_routes[i][idx2] = robot_routes[i][idx2], robot_routes[i][idx1]

                # Calculate costs before and after the swap
                route_cost = sum(euclidean_distance(robot_routes[i][j], robot_routes[i][j+1])
                                 for j in range(len(robot_routes[i])-1))
                
                # Attempt to revert swap based on acceptance probability
                if math.exp(-route_cost / T) < random.random():
                    robot_routes[i][idx1], robot_routes[i][idx2] = robot_routes[i][idx2], robot_routes[i][idx1]

        T *= alpha

    return robot_routes

# Optimize initial routes
final_routes = simulated_annealing(initial_routes)

# Calculate and print the costs
def calculate_costs(routes):
    total_overall_cost = 0
    for i in range(num_robots):
        route_cost = sum(euclidean_distance(routes[i][j], routes[i][j+1]) 
                         for j in range(len(routes[i]) - 1))
        total_overall_cost += route_cost
        print(f"Robot {i} Tour: {routes[i] + [routes[i][0]]}")
        print(f"Robot {i} Total Travel Cost: {route_cost:.2f}")
    print(f"Overall Total Travel Crate: {total_overall_cost:.2f}")

calculate_costs(final_short)