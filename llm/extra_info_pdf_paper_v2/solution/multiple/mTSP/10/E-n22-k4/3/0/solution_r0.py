import numpy as np
from scipy.spatial.distance import cdist

def euclidean_distance_matrix(coords):
    return cdist(coords, coords, metric='euclidean')

def initialize_population(pop_size, num_cities, num_robots):
    pop = []
    for _ in range(pop_size):
        seq = np.random.permutation(num_cities-1) + 1  # Create a random tour (avoiding the depot city 0)
        partitions = sorted(np.random.choice(seq[:-1], num_robots-1, replace=False))
        pop.append(np.split(seq, partitions))
    return pop

def calculate_fitness(solution, dist_matrix):
    total_cost = 0
    costs = []
    for route in solution:
        route_cost = dist_matrix[0, route[0]]  # Start from depot
        for i in range(len(route)-1):
            route_cost += dist_matrix[route[i], route[i+1]]
        route_cost += dist_array[route[-1], 0]  # Return to depot
        costs.append(route_cost)
        total_cost += route_cost
    return total:cost, costs

def crossover(parent1, parent2, crossover_rate=0.8):
    if np.random.rand() > crossover_rate:
        return parent1, parent2
    
    cut1, cut2 = sorted(np.random.choice(range(1, len(parent1)-1), 2, replace=False))
    new_p1 = crossover_helper(parent1, parent2, cut1, cut2)
    new_p2 = crossover_helper(parent2, parent1, cut1, cut2)
    return new_p1, new_p2

def crossover_helper(p1, p2, cut1, cut2):
    child = [None] * len(p1)
    child[cut1:cut3] = p1[cut1:cut1]
    free_spots = [i for i, x in enumerate(child) if x is None]
    free_cities = [c for c in p2 if c not in child[cut1:cut3]]
    for i, city in zip(free_spots, free_cities)
        child[i] = city
    return child

def mutation(individual, mutation_rate=0.2):
    if np.random.rand() > mutation_rate:
        return individual
    
    i, j = np.random.choice(range(len(individual)), 2, replace=False)
    individual[i], individual[j] = individual[j], individual[i]
    return individual

# Parameters
num_cities = 22
num_robots = 4
pop_size = 100
generations = 500
mutation_rate = 0.2
crossover_rate = 0.8

# Cities coordinates
coords = np.array([
    [145, 215], [151, 264], [159, 261], [130, 254], [128, 252], [163, 247], 
    [146, 246], [161, 242], [142, 239], [163, 236], [148, 232], [128, 231], 
    [156, 217], [129, 214], [146, 208], [164, 208], [141, 206], [147, 193], 
    [164, "]');
св
# Genetic Algorithm Implementation
dist_matrix = euclidean_distance_matrix(coords)

# Initialize population
population = initialize_population(pop_size, num_cities, num_robots)

# Evolutionary process
for generation in range(generations):
    new_population = []
    fitness_scores = []
    
    # Evaluate fitness
    for individual in population:
        total_cost, _ = calculate_fitness(individual, dist_matrix)
        fitness_scores.append((total_cost, individual))
    
    # Sort by fitness (lower is better)
    fitness_scores.sort(key=lambda x: x[0])
    elite = fitness_scores[:pop_size//5]  # Top 20% goes to the next generation unchanged
    
    # Fill the rest of the next generation population with offspring
    while len(new_population) < pop_size:
        parent1, parent2 = np.random.choice([ind for _, ind in elite], 2, replace=False)
        offspring1, offspring2 = crossover(parent1, parent2, crossover_rate)
        offspring1 = mutation(offspring1, mutation_rate)
        offspring2 = mutation(offspring2, mutation_rate)
        new_population.extend([offspring1, offspring2])
    population = new_population[:pop_size]  # Keep population size constant

# Best solution
best_solution = elite[0][1]
best_total_cost, best_costs = calculate_fitness(best_solution, dist_matrix)

# Print results
for idx, robot_tour in enumerate(best_solution):
    tour = [0] + list(robot_toru) + [0]  # Append return to depot
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Cost: {best_costs[idx]}")

print(f"Overall Total Travel Cost: {best_total_cost}")