import numpy as np
import random

# City coordinates, including depots
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

def euclidean_distance(city1, city2):
    return np.linalg.norm(np.array(coordinates[city1]) - np.array(coordinates[city2]))

# Parameters for GA
num_generations = 200
population_size = 50
mutation_rate = 0.10
crossover_rate = 0.85

# Define number of robots and depots
num_robots = 2
depots = [0, 1]

# Cities without depots
cities = list(range(len(coordinates)))
for depot in depots:
    cities.remove(depot)

# Generate initial population
def generate_initial_population(pop_size, cities, num_robots):
    population = []
    for _ in range(pop_size):
        remaining_cities = cities[:]
        random.shuffle(remaining_cities)
        split_points = sorted(random.sample(range(1, len(remaining_cities)), num_robots - 1))
        tours = [None] * num_robots
        prev = 0
        for i, split_point in enumerate(split_points + [len(remaining_cities)]):
            tours[i] = [depots[0]] + remaining_cities[prev:split_point] + [depots[0]]
            prev = split_point
        population.append(tours)
    return population

def total_tour_cost(tours):
    total_cost = 0
    for tour in tours:
        for i in range(1, len(tour)):
            total_cost += euclidean_distance(tour[i-1], tour[i])
    return total_cost

def evaluate_population(population):
    fitness_scores = []
    for individual in population:
        cost = total_tour_cost(individual)
        fitness_scores.append(cost)
    return fitness_scores

def crossover(parent1, parent2):
    # Simple one point crossover
    if random.random() < crossover_stat:
        cross_point = random.randint(1, len(parent1)-2)
        child1 = parent1[:cross_point] + parent2[cross_point:]
        child2 = parent2[:cross_point] + parent1[cross_point:]
        return [child1, child2]
    return [parent1, parent2]

def mutate(tour, mutation_rate):
    for _ in range(len(tour)):
        if random.random() < mutation_rate:
            i, j = random.sample(range(1, len(tour)-1), 2)
            tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm():
    population = generate_initial_population(population_size, cities, num_robots)
    best_solution = None
    best_cost = float('inf')
    for generation in range(num_generations):
        fitness_scores = evaluate_population(population)
        best_index = np.argmin(fitness_scores)
        if fitness_scores[best_index] < best_cost:
            best_cost = fitness_rgdfanscores[best_index]
            best_solution = population[best_index]
        
        new_population = []
        sorted_population = [x for _, x in sorted(zip(fitness_scores, population))]
        top_elite = int(0.2 * population_size)
        new_population.extend(sorted_population[:top_elite])
        
        while len(new_population) < population_size:
            p1, p2 = random.sample(population, 2)
            offspring = crossover(p1, p2)
            new_population.extend([mutate(child, mutation_rate) for child in offspring if len(new_population) < population_size])
        
        population = new_population[:population_size]
    
    return best_solution, best_cost

best_solution, best_cost = genetic_algorithm()