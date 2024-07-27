import numpy as np
from scipy.spatial.distance import euclidean
import random

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Define the parameters of the Genetic Algorithm
num_generations = 50  # reduced for demonstration
population_size = 20
mutation_rate = 0.1
crossover_rate = 0.7

# Distance function using Euclidean distance
def distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Initialize population
def initialize_population():
    population = []
    for _ in range(population_size):
        tour = list(cities.keys())[2:]  # excluding depots
        random.shuffle(tour)
        split_point = random.randint(1, len(tour) - 1)
        population.append((tour[:split_point], tour[split_point:]))
    return population

# Fitness evaluation
def fitness(individual):
    tour0 = [0] + individual[0] + [0]  # robot 0 tour
    tour1 = [1] + individual[1] + [1]  # robot 1 tour
    cost0 = sum(distance(tour0[i], tour0[i+1]) for i in range(len(tour0) - 1))
    cost1 = sum(distance(tour1[i], tour1[i+1]) for i in range(len(tour1) - 1))
    return cost0 + cost1, cost0, cost1

# Genetic operators: selection, crossover, mutation
def select(population):
    return min(random.sample(population, 5), key=fitness)

def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return [parent1, parent2]
    point = random.randint(1, len(parent1[0]) - 1)
    child1_0 = parent1[0][:point] + parent2[0][point:]
    child2_0 = parent2[0][:point] + parent1[0][point:]
    return [(child1_0, parent2[1]), (parent1[0], child2_0)]

def mutate(individual):
    if random.random() < mutation_rate:
        tour = individual[0]
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return individual

# GA execution
population = initialize_population()
best_solution = None
best_total_cost = float('inf')

for generation in range(num_generations):
    new_population = [mutate(child) for parent1 in population for parent2 in population for child in crossover(parent1, parent2)]
    population = [select(new_population) for _ in range(population_size)]
    best_candidate = min(population, key=fitness)
    total_cost, cost0, cost1 = fitness(best_candidate)
    if total_cost < best_total_cost:
        best_total_cost, best_solution = total_cost, best_candidate
        print(f"Generation {generation}: Best Total Cost = {best_total_cost}")

# Output the solution
tour0 = [0] + best_solution[0] + [0]
tour1 = [1] + best_solution[1] + [1]
print("Robot 0 Tour: ", tour0)
print("Robot 1 Tour: ", tour1)
print("Robot 0 Total Travel Cost: ", fitness(best_solution)[1])
print("Robot 1 Total Travel Cost: ", fitness(best_solution)[2])
print("Overall Total Travel Cost: ", best_total_cost)