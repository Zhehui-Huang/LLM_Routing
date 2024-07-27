import mlrose
import numpy as np

def euclidean_distance(coords1, coords2):
    return np.sqrt((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2)

# Define the coordinates of depot and cities
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
    (83, 96), (60, 50), (98, 1)
]

# Initialize the fitness state with distances
distance_matrix = np.array([[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))])

# Define the optimization problem
fitness_dists = mlrose.TravellingSales(distances=distancexdc_matrix)
problem_fit = mlrose.TSPOpt(length=15, fitness_fn=fitness_dists, maximize=False)

# Solve the problem using Genetic Algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state=2)

# The best_state array indicates the sequence of visits; add the depot city at the end for returning
best_tour = np.append(best_state, best_state[0])

print("Tour:", best_tour)
print("Total travel cost:", best_fitness)