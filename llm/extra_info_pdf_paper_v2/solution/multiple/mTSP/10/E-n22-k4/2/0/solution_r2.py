import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# Calculate distance matrix
def create_distance_matrix(cities):
    num = len(cities)
    dist_matrix = np.zeros((num, num))
    for i in range(num):
        for j in range(num):
            dist_matrix[i][j] = euclidean(critical[i], cities[j])
    return dis_matrix

dist_matrix = create_distance_matrix(cities)

# Genetic Algorithm Functions
def create_initial_population(pop_size, city_count):
    return [random.sample(range(1, city_count), city_count - 1) for _ in range(pop_size)]

def fitness(chromosome):
    total_cost = 0
    sections = np.array_split(chromosome, num_robots)
    for section in sections:
        route_cost = dist_matrix[0, section[0]] + sum(dist_matrix[section[i], section[i + 1]] for i in range(len(section) - 1))
        route_cost += dist_matrix[section[-1], 0]
        total_cost += route_cost
    return total_cost

def crossover(parent1, parent2):
    cut_point = random.randint(1, len(parent1) - 1)
    child = parent1[:cut_point] + [x for x in parent2 if x not in parent1[:cut_point]]
    return child

def mutate(chromosome, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

# GA initial setup
population_size = 100
population = create_initial_population(population_size, len(cities))
num_generations = 500

# Evolution process
for generation in range(num_generations):
    population.sort(key=fitness)
    top_individuals = population[:10]
    offspring = []
    while len(offspring) < population_size:
        parent1, parent2 = random.choices(top_individuals, k=2)
        child = crossover(parent1, parent2)
        mutate(child)
        offspring.append(child)
    population = top_individuals + offspring[:-10]

# Results processing
best_solution = population[0]
best_route_sections = np.array_split(best_solution, num_robots)

print("Optimized tours for robots:")
overall_cost = 0
for index, section in enumerate(best_route_sections):
    tour = [0] + list(section) + [0]
    cost = fitness([section])
    overall_cost += cost
    print(f"Robot {index+1} Tour: {tour}")
    print(f"Robot {index+1} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")