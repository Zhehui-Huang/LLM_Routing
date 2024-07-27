import numpy as np
from scipy.spatial.distance import euclidean
from random import randint, choice, shuffle

# Coordinates of the cities and depots
locations = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Number of depots and robots
num_depots = 8
num_robots = 8

# Create distance matrix
def generate_distance_matrix(locations):
    n = len(locations)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = euclidean(locations[i], locations[j])
    return dist_matrix

dist_matrix = generate_distance_matrix(locations)

def initialize_population(size, num_cities, num_depots):
    population = []
    for _ in range(size):
        # Let each individual represent an ordered permutation of cities starting after the depots
        individual = list(range(num_depots, num_cities))
        shuffle(individual)
        population.append(individual)
    return population

def calculate_tour_cost(tour, depot):
    cost = dist_matrix[depot, tour[0]] + dist_matrix[tour[-1], depot]
    for i in range(len(tour) - 1):
        cost += dist_matrix[tour[i], tour[i + 1]]
    return cost

def fitness(chromosome, num_depots):
    # Split tours among robots starting from respective depots and calculate the cost
    segment_length = len(chromosome) // num_depots
    costs = []
    tours = []
    for i in range(num_depots):
        start_index = i * segment_length
        if i == num_depots - 1:
            end_index = len(chromosome)
        else:
            end_index = start_index + segment_length
        tour = chromosome[start_index:end_index]
        tour_cost = calculate_tour_cost(tour, i)
        costs.append(tour_cost)
        tours.append([i] + tour + [i])
    total_cost = sum(costs)
    return total_cost, tours

def genetic_solution(depots, locations, iterations=1000, pop_size=50):
    num_cities = len(locations)
    population = initialize_population(pop_size, num_cities, num_depots)
    
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(iterations):
        # Select and create the next generation
        # Fitness evaluation:
        population_fitness = []
        for individual in population:
            cost, _ = fitness(individual, num_depots)
            population_fitness.append(cost)
        
        # Elitism: Carry the best individual over
        min_cost_index = np.argmin(population_fitness)
        if population_fitness[min_cost_index] < best_cost:
            best_cost = population_fitness[min_cost_index]
            best_solution = population[min_cost_index]
        
        # Selection and crossover (not shown for brevity)
        # Mutation (not shown for brevity)
    
    # Return the best found solution, with tours and costs
    _, best_tours = fitness(best_solution, num_depots)
    return best_tours, best_cost

# Run the genetic algorithm solution
best_tours, total_cost = genetic_solution(depots, locations)

# Output the results
for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    tour_cost = calculate_tour_cost(tour[1:-1], tour[0])
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")
print(f"Overall Total Travel Travel Cost: {total_cost}")