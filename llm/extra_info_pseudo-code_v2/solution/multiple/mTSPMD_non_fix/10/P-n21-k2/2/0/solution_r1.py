import numpy as np
import random

cities = [
    (30, 40),  # Depot 0
    (37, 52),  # Depot 1
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

num_cities = len(cities) - 2
num_depots = 2
num_robots = 2

# Distance calculations
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Generate a valid initial solution
def initial_solution():
    all_cities = list(range(2, len(cities)))  # cities without depots
    random.shuffle(all_cities)
    split = num_cities // num_robots
    return [all_cities[i: i + split] for i in range(0, num_cities, split)]

def calculate_route_cost(route, depot_start, depot_end):
    cost = 0
    current_position = depot_start
    for city in route:
        cost += distance_matrix[current_position][city]
        current_position = city
    cost += distance_matrix[current_position][depot_end]
    return cost

def total_cost(solutions):
    total = 0
    tours = []
    for i, sol in enumerate(solutions):
        depot_start = 0  # All start from the same depot
        if i == num_robots - 1:
            depot_end = 1  # Last robot ends at depot 1
        else:
            depot_end = 0
        cost = calculate_route_cost(sol, depot_start, depot_end)
        total += cost
        tours.append((cost, [depot_start] + sol + [depot_end]))
    return total, tours

# Initial solution
solutions = initial_solution()
total, tours = total_cost(solutions)

for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour[1]}")
    print(f"Robot {idx} Total Travel Cost: {tour[0]}")
print(f"Overall Total Travel Cost: {total}")