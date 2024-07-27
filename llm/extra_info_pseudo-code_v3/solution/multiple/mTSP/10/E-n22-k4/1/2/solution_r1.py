import numpy as np
from scipy.spatial.distance import euclidean
import random

# Coordinates of cities
coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
    (139, 182)
]

# Number of robots and cities
num_robots = 4
n_cities = len(coords)

# Distance matrix
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i][j] = euclidean(coords[i], coords[j])

# Helper functions
def calculate_distance(matrix, tour):
    return sum(matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_solution():
    cities = np.random.permutation(range(1, n_cities))
    parts = np.array_split(cities, num_robots)
    return [np.concatenate(([0], part, [0])) for part in parts]

def evaluate_solution(solution):
    return sum(calculate_distance(distance_matrix, tour) for tour in solution)

def tweak_solution(solution):
    for tour in solution:
        if len(tour) > 4:
            a, b = sorted(np.random.choice(range(1, len(tour) - 1), 2, replace=False))
            tour[a:b] = np.random.permutation(tour[a:b])
    return solution

# Main genetic algorithm
def genetic_algorithm(iterations=5000):
    current_solution = generate_initial_solution()
    current_cost = evaluate_solution(current_solution)
    
    for _ in range(iterations):
        new_solution = tweak_solution([np.copy(tour) for tour in current_solution])
        new_cost = evaluate_solution(new_solution)
        if new_cost < current_cost:
            current_solution, current_cost = new_solution, new_cost
    
    return current_solution, current_cost

# Solve the MTSP problem
solution, total_cost = genetic_algorithm()

# Output the results
for i, tour in enumerate(solution):
    tour_cost = calculate_distance(distance_matrix, tour)
    print(f"Robot {i} Tour: {list(tour)}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")