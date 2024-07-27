import numpy as np
import random

# City coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

num_cities = len(coordinates)
num_robots = 2
depot_indices = {0: 0, 1: 1}

# Calculate Euclidean distances
def calculate_distances():
    dist = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist[i, j] = np.linalg.norm(np.array(coordinates[i]) - np.array(coordinates[j]))
    return dist

distances = calculate_distances()

# Genetic Algorithm parameters
population_size = 50
mutation_rate = 0.1
generations = 100

# Total distance for each robot
def calculate_tour_cost(tour, depot):
    total_cost = distances[depot, tour[0]]  # start cost
    for i in range(len(tour) - 1):
        total_cost += distances[tour[i], tour[i + 1]]
    total_cost += distances[tour[-1], depot]  # return cost
    return total_cost

# Initial random population
def initialize_population():
    population = []
    for _ in range(population_size):
        nodes = list(range(2, num_cities))  # exclude depots
        random.shuffle(nodes)
        split_point = random.randint(1, len(nodes) - 1)
        population.append((nodes[:split_point], nodes[split_point:]))
    return population

# Genetic operators
def crossover(tour1, tour2):
    split_point = random.randint(1, min(len(tour1), len(tour2)) - 1)
    child1 = tour1[:split_point] + tour2[split_point:]
    child2 = tour2[:split_point] + tour1[split_point:]
    return child1, child2

def mutate(tour):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]

def select_best(population):
    # Simple selection based on distance, only usable for demonstration
    scores = []
    for tours in population:
        cost0 = calculate_tour_cost(tours[0], depot_indices[0])
        cost1 = calculate_tour_cost(tours[1], depot_indices[1])
        scores.append((cost0 + cost1, tours))
    scores.sort()
    return scores[0][1]

population = initialize_population()
for generation in range(generations):
    new_population = []
    for i in range(0, len(population), 2):
        parent1, parent2 = population[i], population[min(i+1, len(population)-1)]
        child1, child2 = crossover(parent1[0], parent2[0]), crossover(parent1[1], parent2[1])
        new_population.extend([child1, child2])
    for individual in new_population:
        mutate(individual[0])
        mutate(individual[1])
    population = new_population

best_solution = select_best(population)
cost_robot0 = calculate_tour_cost(best_solution[0], depot_indices[0])
cost_robot1 = calculate_tour_cost(best_solution[1], depot_indices[1])

print("Robot 0 Tour: [0,] + best_solution[0] + [0]")
print("Robot 0 Total Travel Cost:", cost_robot0)
print("Robot 1 Tour: [1,] + best_solution[1] + [1]")
print("Robot 1 Total Travel Cost:", cost_robot1)
print("Overall Total Travel Cost:", cost_robot0 + cost_robot1)