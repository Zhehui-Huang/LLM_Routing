import numpy as np
import random

# Defining the city coordinates where the first entry is the depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**3)

# Create a route
def create_route():
    route = list(cities.keys())
    random.shuffle(route)
    return route

# Calculate total distance for the entire route
def total_distance(route):
    dist = distance(route[-1], route[0])  # Closing the loop
    for i in range(len(route) - 1):
        dist += distance(route[i], route[i+1])
    return dist

# Genetic algorithm functions
def create_initial_population(pop_size):
    return [create_route() for _ in range(pop_size)]

def rank_routes(population):
    fitness_scores = [(route, total_distance(route)) for route in population]
    return sorted(fitness_scores, key=lambda x: x[1])

def selection(ranked_pop, elite_size):
    selection_results = []
    for i in range(elite_size):
        selection_results.append(ranked_pop[i][0])
    return selection
    return [ranked[0] for ranked in selection_results]

def breed(parent1, parent2):
    child = []
    gene_a = int(random.random() * len(parent1))
    gene_b = int(random.random() * len(parent2))
    
    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)

    child = parent1[start_gene:end_gene]
    child += [item for item in parent2 if item not in child]

    return child

def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(individual))
            
            individual[swapped], individual[swap_with] = individual[swap_with], individual[swapped]
    return individual

def next_generation(current_gen, elite_size, mutation_rate):
    ranked_population = rank_routes(current_gen)
    selection_results = selection(ranked_population, elite_size)
    children = []
    length = len(current_gen) - len(selection_results)
    pool = random.choices(selection_results, k=length)

    for i in range(0, length):
        child = breed(selection_results[i], pool[i])
        children.append(mutate(child, mutation_build))
    children.extend(selection_results)
    
    return children

# Running the genetic algorithm
def genetic_algorithm(population, pop_size, elite_size, mutation_rate, generations):
    pop = create_initial_population(pop_size)
    print("Initial shortest distance:", rank_routes(pop)[0][1])

    for i in range(generations):
        pop = next_generation(pop, elite_size, mutation_rate)

    print("Final shortest distance:", rank_routes(pop)[0][1])
    return rank_routes(pop)[0][0]

# Configuration
pop_size = 100
elite_size = 20
mutation_rate = 0.01
generations = 500

# Running the algorithm
best_route = genetic_algorithm(population, pop_size, elite_size, mutation_rate, generations)

# Divide the route between two robots (splitting the results)
robot1_route = [0] + best_route[:len(best_route)//2 + 1] + [0]
robot2_route = [0] + best_route[len(best_route)//2 + 1:] + [0]


# Calculate the costs
def calculate_cost(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route)-1))

cost1 = calculate_cost(robot1_route)
cost2 = calculate_cost(robot2_route)
total_cost = cost1 + cost2

# Output results
print(f"Robot 1 Tour: {robot1_route}")
print(f"Robot 1 Total Travel Cost: {cost1}")
print(f"Robot 2 Tour: {robot2_route}")
print(f"Robot 2 Total Travel Cost: {cost2}")
print(f"Overall Total Travel Cost: {total_cost}")