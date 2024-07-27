import numpy as np
import random
from scipy.spatial import distance_matrix

# Define coordinates for all cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Compute distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Configuration
num_robots = 8
depot_indices = list(range(num_robots))  # Robots' starting depots are the first 8 cities

# Initialize GA parameters
population_size = 100
generations = 500
mutation_rate = 0.1

def create_initial_population():
    population = []
    non_depot_cities = list(set(range(len(coordinates))) - set(depot_indices))
    for _ in range(population_size):
        random.shuffle(non_depot_cities)
        population.append(non_depot_cities[:])
    return population

def fitness(chromosome):
    # To hold the global tour assignments, assuming roughly equal split of cities among robots
    chunks = np.array_split(chromosome, num_robots)
    total_cost = 0
    robot_tours = []
    
    for depot, chunk in zip(depot_indices, chunks):
        tour = [depot] + list(chunk) + [depot]
        cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
        total_cost += cost
        robot_tours.append((tour, cost))
        
    return total_cost, robot_tours

def selection(population, fitness_scores):
    probs = [1/f for f in fitness_scores]
    probs /= np.sum(probs)
    selected_indices = np.random.choice(len(population), size=len(population), replace=True, p=probs)
    return [population[i] for i in selected_indices]

def crossover(parent1, parent2):
    size = len(parent1)
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    temp = parent1[cxpoint1:cxpoint2+1]
    child = []
    for gene in parent2:
        if gene not in temp:
            child.append(gene)
    child[cxpoint1:cxpoint1] = temp
    return child

def mutate(chromosome):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(chromosome)), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]

def genetic_algorithm():
    population = create_initial_population()
    best_tours = None
    best_cost = float('inf')
    
    for generation in range(generations):
        new_population = []
        fitness_scores = []
        tour_sets = []
        
        for individual in population:
            cost, tours = fitness(individual)
            fitness_scores.append(cost)
            tour_sets.append(tours)
            
        min_cost_idx = np.argmin(fitness_scores)
        if fitness_scores[min_cost_idx] < best_cost:
            best_cost = fitness_scores[min_cost_idx]
            best_tours = tour_sets[min_cost_idx]
        
        population = selection(population, fitness_scores)
        
        for i in range(0, len(population), 2):
            if i + 1 < len(population):
                child = crossover(population[i], population[i+1])
                mutate(child)
                new_population.append(child)
                new_population.append(population[i])  # Keep some previous individuals
                
        population = new_population
        
    return best_tours, best_cost

best_tours, overall_cost = genetic_algorithm()

# Output results
for robot_id, (tour, cost) in enumerate(best_tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")