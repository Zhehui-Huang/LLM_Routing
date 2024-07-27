import numpy as np
import random

# Coordinates of each city including depots
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

num_cities = len(coordinates)
num_robots = 2

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Initialize population
def initialize_population(pop_size, num_cities, num_robots):
    population = []
    for _ in range(pop_size):
        # Create a list of city indices
        perm = list(np.random.permutation(range(2, num_cities)))  # start from 2 to exclude depots
        # Random positions to split tours, avoiding the first and the last element
        splits = sorted(random.sample(range(1, num_cities - 1), num_robots - 1))
        chromosome = [0] + perm[:splits[0]] + [1] + perm[splits[0]:]
        population.append(chromosome)
    return population

# Calculate the cost of tours
def calculate_cost(chromosome):
    total_cost = 0
    tour_costs = []
    current_tour = [chromosome[0]]
    start_city = chromosome[0]

    for city in chromosome[1:]:
        if city == 1:  # Encountering the other depot
            total_cost += euclidean_distance(current_tour[-1], start_city)
            tour_costs.append((current_tour + [start_city], total_cost))
            start_city = city
            current_tour = [city]
            total_cost = 0
        else:
            total_cost += euclidean_distance(current_tour[-1], city)
            current_tour.append(city)

    # finalize the last tour
    total_cost += euclidean_distance(current_tour[-1], start_city)
    tour_costs.append((current_tour + [start_city], total_cost))
    
    global_cost = sum(cost for _, cost in tour_costs)
    return tour_costs, global_cost

# Genetic Algorithm main function
def genetic_algorithm(num_cities, num_robots, pop_size=100, num_generations=1000):
    population = initialize_population(pop_size, num_cities, num_robots)
    best_solution = None
    best_cost = float('inf')
    
    for generation in range(num_generations):
        new_population = []
        costs = []
        
        for chromosome in population:
            _, cost = calculate_cost(chromosome)
            costs.append(cost)
            if cost < best_cost:
                best_solution = chromosome
                best_cost = cost
                
        # Selection based on cost
        selected = [population[i] for i in np.argsort(costs)[:pop_size//2]]
        
        # Crossover and mutation not fully described, placeholders here:
        # Mutation (naive implementation: swap two random cities)
        for i in range(len(selected)//2):
            if random.random() < 0.1:  # Mutation rate
                idx1, idx2 = random.sample(range(2, len(selected[i])), 2)  # mutate within cities only
                selected[i][idx1], selected[i][idx2] = selected[i][idx2], selected[i][idx1]
        
        new_population.extend(selected)
        new_population.extend(random.choices(population, k=(pop_size-len(selected))))
        population = new_population

    return best_solution, best_cost

# Running the Genetic Algorithm
best_solution, best_cost = genetic_algorithm(num_cities, num_robots)
tour_descriptions, total_cost = calculate_cost(best_solution)
for idx, (tour, cost) in enumerate(tour_descriptions):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {round(cost, 2)}")
print(f"Overall Total Travel Cost: {round(total_cost, 2)}")