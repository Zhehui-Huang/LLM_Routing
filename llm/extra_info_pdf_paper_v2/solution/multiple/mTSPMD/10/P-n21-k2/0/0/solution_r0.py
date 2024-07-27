import numpy as np
import random

# Define the coordinates of each city
cities = [
    (30, 40), # Depot for robot 0
    (37, 52), # Depot for robot 1
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Distance matrix
n_cities = len(cities)
distance_matrix = np.array([[euclidean_distance(cities[i], cities[j]) for j in range(n_cities)] for i in range(n_cities)])

# Ant Colony Optimization parameters
n_ants = 10
n_best = 5
n_iterations = 100
decay = 0.1
alpha = 1
beta = 5

# Initialize pheromones
pheromone = np.ones((n_cities, n_cities)) * 0.1

def aco_tsp():
    best_cost = float('inf')
    best_solution = None

    for _ in range(n_iterations):
        all_solutions = []
        for _ in range(n_ants):
            solution = [0, 1]  # Start each ant at each depot
            for i in range(2, n_cities):
                current = solution[-1]
                probabilities = pheromone[current] ** alpha * ((1.0 / distance_matrix[current]) ** beta)
                probabilities[solution] = 0  # Can't visit a city twice
                probabilities /= probabilities.sum()
                next_city = np.random.choice(np.arange(n_cities), p=probabilities)
                solution.append(next_city)
            solution.append(solution[0])  # Return to the starting depot
            solution.append(solution[1])  # Return to the second depot
            all_solutions.append(solution)

        for solution in all_solutions:
            cost = sum(distance_matrix[solution[i], solution[i+1]] for i in range(len(solution) - 1))
            if cost < best_cost:
                best_cost = cost
                best_solution = solution

        # Evaporate pheromones
        pheromone *= (1 - decay)

        # Update pheromones
        for solution in all_solutions[:n_best]:
            for i in range(len(solution) - 1):
                pheromone[solution[i], solution[i+1]] += 1.0 / distance_matrix[solution[i], solution[i+1]]

    return best_solution, best_cost

best_solution, best_cost = aco_tsp()

print(f'Best Tour: {best_solution}')
print(f'Best Tour Cost: {best_cost}')