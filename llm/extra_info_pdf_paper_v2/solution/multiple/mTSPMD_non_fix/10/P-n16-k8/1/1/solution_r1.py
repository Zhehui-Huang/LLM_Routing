import numpy as np
import math
import random

# Given data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69)
}
robots = 8
start_depot = 0

# Utilities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour)-1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def simulated_annealing():
    cities_list = list(cities.keys())[1:]  # exclude the depot initially
    random.shuffle(cities_list)
    partitions = np.array_split(cities_list, robots)
    tours = [[start_depot] + part.tolist() + [start_depot] for part in partitions]

    temperature = 100
    cooling_rate = 0.99
    min_temperature = 0.1

    while temperature > min_temperature:
        for i in range(robots):
            for _ in range(1000):  # Number of iterations per temperature
                if len(tours[i]) > 3:
                    a, b = np.sort(random.sample(range(1, len(tours[i])-1), 2))
                    new_tour = tours[i][:]
                    new_tour[a], new_tour[b] = new_tour[b], new_tour[a]
                    current_cost = calculate_tour_cost(tours[i])
                    new_cost = calculate_tour_cost(new_tour)
                    
                    if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
                        tours[i] = new_tour

        temperature *= cooling_rate

    return tours

# Running the optimization
solved_tours = simulated_annealing()
total_costs = [calculate_tour_cost(tour) for tour in solved_tours]
overall_cost = sum(total_costs)

# Output results
for i, tour in enumerate(solved_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")