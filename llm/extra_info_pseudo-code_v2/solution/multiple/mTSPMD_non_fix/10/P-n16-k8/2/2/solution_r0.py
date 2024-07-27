import numpy as np
import random

# Environment and Robot setup
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
num_robots = 8
depot = cities[0]

# Distance calculation
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate initial population
def create_chromosome(num_cities, num_robots):
    genes = list(range(1, num_cities))
    random.shuffle(genes)
    genes.insert(0, 0)
    genes.append(0)
    return genes

# Calculate total and individual travel costs
def evaluate_tour(chromosome):
    total_cost = 0
    costs = []
    start_idx = 0
    
    for i in range(1, len(chromosome)):
        if chromosome[i] == 0:
            cost = sum(euclidean_distance(cities[chromosome[j]], cities[chromosome[j + 1]]) 
                       for j in range(start_idx, i))
            costs.append(cost)
            total_cost += cost
            start_idx = i
            
    return costs, total_cost

# Genetic operators: Crossover and mutation
def crossover(parent1, parent2):
    size = len(parent1)
    child = [-1] * size
    start, end = sorted(random.sample(range(size), 2))
    child[start:end] = parent1[start:end]
    
    fill_positions = list(set(range(size)) - set(range(start, end)))
    fill_values = [x for x in parent2 if x not in parent1[start:end]]
    for pos, val in zip(fill_positions, fill_values):
        child[pos] = val
    return child

def mutate(chromosome):
    idx1, idx2 = random.sample(range(1, len(chromosome) - 1), 2)
    chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]

# Genetic algorithm execution
def genetic_algorithm(generations, population_size):
    population = [create_chromosome(len(cities), num_robots) for _ in range(population_size)]
    history = []
    
    for g in range(generations):
        # Evaluate population
        scores = np.array([evaluate_tour(ch)[1] for ch in population])
        best_idx = np.argmin(scores)
        history.append((population[best_idx], scores[best_idx]))
        
        new_population = [population[best_idx]]  # Elitism: keep the best
        
        while len(new_population) < population_size:
            p1, p2 = random.choices(population, k=2)
            child = crossover(p1, p2)
            if random.random() < 0.1:  # Mutation rate
                mutate(child)
            new_population.append(child)
            
        population = new_population
    
    return history[-1]

# Perform the genetic algorithm
best_solution = genetic_algorithm(100, 50)
best_chromosome, best_score = best_solution

# Output the best tours and costs
costs, total_cost = evaluate_tour(best_chromosome)
output = ""
for robot_id, start in enumerate([0] + costs[:-1]):
    tour = best_chromosome[start:start+costs[robot_id]+1]
    output += f"Robot {robot_id} Tour: {tour}\n"
    output += f"Robot {robot_id} Total Travel Cost: {costs[robot_id]}\n"
output += f"Overall Total Travel Cost: {total_cost}\n"

print(output)