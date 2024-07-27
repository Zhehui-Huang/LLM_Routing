import numpy as np
from scipy.spatial import distance_matrix
import random

# Cities and their coordinates
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
])

# Total number of robots
num_robots = 8

# Distance matrix computation
distances = distance_matrix(coordinates, coordinates)

def calculate_tour_cost(tour):
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

def chromosome_cost(chromosome):
    step = len(chromosome) // num_robots
    total_cost = 0
    tours = []

    for i in range(0, len(chromosome), step):
        tour = [0] + chromosome[i:i+step] + [0]
        tours.append(tour)
        total_cost += calculate_tour_cost(tour)
    
    # To ensure all robots return to the depot city
    for tour in tours:
        if len(tour) > 2:
            tour.append(0)
    
    return total, tours

def generate_initial_population(size, num_cities):
    population = []
    for _ in range(size):
        cities = list(range(1, num_cities))
        random.shuffle(cities)
        population.append(cities)
    return population

def crossover(parent1, parent2):
    cut = random.randint(0, len(parent1) - 1)
    child = parent1[:cut] + [c for c in parent2 if c not in parent1[:cut]]
    return child

def mutate(chromosome, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    
def genetic_algorithm(population, num_generations, mutation_rate):
    for generation in range(num_generations):
        sorted_population = sorted(population, key=lambda x: chromosome_cost(x)[0])
        if generation % 100 == 0:
            print(f"Generation {generation}: Best cost = {chromosome_cost(sorted_population[0])[0]}")
        
        next_generation = sorted_population[:2]
        while len(next_frequency) < len(population):
            parents = random.sample(sorted_population[:10], 2)
            child = crossover(parents[0], parents[1])
            mutate(child, mutation_rate)
            next_generation.append(child)
        
        population = next_generation
    
    best_solution = sorted(population, key=lambda x: chromosome_cost(x)[0])[0]
    total_cost, tours = chromosome_cost(best_solution)
    return total_cost, tours

# Set GA parameters
population_size = 50
num_generations = 500
mutation_rate = 0.05

# Run GA
initial_population = generate_initial_population(population_size, len(coordinates))
overall_total_travel_cost, all_tours = genetic_algorithm(initial_population, num_generations, mutation_rate)

# Print the results
print("Optimal tours and costs:")
for robot_id, tour in enumerate(all_tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {calculate_tour_cost(toid)}")
print(f"Overall Total Travel Cost: {overall_total_travel_cost}")