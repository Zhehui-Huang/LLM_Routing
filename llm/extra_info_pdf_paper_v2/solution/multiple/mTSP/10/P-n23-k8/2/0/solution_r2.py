import numpy as np
import random
from scipy.spatial import distance

# City Coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}
num_cities = len(cities)
num_robots = 8

# Compute distance matrix
dist_matrix = np.array([[distance.euclidean(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)])

# Genetic Algorithm settings
population_size = 50
generations = 500
mutation_rate = 0.1

def create_initial_population():
    base_tour = list(range(1, num_cities))
    return [random.sample(base_tour, len(base_tour)) for _ in range(population_size)]

def fitness(tour):
    # Split tour among robots and calculate total distance
    splits = np.array_split(tour, num_robots)
    total_cost = 0
    for split in splits:
        tour_cost = dist_matrix[0][split[0]]  # start from the depot
        for i in range(len(split) - 1):
            tour_cost += dist_matrix[split[i]][split[i + 1]]
        tour_cost += dist_matrix[split[-1]][0]  # return to the depot
        total_cost += tour_cost
    return total_cost

def tournament_selection(population, fitnesses, k=3):
    # Tournament Selection
    best = None
    for _ in range(k):
        ind = random.randint(0, len(population) - 1)
        if best is None or fitnesses[ind] < fitnesses[best]:
            best = ind
    return population[best]

def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[start:end+1] = parent1[start:end+1]
    filler = (city for city in parent2 if city not in child[start:end+1])
    child = [next(filler) if x is None else x for x in child]
    return child

def mutate(tour):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm():
    population = create_initial_population()
    for generation in range(generations):
        fitnesses = [fitness(ind) for ind in population]
        new_population = []
        for _ in range(population_size):
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
    # Select the best individual from the final population
    final_fitnesses = [fitness(ind) for ind in population]
    best_index = np.argmin(final_fitnesses)
    best_sol = population[best_index]
    return best_sol, final_fitnesses[best_index]

best_solution, best_cost = genetic_algorithm()

# Compute the solutions for output
routes = np.array_split(best_solution, num_robots)
robot_tours = [[0] + list(route) + [0] for route in routes]
robot_costs = [fitness(tour) for tour in robot_tours]
total_cost = sum(robot_costs)

# Printing the tours and costs
for idx, (tour, cost) in enumerate(zip(robot_tours, robot_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {total_cost}")