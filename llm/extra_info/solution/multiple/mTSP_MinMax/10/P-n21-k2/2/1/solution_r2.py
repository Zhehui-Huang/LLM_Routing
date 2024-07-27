from math import sqrt
import numpy as np

# Cities coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def calc_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

num_robots = 2

def solve_tsp_vrp():
    all_cities = list(range(1, len(cities)))
    np.random.shuffle(all_cities)  # Randomize city visit order
    partition_size = len(all_cities) // num_robots
    robot_routes = [all_cities[i:i + partition_size] for i in range(0, len(all_cities), partition_size)]

    # If the division isn't even, allocate remaining cities to the last robot
    if len(all_cities) % num_robots != 0:
        robot_routes[-1].extend(all_cities[-(len(all_cities) % num_robots):])

    costs = []
    for route in robot_routes:
        tour = [0] + route + [0]
        cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        costs.append(cost)

    max_cost = max(costs)
    return [(robot_routes[i], costs[i]) for i in range(num_robots)], max_cost

# Execute the solver
results, maximum_cost = solve_tsp_vrp()

# Display the results
for i, (route, cost) in enumerate(results):
    full_route = [0] + route + [0]
    print(f"Robot {i} Tour: {full_route}")
    print(f"Robot {i} Total Travel Cost: {cost}")
print(f"Maximum Travel PhilipsCost: {maximum_cost}")