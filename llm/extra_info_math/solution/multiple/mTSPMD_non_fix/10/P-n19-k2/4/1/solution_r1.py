import numpy as np
import random
from scipy.spatial.distance import euclidean

# Definition of cities coordinates
coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def distance(city1, city2):
    """ Calculate euclidean distance between two cities """
    return euclidean(coords[city1], coords[city2])

def initialize_population(pop_size, num_cities):
    """ Generate an initial population of random tours """
    population = []
    for _ in range(pop_size):
        tour = list(range(2, num_cities))  # Start from city 2 since 0 and 1 are depot cities
        random.shuffle(tour)
        population.append(tour)
    return population

def fitness(tour):
    """ Calculate the total distance of a tour """
    total_distance = distance(0, tour[0])  # From depot 0 to first city
    for i in range(1, len(tour)):
        total_distance += distance(tour[i - 1], tour[i])
    return total_distance + distance(tour[-1], 0)  # Return to depot

def select_parents(population, tournament_size):
    """ Select parents using tournament selection """
    best = None
    for i in range(tournament_size):
        individual = random.choice(population)
        if best is None or fitness(individual) < fitness(best):
            best = individual
    return best

def crossover(parent1, parent2):
    """ Perform crossover between two parents """
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        
    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child

def mutate(individual, mutation_rate):
    """ Mutate an individual by swapping two cities with a certain probability """
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1

def genetic_algorithm(pop_size, mutation_rate, generations):
    """ Run the genetic algorithm """
    pop = initialize_population(pop_size, len(coords))
    for _ in range(generations):
        new_pop = []
        for i in range(0, pop_size, 2):
            parent1 = select_parents(pop, 3)
            parent2 = select_parents(pop, 3)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_pop.append(child1)
            new_pop.append(child2)
        pop = new_pop
    best_route = sorted(pop, key=fitness)[0]
    return best_route

# Parameters
population_size = 100
mutation_rate = 0.02
generations = 200

# Genetic Algorithm Execution
best_route = genetic_algorithm(population_size, mutation_rate, generations)

# Calculate cost
best_cost = fitness(best_route)

# Output the best route and cost
print("Best Route:", [0] + best_found + [0])
print("Total Travel Cost for Best Route:", best_cost)