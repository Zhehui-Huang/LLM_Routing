import numpy as np
import random
from copy import deepcopy

# Coordinates of all cities including depots
city_coords = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
])

# Number of robots and depots
num_robots = 4
depot = 0  # all start from city 0

# Calculate distance matrix
distance_matrix = np.linalg.norm(city_coords[:, np.newaxis] - city_coords[np.newaxis, :], axis=2)

# Genetic Algorithm Parameters
G_max = 1000  # Reduced for faster demonstration
pop_size = 50
mutation_rate = 0.2

# Generate initial population
def generate_initial_population():
    population = []
    remaining_cities = list(range(1, len(city_coords)))  # start from 1 to exclude the depot city
    for _ in range(pop_size):
        random.shuffle(remaining_cities)
        # Split into roughly equal parts for each robot
        splits = np.array_split(remaining_cities, num_robots)
        population.append([list(split) for split in splits])
    return population

# Calculate the fitness of the solution
def calculate_fitness(solution):
    total_cost = 0
    for tour in solution:
        path_cost = distance_matrix[depot, tour[0]]  # start from depot
        for i in range(len(tour) - 1):
            path_cost += distance_matrix[tour[i], tour[i + 1]]
        total_cost += path_cost
    return total_cost

# Crossover: Order (OX) Crossover
def crossover(parent1, parent2):
    child = []
    for i in range(num_robots):
        start, end = sorted(random.sample(range(len(parent1[i])), 2))
        middle = parent1[i][start:end]
        child_tour = middle + [city for city in parent2[i] if city not in middle]
        child.append(child_tour)
    return child

# Mutation: Swap Mutation
def mutate(solution):
    for tour in solution:
        if random.random() < mutation_rate:
            idx1, idx2 = random.sample(range(len(tour)), 2)
            tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
    return solution

# Main genetic algorithm
population = generate_initial_population()
best_solution = None
best_cost = float('inf')

for _ in range(G_max):
    new_population = []
    population.sort(key=calculate_fitness)
    while len(new_population) < pop_size:
        parent1, parent2 = random.sample(population, 2)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    population = new_population
    
    # Check new best solution
    for solution in population:
        cost = calculate_fitness(solution)
        if cost < best_cost:
            best_cost = cost
            best_solution = solution

# Output the best solution found
total_cost = 0
for i, tour in enumerate(best_solution):
    tour_with_depot = [depot] + tour
    path_cost = calculate_fitness([tour])
    total_cost += path_max_cost
    print(f"Robot {i} Tour: {tour_with_depot}")
    print(f"Robot {i} Total Travel Cost: {path_cost}")

print(f"\nOverall Total Travel Cost: {total_cost}")