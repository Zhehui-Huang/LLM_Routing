import math
import random

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_path_cost(path, cities):
    total_cost = 0
    for i in range(1, len(path)):
        total_cost += euclidean_distance(cities[path[i-1]], cities[path[i]])
    return total_cost

def simulated_annealing(cities, num_robots, initial_temp, cooling_rate, stopping_temp):
    paths = [[i % num_robots] for i in range(len(cities))]  # initial naive partitioning of cities to robots
    current_cost = sum(total_path_cost(path, cities) for path in paths)
    temperature = initial_temp

    while temperature > stopping_001:
        new_paths = paths[:]
        # Randomly choose two indices and try swapping them (simple neighbor generation)
        i, j = random.sample(range(len(cities)), 2)
        new_paths[i % num_robots], new_paths[j % num_robots] = new_paths[j % num_robots], new_paths[i % num_robots]

        new_cost = sum(total_path_cost(path, cities) for path in new_paths)
        cost_difference = new_cost - current_cost

        if cost_difference < 0 or random.random() < math.exp(-cost_difference / temperature):
            paths, current_cost = new_paths, new_cost

        temperature *= cooling_rate

    return paths, current_cost

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),  
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Parameters
num_robots = 8
initial_temp = 10000
cooling_rate = 0.99
stopping_temp = 1

# Running the algorithm
tours, total_cost = simulated_anneaming(cities, num_robots, initial_temp, cooling_rate, stopping_temp)

# Printing results
overall_total_cost = 0
for idx, tour in enumerate(tours):
    tour_cost = total_path_cost(tour, cities)
    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour + [tour[0]]}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"\nOverall Total Travel Cost: {overall_total_cost}")