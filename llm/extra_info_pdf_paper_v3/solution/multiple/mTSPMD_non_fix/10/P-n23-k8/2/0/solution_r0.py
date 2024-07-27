import math
import random
import numpy as np

# City locations
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Parameters
num_robots = 8

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

def simulated_annealing(cities, initial_temp, min_temp, cooling_rate):
    current_solution = list(cities.keys())
    random.shuffle(current_solution)
    current_cost = total_tour_cost(current_solution)
    temperature = initial_temp
    while temperature > min_temp:
        next_solution = current_solution[:]
        l, r = sorted(random.sample(range(len(next_solution)), 2))
        next_solution[l:r+1] = reversed(next_solution[l:r+1])
        next_cost = total_tour_cost(next_solution)
        if next_cost < current_cost or random.random() < math.exp((current_cost - next_cost) / temperature):
            current_solution, current_cost = next_solution, next_cost
        temperature *= cooling_rate
    return current_solution, current_cost

def divide_tours_among_robots(total_tour):
    chunk_size = len(total_tour) // num_robots
    robot_tours = [total_tour[i*chunk_size:(i+1)*chunk_size] for i in range(num_robots)]
    if len(total_tour) % num_robots != 0:
        robot_tours[-1].extend(total_tour[num_robots*chunk_size:])
    return robot_tours

# Running Simulated Annealing
initial_temperature = 1000
minimum_temperature = 1
cooling_rate = 0.95
best_tour, best_cost = simulated_annealing(cities, initial_temperature, minimum_temperature, cooling_rate)

# Dividing tours among robots
robot_tours = divide_tours_among_robots(best_tour)
robot_tours_costs = [total_tour_cost(tour) for tour in robot_tours]

overall_cost = sum(robot_tours_costs)
for i, tour in enumerate(robot_tours):
    print(f"Robot {i} Tour: [{0}] + {tour} + [{0}]")
    print(f"Robot {i} Total Travel Cost: {robot_tours_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")