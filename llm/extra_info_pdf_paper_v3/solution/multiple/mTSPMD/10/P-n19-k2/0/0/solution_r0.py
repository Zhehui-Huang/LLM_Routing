import numpy as np
import random
from scipy.spatial import distance

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate the distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = distance.euclidean(cities[i], cities[j])
    return distance_matrix

distance_matrix = calculate_distance_matrix(cities)

def create_initial_population(size, non_depot_cities):
    population = []
    for _ in range(size):
        individual = random.sample(non_depot_cities, len(non_depot_cities))
        population.append(individual)
    return population

def evaluate_individual(individual, depots):
    # Assign the first half to depot 0, the second half to depot 1
    split = len(individual) // 2
    robot0_tour = [0] + individual[:split] + [0]
    robot1_tour = [1] + individual[split:] + [1]
    
    cost0 = sum(distance_matrix[robot0_tour[i]][robot0_tour[i+1]] for i in range(len(robot0_tour) - 1))
    cost1 = sum(distance_matrix[robot1_tour[i]][robot1_tour[i+1]] for i in range(len(robot1_tour) - 1))
    return (robot0_tour, cost0), (robot1_tour, cost1)

def evolve_population(population, depots, best_fitness, mutation_rate=0.1):
    new_population = []
    scores = [(evaluate_individual(ind, depots), ind) for ind in population]
    scores.sort(key=lambda x: x[0][0][1] + x[0][1][1])
    best_individual = scores[0][1]
    if best_fitness is None or best_fitness[0][0][1] + best_fitness[0][1][1] > scores[0][0][0][1] + scores[0][0][1][1]:
        best_fitness = scores[0]
    # Elitism
    new_population.append(best_individual)
    # Rest of the new population
    for _ in range(1, len(population)):
        parent1, parent2 = random.choices(population, k=2)
        child = crossover(parent1, parent2)
        if random.random() < mutation_rate:
            mutate(child)
        new_population.append(child)
    return new_population, best_fitness

def crossover(parent1, parent2):
    cross_point = random.randint(0, len(parent1) - 1)
    child = parent1[:cross_point] + [city for city in parent2 if city not in parent1[:cross_point]]
    return child

def mutate(individual):
    idx1, idx2 = random.sample(range(len(individual)), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Main Genetic Algorithm function
def genetic_algorithm(population_size=100, generations=500):
    non_depot_cities = list(cities.keys())[2:]  # exclude depot cities 0 and 1
    population = create_initial_population(population_size, non_depot_cities)
    best_fitness = None
    for _ in range(generations):
        population, best_fitness = evolve_population(population, [0, 1], best_fitness)
    return best_fitness

# Run Genetic Algorithm
best_solution = genetic_algorithm()
(robot0, cost0), (robot1, cost1) = best_solution[0]
overall_cost = cost0 + cost1

print(f"Robot 0 Tour: {robot0}")
print(f"Robot 0 Total Travel Cost: {cost0:.2f}")
print(f"Robot 1 Tour: {robot1}")
print(f"Robot 1 Total Travel Cost: {cost1:.2f}")
print(f"Overall Total Travel Cost: {overall_cost:.2f}")