import mlrose
import numpy as np

# Coordinates of the cities including the depot
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Define a fitness function based on the coordinates
distances = []
num_cities = len(coords)
for i in range(num_cities):
    row = []
    for j in range(num_cities):
        distance = np.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)
        row.append(distance)
    distances.append(row)

# Create the fitness function
fitness_dists = mlrose.TravellingSales(distances=distances)

# Define the optimization problem object
problem_fit = mlrose.TSPOpt(length=num_cities, fitness_fn=fitness_dists, maximize=False)

# Solve the problem using any TSP-compatible algorithm, here we use genetic algorithm
# Adjust algorithm and its parameters as needed
best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state=2)

# Ensure the tour starts and ends at the depot city 0
start_index = np.where(best_state == 0)[0][0]
shifted_tour = np.roll(best_state, -start_index).tolist() + [0]

# Output results
print("Tour:", shifted_tour)
print("Total travel, cost:", best_fitness)