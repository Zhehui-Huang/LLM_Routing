import math
import random
import copy

# Define city coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate an initial feasible solution (randomly assign cities to each robot)
def initial_solution():
    all_cities = list(range(2, 19))  # Exclude depots (already assigned)
    random.shuffle(all_cities)
    midpoint = len(all_cities) // 2
    robot0_route = [0] + all_cities[:midpoint] + [0]
    robot1_route = [1] + all_cities[midpoint:] + [1]
    return robot0_route, robot1_route

# Calculate the total cost of each robot's route
def calculate_cost(route):
    return sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route)-1))

# Optimize the routes using Simulated Annealing
def simulated_annealing(robot_routes):
    temp = 1000
    cooling_rate = 0.995
    while temp > 1:
        new_routes = copy.deepcopy(robot_routes)
        for i in range(2):
            # Pick two cities to swap (excluding the depot return trips)
            swap_pos1, swap_pos2 = random.sample(range(1, len(robot_routes[i]) - 2), 2)
            new_routes[i][swap_pos1], new_routes[i][swap_pos2] = new_routes[i][swap_pos2], new_routes[i][swap_pos1]
        # Calculate new cost and current cost
        current_cost = sum(calculate_cost(r) for r in robot_routes)
        new_cost = sum(calculate_cost(r) for r in new_routes)
        # Acceptance probability
        if new_cost < current_cost or math.exp((current_cost - new_cost) / temp) > random.random():
            robot_routes = new_routes
        temp *= cooling_rate
    return robot_routes

# Main execution function
def main():
    robot_routes = initial_solution()
    optimized_routes = simulated_annealing(robot_routes)
    costs = [calculate_cost(route) for route in optimized_routes]
    total_cost = sum(costs)

    print(f"Robot 0 Tour: {optimized_routes[0]}")
    print(f"Robot 0 Total Travel Cost: {costs[0]}")
    print(f"Robot 1 Tour: {optimized_routes[1]}")
    print(f"Robot 1 Total Travel Cost: {costs[1]}")
    print(f"Overall Total Travel Cost: {total_cost}")

main()