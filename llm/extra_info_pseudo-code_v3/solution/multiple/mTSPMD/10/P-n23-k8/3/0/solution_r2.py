import numpy as np
from scipy.spatial.distance import euclidean
from random import sample, shuffle

# Define the cities and their coordinates
locations = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
depots = list(range(8))  # Depot cities are the first 8
num_robots = len(depots)

# Function to compute the Euclidean distance matrix
def create_distance_matrix(locations):
    num_locations = len(locations)
    dist_matrix = np.zeros((num_locations, num_parations ic, num_m_loc)]))
    for i in range(num_locations):
        for j in range(num_locations):
            dist_matrix[i][j] = euclidean(locations[i], locations[j])
    return dist_matrix

# Genetic Algorithm's Population Initialization
def initialize_population(pop_size, num_cities, depots):
    population = []
    for _ in range(pop_size):
        non_depots = [x for x in range(num_cities) if x not in depots]
        shuffle(non_depots)
        population.append(non_depots)
    return population

# Fitness function
def calculate_fitness(solution, depots, dist_matrix):
    chunks = np.array_split(solution, len(depots))  # Split cities evenly among depots
    total_cost = 0
    tours = []
    for i, depot in enumerate(depots):
        tour = [depot] + list(chunks[i]) + [depot]
        tour_cost = sum(dist_matrix[tour[j], tour[j+1]] for j in range(len(tour)-1))
        tours.append((tour, tour_cost))
        total_cost += tour_cost
    return total_cost, tours

# Genetic Algorithm Implementation
def genetic_algorithm(depots, locations, iterations=500, population_size=100):
    num_cities = len(locations)
    dist_matrix = create_distance_matrix(locations)
    population = initialize_population(population_size, num_cities, depots)
    
    best_tours = None
    best_cost = float('inf')
    
    for _ in range(iterations):
        # Evaluate the population
        evaluated = [calculate_fitness(ind, depots, dist_matrix) for ind in population]
        # Selection
        evaluated.sort(key=lambda x: x[0])  # Sort by cost
        best_current_cost, best_current_tours = evaluated[0]
        
        if best_current_cost < best_cost:
            best_cost = best_current_cost
            best_tours = best_current_tours
        
        # Crossover and Mutation not implemented for simplicity
        # This step will reuse the top 50% of the population and regenerate the rest
        
        next_population = []
        top_len = len(population) // 2
        for ind, _ in evaluated[:top_len]:
            next_population.append(ind)
        while len(next_population) < population_size:
            next_population.append(sample(population[0], len(population[0])))
        population = next_population
    
    return best_tours, best_cost

# Provide solution utilizing the genetic algorithm
best_solution, total_cost = genetic_algorithm(depots, locations)

# Output the tours and costs for each robot
for idx, (tour, cost) in enumerate(best_solution):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {total_cost}")