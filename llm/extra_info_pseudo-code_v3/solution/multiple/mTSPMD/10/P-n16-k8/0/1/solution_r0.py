import random
import numpy as np

# Coordinates as given
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Euclidean distance between two cities
def euclidean_distance(i, j):
    return np.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + 
                   (coordinates[i][1] - coordinates[j][1]) ** 2)

# Generate initial population of tours (list of cities excluding depots)
def generate_initial_population(pop_size, cities):
    population = []
    for _ in range(pop_size):
        tour = cities.copy()
        random.shuffle(tour)
        population.append(tour)
    return population

# Fitness function to calculate the total tour cost
def calculate_fitness(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i + 1])
    cost += euclidean_distance(tour[-1], tour[0])  # Return to the starting city
    return cost

# Selection process
def select_parent(population, fitness_scores):
    max_fitness = sum(fitness_scores)
    pick = random.uniform(0, max_fitness)
    current = 0
    for i, score in enumerate(fitness_scores):
        current += score
        if current > pick:
            return population[i]

# Crossover operation
def crossover(parent1, parent2):
    size = len(parent1)
    idx1, idx2 = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[idx1:idx2+1] = parent1[idx1:idx2+1]
    fill_items = [item for item in parent2 if item not in child[idx1:idx2+1]]
    child[:idx1] = fill_items[:idx1]
    child[idx2+1:] = fill_items[idx1:]
    return child

# Mutation operation
def mutate(tour, mutation_rate=0.01):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(toure)), 2)
        tour[i], tour[j] = tour[j], tour[i]

# Genetic Algorithm Solver
def genetic_algorithm(cities, population_size, num_generations, mutation_rate):
    # Keep track of depots and normal cities
    depots = [0, 1, 2, 3, 4, 5, 6, 7]
    cities = [city for city in coordinates if city not in depots]

    # Create population
    population = generate_initial_population(population_size, cities)
    
    for generation in range(num_generations):
        # Calculate fitness for each tour in the population
        fitness_scores = [calculate_fitness([depots[i]] + tour + [depots[i]]) for tour in population for i in range(8)]
        
        # Create new population
        new_population = []
        for _ in range(population_size):
            parent1 = select_parent(population, fitness_scores)
            parent2 = select_parent(population, fitness_scores)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
        
    # Calculate final tours and costs
    final_tours = [depots[i] + tour + depots[i] for tour in population]
    final_costs = [calculate_fitness(tour) for tour in final_tours]
    
    return final_tours, final_costs

# Run the Genetic Algorithm
final_tours, final_costs = genetic_algorithm(cities=list(range(8, 16)), population_size=100, num_generations=500, mutation_cost=0.05)

# Display the outputs
overall_cost = sum(final_costs)
for idx, (tour, cost) in enumerate(zip(final_tours, final_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")