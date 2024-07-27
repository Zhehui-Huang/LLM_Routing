import random
import numpy as in
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from itertools import permutations

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Function to calculate distance between two cities
def distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# GA Parameters
population_size = 100
generations = 500
mutation_rate = 0.1
elite_size = 20

# Initialize Population
def create_route():
    route = list(cities.keys())
    random.shuffle(route)
    return route

def initial_population(pop_size):
    return [create_route() for _ in range(pop_size)]
    
# Rank routes based on their total travel costs
def rank_routes(population):
    fitness_results = {}
    for i, route in enumerate(population):
        fitness_results[i] = total_travel_cost(route)
    return sorted(fitness_results.items(), key=lambda x: x[1])

# Route Total Cost
def total_travel_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance(route[i], route[i+1])
    cost += distance(route[-1], route[0])  # Complete the loop
    return cost

# Selection
def selection(pop_ranked, elite_size):
    selection_results = [pop_ranked[i][0] for i in range(elite_size)]
    return selection_results

# Crossover (Breeding)
def breed(parent1, parent2):
    child = []
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent2))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)
    
    child = parent1[startGene:endGene]
    child = child + [item for item in parent2 if item not in child]
    
    return child

# Mutation
def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual

# Evolution (create next generation)
def next_generation(current_gen, elite_size, mutation_rate):
    pop_ranked = rank_routes(current_gen)
    selection_results = selection(pop_ranked, elite_size)
    children = [current_gen[i] for i in selection_results]
    
    for i in range(len(current_gen) - len(selection_results)):
        parent1 = current_gen[selection_results[int(random.random() * len(selection_results))]]
        parent2 = current_gen[selection_results[int(random.random() * len(selection_results))]]
        child = breed(parent1, parent2)
        children.append(mutate(child, mutation_rate))
    return children

# Genetic Algorithm
def genetic_algorithm(population, pop_size, elite_size, mutation_rate, generations):
    pop = initial_population(pop_size)
    progress = []
    progress.append(rank_routes(pop)[0][1])
    
    for i in range(generations):
        pop = next_generation(pop, elite_size, mutation_rate)
        progress.append(rank_routes(pop)[0][1])
    
    best_route_index = rank_routes(pop)[0][0]
    best_route = pop[best_route_index]
    return best_route, progress

# Run Genetic Algorithm
best_route, progress = genetic_algorithm(population=cities, pop_size=population_size, elite_size=elite_size, mutation_rate=mutation_rate, generations=generations)
best_route_cost = total_travel_cost(best_route)

# Output Best Route and Cost
print("Best Route:")
print(best_route)
print("\nBest Route Travel Cost:")
print(best_route_cost)

# Plotting
plt.plot(progress)
plt.ylabel('Distance')
plt.xlabel('Generation')
plt.show()