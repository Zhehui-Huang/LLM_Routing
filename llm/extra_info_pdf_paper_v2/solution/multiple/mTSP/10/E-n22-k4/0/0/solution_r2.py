import numpy as np
import random
from math import sqrt

# Coordinates for the cities including the depot
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Number of robots
num_robots = 4

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate a valid initial solution: evenly distribute cities among robots
def generate_initial_solution():
    all_cities = list(cities.keys())[1:]  # excluding the depot
    random.shuffle(all_cities)
    return [all_cities[i::num_robots] for i in range(num_robots)]

# Calculate cost for a given tour
def tour_cost(tour):
    cost = calc_distance(0, tour[0]) + calc_distance(tour[-1], 0)
    cost += sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return cost

# Two-opt optimization on a single tour
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 1):
            for j in range(i+1, len(tour)):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if tour_cost(new_tour) < tour_cost(best):
                    best = new_tour
                    improved = True
    return best

# Optimize all tours
def optimize_solution(tours):
    return [two_opt(tour) for tour in tours]

# Main setup
initial_solution = generate_initial_solution()
optimized_solution = optimize_solution(initial_solution)

# Output results
total_cost = 0
for index, tour in enumerate(optimized_solution):
    cost = tour_cost(tour)
    total_cost += cost
    print(f"Robot {index} Tour: [0, {' '.join(map(str, tour))}, 0]")
    print(f"Robot {index} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")