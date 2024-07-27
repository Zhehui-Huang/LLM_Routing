import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)}

# Calculate distance between two cities
def distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Genetic Algorithm Parameters
num_generations = 500
population_size = 100
mutation_rate = 0.1
crossover_rate = 0.8

# Initialize population
def initialize_population():
    population = []
    for _ in range(population_size):
        # Create a random permutation of non-depot cities
        tour = list(cities.keys())[2:]
        random.shuffle(tour)
        # Randomly split into two tours for each robot
        split_point = random.randint(1, len(tour) - 1)
        population.append((tour[:split_point], tour[split_point:]))
    return population

# Fitness function
def fitness(individual):
    tour1, tour2 = [0] + individual[0] + [0], [1] + individual[1] + [1]
    cost1 = sum(distance(tour1[i], tour1[i+1]) for i in range(len(tour1)-1))
    cost2 = sum(distance(tour2[i], tour2[i+1]) for i in range(len(tour2)-1))
    return cost1 + cost2, cost1, cost2

# Tournament selection
def select(population):
    tournament_size = 5
    candidates = random.sample(population, tournament_size)
    return min(candidates, key=fitness)

# Partially matched crossover (PMX)
def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return [parent1, parent2]
    cut1, cut2 = sorted(random.sample(range(len(parent1[0])), 2))
    child1 = parent1[0][:cut1] + parent2[0][cut1:cut2] + parent1[0][cut2:]
    child2 = parent2[0][:cut1] + parent1[0][cut1:cut2] + parent2[0][cut2:]
    return [(child1, parent2[1]), (child2, parent1[1])]

# Mutation by swapping
def mutate(individual):
    if random.random() < mutation_rate:
        tour1 = individual[0]
        i, j = random.sample(range(len(tour1)), 2)
        tour1[i], tour1[j] = tour1[j], tour1[i]
    return individual

# Main execution of the Genetic Algorithm
population = initialize_population()
best_solution = None
best_cost = float('inf')

for generation in range(num_generations):
    new_population = []
    for _ in range(population_size // 2):
        parent1 = select(population)
        parent2 = select(population)
        children = crossover(parent1, parent2)
        for child in children:
            new_population.append(mutate(child))
    population = new_population
    current_best = min(population, key=fitness)
    current_cost, cost1, cost2 = fitness(current_best)
    if current_cost < best_cost:
        best_cost = current_cost
        best_solution = current_best

# Display the output correctly
tour1 = [0] + best_solution[0] + [0]
tour2 = [1] + best_solution[1] + [1]
cost1 = sum(distance(tour1[i], tour1[i + 1]) for i in range(len(tour1) - 1))
cost2 = sum(distance(tour2[i], tour2[i + 1]) for i in range(len(tour2) - 1))
total_cost = cost1 + cost2

print("Robot 0 Tour:", tour1)
print("Robot 0 Total Travel Cost:", cost1)
print("\nRobot 1 Tour:", tour2)
print("Robot 1 Total Travel Cost:", cost2)
print("\nOverall Total Travel Cost:", total_cost)