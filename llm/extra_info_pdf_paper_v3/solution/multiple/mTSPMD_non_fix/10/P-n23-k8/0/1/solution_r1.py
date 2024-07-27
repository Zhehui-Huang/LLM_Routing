import numpy as np
import math
import random

# Cities and their coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
          (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Simulated Annealing process to solve MmTSP
def simulated_annealing(cities, T=1000, cooling_rate=0.995, stopping_temperature=1):
    path = list(range(1, len(cities)))  # Start path from city 1 to the last city
    random.shuffle(path)  # Random initial path
    path = [0] + path  # Include depot at the beginning

    def path_cost(path):
        return sum(euclidean_distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1))

    min_cost = path_cost(path)
    min_path = path[:]
    
    while T > stopping_temperature:
        i, j = sorted(random.sample(range(1, len(path)), 2))  # Choose two indices to swap (not choosing the depot position)
        new_path = path[:i] + path[i:j+1][::-1] + path[j+1:]  # Create new path with a swap
        new_cost = path_cost(new_path)

        if new_cost < min_cost or random.random() < math.exp((min_cost - new_cost) / T):
            path, min_cost = new_path, new_cost
        
        T *= cooling_rate
        
    return path, min_cost

# Solution setup for multiple robots starting from city 0
def generate_robot_tours(cities, num_robots):
    path, total_cost = simulated_annealing(cities)
    segments = np.array_split(path[1:], num_robots)  # split path into segments excluding the depot city
    robot_tours = {}
    individual_costs = {}

    for idx, segment in enumerate(segments):
        tour = [0] + list(segment)
        cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        robot_tours[idx] = tour
        individual_costs[idx] = cost

    return robot_tours, individual_costs

# Running the simulation with 8 robots starting from depot (city 0)
robot_tours, total_costs = generate_robot_tours(cities, 8)

# Outputting the results
overall_total_cost = sum(total_costs.values())
for robot, tour in robot_tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")