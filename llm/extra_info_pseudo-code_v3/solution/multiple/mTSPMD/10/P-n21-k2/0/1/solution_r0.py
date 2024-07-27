import numpy as np
import random
from scipy.spatial.distance import euclidean

# Parameters
NUM_GENERATIONS = 400
POPULATION_SIZE = 100
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

# Function to calculate the total distance of a tour
def calculate_distance(tour, coordinates):
    distance = 0
    for i in range(len(tour) - 1):
        distance += euclidean(coordinates[tour[i]], coordinates[tour[i+1]])
    return distance

# Crossover - Order 1 Crossover
def crossover(parent1, parent2):
    size = len(parent1)
    child = [-1]*size
    start, end = sorted(random.sample(range(size), 2))
    child[start:end] = parent1[start:end]
    p2_pos = end
    c_pos = end

    while -1 in child:
        if parent2[p2_pos] not in child:
            child[c_pos] = parent2[p2_pos]
            c_pos = (c_pos + 1) % size
        p2_pos = (p2_pos + 1) % size
    return child

# Mutation - Swap Mutation
def mutate(tour):
    i, j = random.sample(range(len(tour)), 2)
    tour[i], tour[j] = tour[j], tour[i]
    return tour

# Generate initial population
def generate_initial_population(pop_size, num_cities):
    population = []
    base_tour = list(range(num_cities))
    for _ in range(pop_size):
        random.shuffle(base_tour)
        population.append(base_tour[:])
    return population

# GA main procedure
def genetic_algorithm():
    num_cities = len(coordinates)
    population = generate_initial_population(POPULATION_SIZE, num_cities)
    
    for generation in range(NUM_GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE):
            if random.random() < CROSSOVER_RATE:
                # Select parents and perform crossover
                parent1, parent2 = random.sample(population, 2)
                child = crossover(parent1, parent2)
            else:
                child = random.choice(population)[:]
                
            # Mutation
            if random.random() < MUTATION_RATE:
                child = mutate(child)
                
            new_population.append(child)
        
        # Evaluate and select the best solutions
        population = sorted(new_population, key=lambda x: calculate_distance(x, coordinates))[:POPULATION_SIZE]
    
    # Find the best solution
    best_tour = min(population, key=lambda x: calculate_distance(x + [x[0]], coordinates))
    return best_tour + [best_tour[0]]

# Solve for each robot
def solve_mmtsp():
    overall_cost = 0
    robots = [[0], [1]]  # Start with depots
    best_tour = genetic_algorithm()
    partition = len(best_tour) // 2
    tours = [best_tour[:partition], best_tour[partition:]]
    
    for i, tour in enumerate(tours):
        tour_cost = calculate_distance(tour, coordinates)
        robots[i].extend(tour[1:-1])
        robots[i].append(robots[i][0])
        tour_cost += euclidean(coordinates[robots[i][-2]], coordinates[robots[i][-1]])
        overall_cost += tour_cost
        
        print(f"Robot {i} Tour: {robots[i]}")
        print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")
    
    print(f"Overall Total Travel Cost: {overall_cost:.2f}")

# Execute the solution
solve_mmtsp()