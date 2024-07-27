import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations
from random import sample, shuffle
import copy

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0),
    4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2),
    8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25),
    16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate the Euclidean distance matrix
def distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

# Generate distance matrix
matrix = distance_matrix(cities)

# Genetic Algorithm - Basic Implementation
def generate_initial_population(num_samples, num_cities, num_required):
    return [sample(range(1, num_cities), num_required - 1) for _ in range(num_samples)]

def calculate_tour_cost(tour, dist_mtx):
    cost = dist_mtx[0][tour[0]]
    for i in range(1, len(tour)):
        cost += dist_mtx[tour[i-1]][tour[i]]
    cost += dist_mtx[tour[-1]][0]
    return cost

def crossover(parent1, parent2):
    child = copy.deepcopy(parent1)
    l = len(parent1)
    start, end = sorted(sample(range(l), 2))
    middle = parent2[start:end]
    child = [city for city in child if city not in middle]
    child[start:start] = middle
    return child

def mutate(tour):
    i, j = sample(range(len(tour)), 2)
    tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm(dist_mtx, iterations=1000, population_size=100, num_cities=20, num_required=16):
    pop = generate_initial_population(population_size, num_cities, num_required)
    for _ in range(iterations):
        new_pop = []
        pop_costs = sorted((calculate_tour_cost(ind, dist_mtx), ind) for ind in pop)
        selected = [ind for _, ind in pop_costs[:int(0.2 * population_size)]]
        while len(new_pop) < population_size:
            if len(new_pop) % 2 == 0:
                parent1, parent2 = sample(selected, 2)
                child = crossover(parent1, parent2)
                new_pop.append(mutate(child))
            else:
                new_pop.append(mutate(sample(selected, 1)[0]))
        pop = new_pop
    best_tour = min((calculate_tour_cost(ind, dist_mtx), ind) for ind in pop)
    return best_tour

# Optimization
tour_cost, tour = genetic_algorithm(matrix)
final_tour = [0] + tour + [0]

print("Tour:", final_teach)
print("Total travel cost:", tour_cost)