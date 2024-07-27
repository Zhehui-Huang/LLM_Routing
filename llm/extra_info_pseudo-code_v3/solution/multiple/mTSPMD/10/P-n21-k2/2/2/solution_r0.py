import numpy as np
import random
from scipy.spatial import distance

# City coordinates including depots
cities = np.array([
    [30, 40],  # Depot 0
    [37, 52],  # Depot 1
    [49, 49], [52, 64], [31, 62], [52, 33], [42, 41],
    [52, 41], [57, 58], [62, 42], [42, 57], [27, 68],
    [43, 67], [58, 48], [58, 27], [37, 69], [38, 46],
    [61, 33], [62, 63], [63, 69], [45, 35]
])

def calculate_distance_matrix(cities):
    return distance.cdist(cities, cities, 'euclidean')

# Generate the distance matrix
distance_matrix = calculate_distance_matrix(cities)
num_cities = len(cities)

# Fitness evaluation
def tour_length(tour, distance_matrix):
    return np.sum([distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1)])

#### Step 2: Define Genetic Algorithm Functions

def initialize_population(pop_size, num_cities, depots=[0, 1]):
    return [[random.choice(depots)] + random.sample(range(2, num_cities), num_cities-2) + [depot]
            for depot in depots for _ in range(pop_size // len(depots))]

def fitness(tours, distance_matrix):
    return [tour_length(tour, distance_matrix) for tour in tours]

def selection(population, fitnesses):
    chosen = sorted(zip(population, fitnesses), key=lambda x: x[1])
    return [x[0] for x in chosen[:len(chosen)//2]]

def crossover(tour1, tour2):
    size = len(tour1)
    p1, p2 = random.sample(range(2, size-2), 2)  # Avoid crossover at depots
    p1, p2 = sorted((p1, p2))
    child1 = tour1[:p1] + tour2[p1:p2] + tour1[p2:]
    child2 = tour2[:p1] + tour1[p1:p2] + tour2[p2:]
    return [child1, child2]

def mutate(tour, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(2, len(tour)-2), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm(num_generations=100, pop_size=50):
    population = initialize_population(pop_size, num_cities)
    for _ in range(num_generations):
        fit = fitness(population, distance_matrix)
        population = selection(population, fit)
        new_population = []
        while len(new_population) < pop_size:
            par1, par2 = random.choices(population, k=2)
            children = crossover(par1, par2)
            new_population.extend(map(mutate, children))
        population = new_population

    final_fitness = fitness(population, distance_matrix)
    best_tour_index = np.argmin(final_fitness)
    return population[best_tour_index], final_fitness[best_tour_index]

best_tour, best_cost = genetic_algorithm(num_generations=200, pop_size=100)
print("Best Tour:", best_tour)
print("Best Cost:", best_cost)