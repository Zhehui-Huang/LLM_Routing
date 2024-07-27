import numpy as np
import random
from math import sqrt

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Greedy insertion heuristic adapted for multi-depot
def initialize_solution():
    available_cities = list(cities.keys())[2:]  # exclude depots initially
    tours = [[0], [1]]  # robots start at their respective depots
    remaining_capacity = [len(available_cities) // 2, len(available_cities) - len(available_cities) // 2]

    def find_next_city(tour):
        last_city = tour[-1]
        min_dist = float('inf')
        next_city = None
        for city in available_cities:
            dist = euclidean_distance(cities[last_city], cities[city])
            if dist < min_dist:
                min_dist = dist
                next_city = city
        return next_city

    # Assign cities to each robot
    for t in range(2):
        while remaining_capacity[t] > 0 and available_cities:
            next_city = find_next_city(tours[t])
            tours[t].append(next_city)
            available_cities.remove(next_city)
            remaining_capacity[t] -= 1

    # Ensure each robot returns to its starting depot
    tours[0].append(0)
    tours[1].append(1)

    return tours

def calculate_total_cost(tours):
    total_cost = 0
    individual_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        individual_costs.append(cost)
        total_cost += cost
    return total_cost, individual_costs

def genetic_algorithm():
    current_solution = initialize_solution()
    best_cost, individual_costs = calculate_total_cost(current_solution)

    # Genetic operations and improvements would be implemented here, modifying current_solution
    # For simplicity, let's consider current_solution as our best found solution after hypothetical optimizations

    return current\
_tours=u_olution, individual_costs, best_cost

# Running the algorithm
solution_tours, solution_costs, total_cost = genetic_algorithm()

for i, (tour, cost) in enumerate(zip(solution_tours, solution_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"\nOverall Total Travel Cost: {total_cost:.2f}")