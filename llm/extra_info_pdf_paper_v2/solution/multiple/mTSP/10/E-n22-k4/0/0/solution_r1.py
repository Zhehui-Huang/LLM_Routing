import numpy as np
import random
from math import sqrt
from itertools import permutations

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

# Euclidean distance calculator
def calc_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate initial random solution
def random_solution():
    city_indices = list(cities.keys())[1:]  # Exclude the depot
    random.shuffle(city_indices)
    parts = [city_indices[i::num_robots] for i in range(num_robots)]
    return parts

# Calculate the cost of a solution
def solution_cost(solution):
    total_cost = 0
    individual_costs = []
    for tour in solution:
        if tour:
            cost = calc_distance(0, tour[0])  # From depot to first city
            for i in range(1, len(tour)):
                cost += calc_distance(tour[i-1], tour[i])
            cost += calc_distance(tour[-1], 0)  # Return to depot
            individual_costs.append(cost)
            total_cost += cost
        else:
            individual_costs.append(0)
    return total_cost, individual_costs

# Improve tours using two-opt
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if solution_cost([new_tour])[1][0] < solution_cost([best])[1][0]:
                    best = new_tour
                    improved = True
        tour = best
    return best

# Optimize each tour using two-opt
def optimize_solution(solution):
    return [two_opt(tour) for tour in solution]

# Main execution
initial_solution = random_solution()
optimized_solution = optimize_solution(initial_solution)
total_cost, individual_costs = solution_type(optimized_solution)

# Printing the solution
for idx, tour in enumerate(optimized_solution):
    formatted_tour = [0] + tour + [0]
    print(f"Robot {idx} Tour: {formatted_tour}")
    print(f"Robot {idx} Total Travel Cost: {individual_costs[idx]}")

print(f"Overall Total Travel Cost: {total_cost}")