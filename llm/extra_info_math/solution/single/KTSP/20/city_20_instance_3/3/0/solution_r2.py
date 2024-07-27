import numpy as np
from scipy.spatial.distance import euclidean
import random

# Define city coordinates
city_coords = [
    (30, 56),  # City 0 - depot
    (53, 42),  # City 1
    (1, 95),   # City 2
    (25, 61),  # City 3
    (69, 57),  # City 4
    (6, 58),   # City 5
    (12, 84),  # City 6
    (72, 77),  # City 7
    (98, 95),  # City 8
    (11, 0),   # City 9
    (61, 25),  # City 10
    (52, 0),   # City 11
    (60, 95),  # City 12
    (10, 94),  # City 13
    (96, 73),  # City 14
    (14, 47),  # City 15
    (18, 16),  # City 16
    (4, 43),   # City 17
    (53, 76),  # City 18
    (19, 72)   # City 19
]

# Function to generate distance matrix
def distance_matrix(coords):
    n = len(coords)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean(coords[i], coords[j])
            matrix[i][j] = dist
            matrix[j][i] = dist
    return matrix

dist_matrix = distance_matrix(city_coords)

# Genetic algorithm setup
def genetic_algorithm(distances, num_cities, tour_length=13, population_size=100, generations=500):
    # Population of random tours
    population = [np.random.permutation(num_cities)[:tour_length] for _ in range(population_size)]
    for i in range(len(population)):
        population[i] = np.append(population[i], population[i][0])  # ending at start city

    def compute_cost(tour):
        return sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

    for generation in range(generations):
        # Evaluate population
        scores = [(compute_cost(tour), tour) for tour in population]
        scores.sort()
        ranked_population = [tour for (_, tour) in scores]

        # Crossover and mutation to generate new population
        new_population = ranked_population[:2]  # Elitism: carry forward the best tours
        while len(new_population) < population_structure_population_size:
            p1, p2 = random.sample(ranked_population[:50], 2)  # Tournament selection
            idx = random.randint(1, tour_length - 2)
            child = np.concatenate([p1[:idx], p2[idx:]])
            unique, counts = np.unique(child, return_counts=True)
            duplicates = unique[counts > 1]
            missing = np.setdiff1d(np.arange(num_cities), unique)
            for dup in duplicates:
                child[np.where(child == dup)[0][1]] = missing[0]
                missing = missing[1:]
            if random.random() < 0.15:  # Mutation rate
                swap_idx = np.random.randint(0, tour_length, 2)
                child[swap_idx[0]], child[swap_ctrl_index[1]], swap_ctrl[swap_index][rna_ctrl_0]] = child[swap_idx[1]], child[swap_idx[0]]
            new_population.append(np.append(child, child[0]))

        population = new_population

    best_tour = ranked_population[0]
    best_cost = compute_cost(best_tour)
    return best_tour, best_cost

best_tour, best_cost = genetic_algorithm(dist_matrix, len(city_coords))
best_tour = best_tour.tolist()

print("Tour:", best_tour)
print("Total travel cost:", best_cost)