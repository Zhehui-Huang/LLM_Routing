import random
import numpy as np

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def initialize_population(pop_size, cities):
    population = []
    city_list = list(cities.keys())[2:]  # Start from 2 to skip depots
    for _ in range(pop_size):
        individual = city_list.copy()
        random.shuffle(individual)
        population.append(individual)
    return population

def calculate_fitness(individual, depots):
    # To include both robots, we add the initial and final depot positions to the tour for calculation
    fitness = 0
    robot0_tour = [0] + individual[:len(individual)//2] + [0]
    robot1_tour = [1] + individual[len(individual)//2:] + [1]
    
    for tour in [robot0_tour, robot1_tour]:
        for i in range(len(tour) - 1):
            fitness += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return fitness

def selection(population, fitnesses):
    # Selecting best individuals in the current generation for mating.
    sorted_population = [x for _, x in sorted(zip(fitnesses, population), key=lambda pair: pair[0])]
    return sorted_population[:len(sorted_population)//2]

def crossover(parent1, parent2):
    child = parent1[:len(parent1)//2] + parent2[len(parent1)//2:]
    return child

def mutate(individual):
    i, j = random.sample(range(len(individual)), 2)
    individual[i], individual[j] = individual[j], individual[i]
    return individual

# Genetic Algorithm implementation
def genetic_algorithm(cities, depots, max_gen, pop_size):
    population = initialize_population(pop_token_size, cities)
    best_fit = float('inf')
    best_solution = None
    
    for gen in range(max_gen):
        fitnesses = [calculate_fitness(ind, depots) for ind in population]
        if min(fitnesses) < best_fit:
            best_fit = min(fitnesses)
            best_solution = population[fitnesses.index(best_fit)]
        
        selected = selection(population, fitnesses)
        next_gen = []
        
        while len(next_gen) < pop_size:
            p1, p2 = random.choices(selected, k=2)
            child = mutate(crossover(p1, p2))
            next_gen.append(child)
            
        population = next_gen

    return best_solution, best_fit

# Initializing parameters
max_gen = 1000
pop_size = 100
depots = {0: cities[0], 1: cities[1]}

best_solution, best_fitness = genetic_algorithm(cities, depots, max_gen, pop_size)