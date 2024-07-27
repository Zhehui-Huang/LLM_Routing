import random
import math
import numpy as np

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots and their depot assignments 
num_robots = 8
depots = list(range(8))

# Euclidean distance function
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to calculate the cost of a tour
def calculate_tour_cost(tour):
    cost = 0.0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

# Generate an initial random solution (divide non-depot cities among robots)
def generate_initial_solution():
    nondepot_cities = [i for i in cities.keys() if i not in depots]
    random.shuffle(nondepot_cities)
    parts = np.array_split(nondepot_cities, num_robots)
    tours = [[depots[i]] + list(parts[i]) + [depots[i]] for i in range(num_robots)]
    return tours

# Genetic Algorithm for MmTSP
def genetic_algorithm(max_generations=100, population_size=50, mutation_rate=0.1):
    population = [generate_initial_solution() for _ in range(population_size)]
    best_solution, best_cost = None, float('inf')

    for generation in range(max_generations):
        fitness = [sum(calculate_tour_cost(tour) for tour in individual) for individual in population]
        best_current_fit = min(fitness)
        best_index = fitness.index(best_current_fit)
        
        if best_current_fit < best_cost:
            best_cost = best_current_fit
            best_solution = population[best][(generation%10==0):]

    return best_solution, best_cost

best_solution, overall_cost = genetic_algorithm()

# Printing the result for each robot
for i, tour in enumerate(best_solution):
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")