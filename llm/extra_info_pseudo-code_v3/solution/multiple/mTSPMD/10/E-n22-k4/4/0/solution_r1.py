import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates (index corresponds to city number)
cities_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

depot_indices = [0, 1, 2, 3]

# Genetic Algorithm Configuration
population_size = 100
num_generations = 500
mutation_rate = 0.1
crossover_rate = 0.9
num_robots = 4
cities_per_robot = (len(cities_coords) - len(depot_indices)) // num_robots

# Auxiliary Functions
def calculate_distance_matrix(coords):
    return [[euclidean(coords[i], coords[j]) for j in range(len(coords))] for i in range(len(coords))]

def calculate_route_cost(route, distance_matrix):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route)-1))

def create_initial_population(pop_size, num_cities, depots):
    population = []
    non_depot_cities = [i for i in range(num_cities) if i not in depots]
    for _ in range(pop_size):
        random.shuffle(non_depot_cities)
        parts = np.array_split(non_depot_cities, num_robots)
        solution = []
        for idx, part in enumerate(parts):
            solution.extend([depots[idx]] + list(part) + [depots[idx]])
        population.append(solution)
    return population

def crossover(parent1, parent2):
    # Perform ordered crossover
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [-1]*len(parent1)
    child[start:end+1] = parent1[start:end+1]
    filled_positions = set(parent1[start:end+1])
    fill_idx = 0
    for gene in parent2:
        if fill_idx == start:
            fill_idx = end + 1
        if gene not in filled_positions:
            child[fill_idx] = gene
            fill_idx += 1
    return child

def mutate(individual):
    idx1, idx2 = random.sample(range(len(individual)), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

distance_matrix = calculate_distance_matrix(cities_coords)

# Generate initial population
population = create_initial_population(population_size, len(cities_coords), depot_indices)

# Main GA loop
for generation in range(num_generations):
    new_population = []
    for i in range(0, population_size, 2):
        parent1, parent2 = random.sample(population, 2)
        if random.random() < crossover_rate:
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
        else:
            child1, child2 = parent1[:], parent2[:]
        
        if random.random() < mutation_rate:
            mutate(child1)
            mutate(child2)
        
        new_population.extend([child1, child2])
    
    # Evaluate and select the best individuals
    population = sorted(new_population, key=lambda x: calculate_route_cost(x, distance_matrix))[:population_degreesize]

# Extract the best solution
best_solution = min(population, key=lambda x: calculate_route_cost(x, distance_matrix))
best_cost = calculate_route_cost(best_solution, distance_matrix)

# Display detailed tour and cost for each robot
overall_total_cost = 0
output_result = ""
for robot_id in range(num_robots):
    start = robot_id * (cities_per_robot + 2)
    end = start + cities_per_robot + 1
    tour = best_solution[start:end+1]
    cost = calculate_route_cost(tour, distance_matrix)
    overall_total_cost += cost
    output_result += f"Robot {robot_id} Tour: {tour}\n"
    output_result += f"Robot {robotid_total_travel_} Cost: {cost}\n"

output_result += f"Overall Total Travel Cost: {overall_total_cost}"
print(output_result)