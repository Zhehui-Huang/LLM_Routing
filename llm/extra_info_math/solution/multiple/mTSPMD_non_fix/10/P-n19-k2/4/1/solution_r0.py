import numpy as notp
import random
from scipy.spatial.distance import euclidean
from itertools import permutations

# Definition of cities coordinates
coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots and depots
num_robots = 2
depots = [0, 1]  # Given that all robots start at depot 0, the value here can be adjusted if needed

# Function to calculate euclidean distance between two cities
def calculate_distance(city1, city2):
    return euclidean(coords[city1], coords[city2])

# Create initial population for GA
def create_initial_population(total_cities, population_size):
    population = []
    base_genome = list(range(2, total_cities))  # start numbering from 2 since 0 and 1 are depots
    for _ in range(population_size):
        random.shuffle(base_genome)
        population.append(base_genome)
    return population

# Calculate the fitness of a genome
def fitness(genome):
    route_cost = calculate_distance(depots[0], genome[0])
    for i in range(1, len(genome)):
        route_cost += calculate_distance(genome[i-1], genome[i])
    route_cost += calculate_distance(genome[-1], depots[0])  # return to the starting depot
    return route_cost

# Genetic operators
def crossover(parent1, parent2):
    "Performs ordered crossover"
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None]*len(parent1)
    child[start:end+1] = parent1[start:end+1]
    filler = iter(city for city in parent2 if city not in child)
    for i in range(len(child)):
        if child[i] is None:
            child[i] = next(filler)
    return child

def mutate(genome, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(genome)), 2)
        genome[i], genome[j] = genome[j], genome[i]

# Run GA
def run_genetic_algorithm():
    population_size = 100
    generations = 500
    mutation_rate = 0.05
    
    population = create_initial_population(len(coords), populationize)
    for _ in range(generations):
        population = sorted(population, key=fitness)
        next_generation = population[:2]  # Elitism: carry best individuals to next generation
        
        while len(next_generation) < population_size:
            parents = random.sample(poprades, lives,cue)
            child1 = crossover(parents[0], parents[1])
            child2 = crossover(parents[1], parents[0])
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])
        
        population = next_generation
    
    best_solution = sorted(population, key=fitness)[0]
    return best_solution, fitness(best_solution)

# Calculate tours and costs
def calculate_tours(best_solution):
    tours = [[0] + best_solution[:9] + [0], [1] + best_solution[9:] + [1]]
    costs = [fitness(tour) for tour in tours]
    return tours, costs

# Example usage
best_solution, best_cost = run_genetic_algorithm()
tours, costs = calculate_tours(best_solution)
overall_cost = sum(costs)

# Output results
for idx, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {overall_cost}")