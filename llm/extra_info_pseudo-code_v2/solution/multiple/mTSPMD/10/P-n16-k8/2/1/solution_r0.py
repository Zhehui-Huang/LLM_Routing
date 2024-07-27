import numpy as np
import math
from random import choice, seed

# Initialization of city and robot data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

depot_starts = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7
}

num_robots = 8
alpha = 1.0
beta = 2.0
rho = 0.1
antnum = 32
cyclenum = 100
init_pheromone = 1.0

# Euclidean distance calculation
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize distance matrix
n = len(cities)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i, j] = calc_distance(i, j)

# Initialize pheromone trails
pheromones = np.full((n, n), init_pheromone)

# Heuristic information 1/distance
eta = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            eta[i, j] = 1 / distances[i, j]
        else:
            eta[i, j] = 0

def choose_next_city(current_city, allowed_cities, pheromones, eta):
    pheromones_current = pheromones[current_city][allowed_cities]
    eta_current = eta[current_city][allowed_cities]
    probabilities = pheromones_current**alpha * eta_current**beta
    probabilities /= probabilities.sum()
    return np.random.choice(allowed_cities, p=probabilities)

def construct_solution(pheromones, eta):
    tour = {}
    tour_length = {}
    allowed_cities = set(range(n))
    
    for robot in range(num_robots):
        current_city = depot_starts[robot]
        tour[robot] = [current_city]
        tour_length[robot] = 0

    while allowed_cities:
        for robot in range(num_robots):
            if len(tour[robot]) == 1 or tour[robot][-1] != depot_starts[robot]:
                if len(allowed_cities) == 1:
                    next_city = allowed_cities.pop()
                else:
                    allowed = list(allowed_cities)
                    next_city = choose_next_city(tour[robot][-1], allowed, pheromones, eta)
                    allowed_cities.remove(next_city)
                tour[robot].append(next_city)
                tour_length[robot] += distances[tour[robot][-1], next_city]
                if next_city in depot_starts.values():
                    break

    # Close tours
    for robot in range(num_robots):
        start_city = depot_starts[robot]
        tour[robot].append(start_city)
        tour_length[robot] += distances[tour[robot][-1], start_city]

    return tour, tour_length

def update_pheromones(tour, tour_length, pheromones):
    for robot, path in tour.items():
        added_pheromone = 1 / tour_length[robot]
        for i in range(len(path) - 1):
            pheromones[path[i], path[i+1]] += added_pheromone

def main():
    best_solution = None
    best_total_cost = float('inf')
    best_tour_lengths = None
    
    for _ in range(cyclenum):
        tour, tour_length = construct_solution(pheromones, eta)
        total_tour_length = sum(tour_length.values())
        
        if total_tour_length < best_total_cost:
            best_solution = tour
            best_total_cost = total_tour_length
            best_tour_lengths = tour_length
            improvement_stage = 0
        else:
            improvement_stage += 1

        # Update pheromones
        pheromones *= (1 - rho)
        update_pheromones(tour, tour_length, pheromones)
        
        if improvement_stage >= cyclenum:
            break
    
    print(f"Overall Total Travel Cost: {best_total_cost}")
    for robot in range(num_robots):
        print(f"Robot {robot} Tour: {best_solution[robot]}")
        print(f"Robot {robot} Total Travel Cost: {best_tour_lengths[robot]}")

seed(1)
main()