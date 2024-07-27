import numpy as np
import random
from scipy.spatial import distance_matrix

# Define coordinates for each city and depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Compute distance matrix using Euclidean distance
n_cities = len(coordinates)
distance_mtx = distance_matrix(coordinates, coordinates)

def evaluate_cost(chromosome):
    cost = 0
    for i in range(1, len(chromosome)):
        cost += distance_mtx[chromosome[i-1], chromosome[i]]
    return cost

def crossover(parent1, parent2):
    size = len(parent1)
    child = [-1] * size
    index1, index2 = sorted(random.sample(range(size), 2))
    child[index1:index2+1] = parent1[index1:index2+1]

    p2_vals = [val for val in parent2 if val not in child]
    p2_idx = 0
    for i in range(size):
        if child[i] == -1:
            child[i] = p2_vals[p2_idx]
            p2_idx += 1
    return child

def mutate(chromosome, mutation_rate=0.05):
    if random.random() < mutation_rate:
        i1, i2 = random.sample(range(len(chromosome)), 2)
        chromosome[i1], chromosome[i2] = chromosome[i2], chromosome[i1]

def generate_initial_population(pop_size, n_cities, depots):
    population = []
    for _ in range(pop_size):
        city_list = list(range(n_cities))
        for depot in reversed(depots):
            city_list.remove(depot)
        random.shuffle(city_list)
        for depot in depots:
            city_list.insert(0, depot)
            city_list.append(depot)
        population.append(city_list)
    return population

def genetic_algorithm(depots, n_generations=100, pop_size=50):
    population = generate_initial_population(pop_size, n_cities, depots)

    for generation in range(n_generations):
        # Evaluate each individual
        costs = [evaluate_cost(chromosome) for chromosome in population]
        # Tournament Selection
        new_population = []
        while len(new_population) < pop_size:
            fighters = random.sample(list(zip(population, costs)), k=3)
            winner = min(fighters, key=lambda x: x[1])
            new_population.append(winner[0])

        # Crossover and Mutation
        next_generation = []
        for _ in range(pop_size//2):
            p1, p2 = random.sample(new_population, 2)
            child1 = crossover(p1, p2)
            child2 = crossover(p2, p1)
            mutate(child1)
            mutate(child2)
            next_generation.extend([child1, child2])

        population = next_generation

    # Evaluate solution
    best_solution = min(population, key=evaluate_cost)
    best_cost = evaluate_cost(best_solution)
    return best_solution, best_cost

# Assuming robots start and end at each assigned depots:
robots_depots = [0, 1, 2, 3]

# Run the genetic algo
best_tour, total_cost = genetic_algorithm(robots_depots)
print("Robot Tours:")
for i in range(len(robots_depots)):
    print(f"Robot {i + 1} Tour: {best_tour}")
    tour_cost = evaluate_cost(best_tour)
    print(f"Robot {i + 1} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")