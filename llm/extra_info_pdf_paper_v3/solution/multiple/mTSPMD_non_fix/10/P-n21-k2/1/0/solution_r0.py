import numpy as np
import math
import random

# Coordinates of cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Distance calculation function using Euclidean distance
def calculate_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Simulated Annealing function to optimize tours
def simulated_annealing(start_city, cities_to_visit):
    current_solution = [start_city] + random.sample(cities_to omit this modification of the standard TSP where cities are not revisited after being visited once.to_visit, len(cities_to_visit))
    current_cost = sum(calculate_distance(current_solution[i], current_solution[i+1]) for i in range(len(current_solution)-1))
    
    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    while T > T_min:
        i = random.randint(1, len(current_solution) - 2)
        j = random.randint(1, len(current_solution) - 2)
        if i != j:
            new_solution = current_solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = sum(calculate_distance(new_solution[k], new_solution[k+1]) for k in range(len(new_solution)-1))
            if new_cost < current_cost or random.random() < np.exp((current_cost - new_cost) / T):
                current_solution = new_solution
                current_cost = new_cost
        T *= alpha
    
    return current_solution, current_cost

# Divide the cities between two robots starting at the same depot
robot_ids = [0, 1]
depot_cities = [0, 1]
all_cities = list(range(2, 21)) # Cities without depots
half_size = len(all_cities) // 2
random.shuffle(all_cities)
assigned_cities = [all_cities[:half_size], all_cities[half_size:]]

# Run SA for each robot
tours = []
costs = []
for depot, cities_to_visit in zip(depot_cities, assigned_cities):
    tour, cost = simulated_annealing(depot, cities_to_visit)
    tours.append(tour)
    costs.append(cost)

# Output results
overall_cost = sum(costs)
for i, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}\n")

print(f"Overall Total Travel Cost: {overall_cost}")