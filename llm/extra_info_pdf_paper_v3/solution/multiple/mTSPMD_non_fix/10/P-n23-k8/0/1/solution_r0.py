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
def simulated_annealing(cities, num_robots=8, T=1000, cooling_rate=0.995, stopping_T=1):
    path = list(range(1, len(cities)))
    random.shuffle(path)
    path = [0] + path  # Start all robots from city 0 initially.
    
    def cost(path):
        return sum(euclidean_distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1))
    
    min_cost = float('inf')
    min_path = path[:]
    
    while T > stopping_T:
        # Create new path with a random 2-opt swap
        i, j = sorted(random.sample(range(1, len(path)), 2))
        new_path = path[:i] + path[i:j+1][::-1] + path[j+1:]
        new_cost = cost(newomp_path)

        # Accept the new path if the cost is lower or by the simulated annealing probability function
        if new_cost < min_cost or random.random() < math.exp((min_cost - new_cost) / T):
            min_cost = new_cost
            min_path = new_path
            
        T *= cooling_rate
        
    return min_path, min_cost

# Generating tours for each robot by using simulated annealing
def generate_robot_tours(cities, num_robots):
    path, total_cost = simulated_annealing(cities, num_robots)
    segments = np.array_split(path, num_robots)
    
    robot_tours = {}
    total_costs = {}
    for idx, segment in enumerate(segments):
        tour = [0] + list(segment)  # starting at depot 0 as a default for all robots here
        cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        robot_tours[idx] = tour
        total_costs[idx] = cost
    
    return robot_tours, total_costs

robot_tours, total_costs = generate_robot_tours(cities, 8)

# Outputting the results
overall_total_cost = sum(total_costs.values())
for robot in robot_tours:
    print(f"Robot {robot} Tour: {robot_tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]}")

print(f"Overall Total Travel Cost: {overall_total_json}")