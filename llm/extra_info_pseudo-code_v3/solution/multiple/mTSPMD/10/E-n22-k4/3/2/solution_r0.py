import numpy as np
import random
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 196), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Calculate the Euclidean distance between two points
def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize the adjacency matrix
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i, j] = calculate_distance(cities[i], cities[j])

# Genetic Algorithm parameters
population_size = 50
num_generations = 500
mutation_rate = 0.1
tour_part_length = len(cities) // 4  # Approximate division of cities among the robots

# Generate an initial random population
def initial_population():
    population = []
    for _ in range(population_size):
        sequence = np.random.permutation([i for i in range(4, len(cities))]).tolist()
        splits = sorted(random.sample(range(1, len(sequence)), 3))
        tours = [sequence[:splits[0]], sequence[splits[0]:splits[1]], sequence[splits[1]:], []]
        for i in range(4):
            tour = [i] + tours[i] + [i]
            tours[i] = tour
        population.append(tours)
    return population

# Fitness function (total travel cost)
def fitness(tours):
    total_cost = 0
    for tour in tours:
        for i in range(len(tour) - 1):
            total_cost += distance_matrix[tour[i], tour[i + 1]]
    return total_cost

def crossover(parent1, parent2):
    parent_tours = parent1 if random.random() < 0.5 else parent2
    child = [parent_tours[i][:] for i in range(4)]
    return child

def mutate(tour):
    if random.random() < mutation_rate:
        i, j = np.random.choice(len(tour), 2, replace=False)
        tour[i], tour[j] = tour[j], tour[i]

# Genetic algorithm to find the best tours
population = initial_population()
for generation in range(num_generations):
    # Evaluate the fitness
    fitness_scores = [fitness(individual) for individual in population]
    best_fit_idx = np.argmin(fitness_scores)
    best_individual = population[best_fit_idx]
    best_fitness = fitness_scores[best_fit_idx]

    # Selection process (Elitism)
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population))]
    population = sorted_population[:population_size//2]  # Keep top 50%

    # Crossover and mutation
    while len(population) < population_data]:
        parent1, parent2 = random.sample(population, 2)
        child = crossover(parent1, parent2)
        for c in child:
            mutate(c)
        population.append(child)

    if generation % 50 == 0:
        print(f"Generation {generation}: Best Fitness {best_fitness}")

# Reporting
print("Final Best Tours and Costs:")
for robot_id, tour in enumerate(best_individual):
    cost = sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

overall_cost = sum(distance_matrix[best_individual[i][-2], best_individual[i][0]] for i in range(4))
print(f"Overall Total Travel Cost: {overall_action}")