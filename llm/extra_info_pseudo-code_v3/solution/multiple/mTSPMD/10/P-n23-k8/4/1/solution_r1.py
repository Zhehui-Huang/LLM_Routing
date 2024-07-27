import numpy as np
import random

# City and robot data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
robots = 8
depot_cities = list(range(robots))

# Distance calculation
def distance(a, b):
    return np.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Prepare distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = distance(i, j)
        else:
            distance_matrix[i, j] = float('inf')

# GA implementation details
population_size = 200
num_generations = 500

# Helper functions
def create_individual():
    """ Create a feasible route for each robot returning each to its respective depot. """
    cities_to_visit = list(range(8, num_cities))
    random.shuffle(cities_to_visit)
    segment_lengths = np.random.multinomial(len(cities_to_visit), [1.0 / robots] * robots)
    starts = [sum(segment_lengths[:i]) for i in range(robots)]

    chromosome = []
    for i in range(robots):
        current_cities = cities_to_visit[starts[i]:starts[i] + segment_lengths[i]]
        chromosome.append([depot_cities[i]] + current_cities + [depot_cities[i]])
    
    return chromosome

def individual_cost(chromosome):
    """ Calculate total cost of a specific individual's routes. """
    total_cost = 0
    for tour in chromosome:
        for i in range(len(tour) - 1):
            total_cost += distance_matrix[tour[i], tour[i + 1]]
    return total_cost

def crossover(parent1, parent2):
    """ Apply crossover operation to generate new offspring. """
    # Simple one-point crossover
    point = random.randint(1, robots - 1)
    new_tour = parent1[:point] + parent2[point:]
    return new_tour

def mutate(chromosome):
    """ Randomly swap two cities in two tours to maintain diversity in population. """
    tour_index1, tour_index2 = random.sample(range(robots), 2)
    if len(chromosome[tour_index1]) > 2 and len(chromosome[tour_index2]) > 2:
        city_index1 = random.randint(1, len(chromosome[tour_index1]) - 2)
        city_index2 = random.randint(1, len(chromosome[tour_index2]) - 2)
        chromosome[tour_index1][city_index1], chromosome[tour_index2][city_index2] = \
            chromosome[tour_index2][city_index2], chromosome[tour_index1][city_index1]
    
population = [create_individual() for _ in range(population_size)]
best_solution = None
best_cost = float('inf')

# Evolution
for generation in range(num_generations):
    # Select individuals based on roulette wheel selection
    costs = np.array([individual_cost(ind) for ind in population])
    fitness = 1 / (1 + costs - costs.min())
    probabilities = fitness / fitness.sum()
    selected_indices = np.random.choice(range(population_size), size=population_size, replace=True, p=probabilities)
    selected_population = [population[i] for i in selected_indices]

    # Crossover and mutation
    next_population = []
    for i in range(0, population_size, 2):
        if i + 1 < population_size:
            offspring1, offspring2 = crossover(selected_population[i], selected_population[i + 1])
            mutate(offspring1)
            mutate(offspring2)
            next_population.append(offspring1)
            next_population.append(offspring2)
    
    # Re-evaluate and keep the best
    population = next_population
    current_best_idx = np.argmin(costs)
    current_best_cost = costs[current_best_idx]
    if current_best_cost < best_cost:
        best_cost = current_best_cost
        best_solution = population[current_best_idx]

# Output best solution found
print("Best Tours:")
overall_total_cost = 0
for r, tour in enumerate(best_solution):
    tour_cost = sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    overall_total_cost += tour_cost
    print(f"Robot {r} Tour: {tour}")
    print(f"Robot {r} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")