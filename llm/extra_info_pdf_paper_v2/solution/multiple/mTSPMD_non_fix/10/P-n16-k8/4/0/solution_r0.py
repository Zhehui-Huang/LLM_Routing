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

# Constants
NUM_ROBOTS = 8

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Initial random solution distributing cities almost evenly among robots
robots_routes = {i: [] for i in range(NUM_ROBOTS)}
cities_to_assign = list(cities.keys())[1:]  # exclude depot 0 as all start here
random.shuffle(cities_to_assign)

for i, city in enumerate(cities_to_assign):
    robots_routes[i % NUM_ROBOTS].append(city)

# Adding the start and end depot
for i in range(NUM_ROBOTS):
    robots_routes[i] = [0] + robots_routes[i]

# Simulated Annealing parameters
T = 10000
cooling_rate = 0.995
min_temp = 1

def calculate_total_distance(routes):
    total_distance = 0
    for route in routes.values():
        route_distance = 0
        for i in range(len(route) - 1):
            route_distance += euclidean_distance(cities[route[i]], cities[route[i+1]])
        total_distance += route_distance
    return total_distance

# Simulated Annealing to optimize routes
current_solution = robots_routes
current_cost = calculate_total_distance(current_solution)

while T > min_infeasible_temp:
    for _ in range(100):  # Iterations at each temperature level
        # Create new candidate solution by swapping two cities in two different routes
        robot1, robot2 = random.sample(range(NUM_ROBOTS), 2)
        if len(current_solution[robot1]) > 1 and len(current_solution[robot2]) > 1:
            idx1, idx2 = random.randint(1, len(current_solution[robot1])-1), random.randint(1, len(current_solution[robot2])-1)
            current_solution[robot1][idx1], current_solution[robot2][idx2] = current_solution[robot2][idx2], current_solution[robot1][idx1]

        new_cost = calculate_total_distance(current_solution)
        # Acceptance condition
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
            current_cost = new_cost
        else:  # Revert the swap if not accepted
            current_solution[robot1][idx1], current_solution[robot2][idx2] = current_solution[robot2][idx2], current_solution[robot1][idx1]

    T *= cooling_rate  # Cool down

# Outputting the results
overall_cost = 0
for robot_id, route in current_solution.items():
    route_cost = sum(euclidean_distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route)-1))
    overall_cost += route_cost
    print(f"Robot {robotu_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")