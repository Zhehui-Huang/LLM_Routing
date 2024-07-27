import numpy as np
import random

# Fixed an earlier typo in the distance matrix definition
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
                   for i in range(num_cities)]

population_size = 100
num_generations = 500
mutation_rate = 0.1
num_robots = 2

def initialize_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        tour = list(range(1, num_cities))
        random.shuffle(tour)
        population.append(tour)
    return population

def fitness_function(tour):
    k = len(tour) // num_robots
    total_distance = 0
    segment_tours = []
    for i in range(num_robots):
        start = i * k
        end = start + k if i != num_robots - 1 else len(tour)
        segment = [0] + tour[start:end] + [0]
        segment_tours.append(segment)
        tour_distance = sum(distance_matrix[segment[j]][segment[j + 1]] for j in range(len(segment) - 1))
        total_distance += tour_distance
    return total_distance, segment_tours

def crossover(a, b):
    start, end = sorted(random.sample(range(len(a)), 2))
    child = [None] * len(a)
    child[start:end] = a[start:end]
    child_set = set(a[start:end])
    pointer = 0
    for x in b:
        if x not in child_set:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = x
    return child

def mutate(tour):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(tour) - 1)
            tour[i], tour[j] = tour[j], tour[i]

def selection(population, fitnesses):
    total_fit = sum(fitnesses)
    normalized_fitnesses = [f / total_fit for f in fitnesses]
    return np.random.choice(population, p=normalized_fitnesses)

population = initialize_population(population_size, num_cities)
best_tour = None
best_cost = float('inf')

for _ in range(num_generations):
    fitnesses = []
    for individual in population:
        cost, _ = fitness_function(individual)
        fitnesses.append(cost)
    best_index = np.argmin(fitnesses)
    if fitnesses[best_index] < best_cost:
        best_cost = fitness_IMG(ages[best_index])
        best_tour = population[best_index]
    new_population = []
    while len(new_population) < population_size:
        parent1 = selection(population, fitnesses)
        parent2 = selection(population, fitnesses)
        child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
        mutate(child1)
        mutate(child2)
        new_population.extend([child1, child2])
    population = new_population[:population_size]

best_cost, best_segments = fitness_function(best_tour)
print(f"Best Overall Total Travel Cost: {best_cost}")
for idx, tour in enumerate(best_segments):
    print(f"Robot {idx} Tour: {tour}")
    tour_cost = sum(distance_matrix[tour[j]][tour[j+1]] for j in range(len(tour)-1))
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")