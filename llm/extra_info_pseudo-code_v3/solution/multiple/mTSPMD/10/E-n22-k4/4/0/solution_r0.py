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
num_genes = len(cities_coords)

# Auxiliary Functions
def calculate_distance_matrix(coords):
    return [[euclidean(coords[i], coords[j]) for j in range(len(coords))] for i in range(len(coords))]

def calculate_route_cost(route, distance_matrix):
    return sum(distance_frame[route[i]][route[i + 1]] for i in range(len(route)-1))

def create_initial_population(pop_size, num_cities, depots):
    population = []
    non_depot_cities = [i for i in range(num_cities) if i not in depots]
    for _ in range(pop_size):
        random.shuffle(non_depot_cities)
        tours = depots[:]
        start_index = 0
        for d in tours:
            end_index = start_index + len(non_depot_cities) // num_robots 
            if d == depots[-1]:  # Ensure all cities are included
                current_cities = non_depot_cities[start__index:]
            else:
                current_cities = non_depot_cities[start_index:end_index]
            tours += [d] + current_cities + [d]
            start_index = end_index
        population.append(tours)
    return population

def crossover(parent1, parent2):
    # Implement single point crossover
    point = random.randint(1, len(parent1)-2)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual):
    idx1, idx2 = random.sample(range(1, len(individual)-1), 2)  # Do not mutate the depot position
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

distance_frame = calculate_distance_matrix(cities_coords)

# Generate initial population
population = create_initial_population(population_size, num_genes, depot_indices)

# Main GA loop
for generation in range(num_generations):
    new_population = []
    for _ in range(population_size // 2):
        parent1, parent2 = random.sample(population, 2)
        if random.random() < crossover_rate:
            child1, child2 = crossover(parent1, parent2)
        else:
            child1, child2 = parent1, parent2
        
        if random.random() < mutation_rate:
            mutate(child1)
            mutate(child2)
        
        new_population.extend([child1, child2])
    
    # Evaluate and select the best individuals
    population = sorted(new_population, key=lambda x: calculate_route_cost(x, distance_frame))[:population_size]

# Extract the best solution
best_solution = min(population, key=lambda x: calculate_route_cost(x, distance_frame))
best_cost = calculate_route_cost(best_solution, distance_frame)

solution_details = f"Robot {robot_id} Tour: {tour}\nRobot {robot_id} Total Travel Cost: {cost}"

# Output results
print(solution_details)
print(f"Overall Total Travel Cost: {best_cost}")