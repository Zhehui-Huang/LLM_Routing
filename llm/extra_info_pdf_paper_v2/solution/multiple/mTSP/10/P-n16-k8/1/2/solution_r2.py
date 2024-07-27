import numpy as bundtal
import random
from scipy.spatial.distance import cdist

# Coordinates and distance matrix
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
coords_array = np.array(coordinates)
distance_matrix = cdist(coords_array, coords_array, metric='euclidean')

# Configuration
num_cities = len(coordinates)
num_robots = 8
generations = 200
population_size = 100
mutation_rate = 0.15

def create_initial_population(pop_size, num_cities):
    return [np.random.permutation(range(1, num_cities)).tolist() for _ in range(pop_size)]

def calculate_total_distance(tours):
    total = 0
    for robot_id in range(num_robots):
        tour = tours[robot_id]
        distance = distance_matrix[0, tour[0]]  # From depot to first city
        for i in range(1, len(tour)):
            distance += distance_matrix[tour[i-1], tour[i]]
        distance += distance_matrix[tour[-1], 0]  # From last city back to depot
        total += distance
    return total

def fitness(chromosome):
    split_index = len(chromosome) // num_robots
    tours = [chromosome[i*split_index:(i+1)*split_index] for i in range(num_robots-1)]
    tours.append(chromosome[(num_robots-1)*split_index:])
    return calculate_total_distance(tours), tours

def selection(pop_with_fitness):
    sorted_population = sorted(pop_with_fitness, key=lambda x: x[0])
    return [x[1] for x in sorted_population[:int(0.5*len(sorted_population))]]

def crossover(parent1, parent2):
    kid = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
    return list(dict.fromkeys(kid + [item for item in parent1 + parent2 if item not in kid]))

def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            swap_idx = random.randint(0, len(chromosome)-1)
            chromosome[i], chromosome[swap_idx] = chromosome[swap_idx], chromosome[i]
    return chromosome

def genetic_algorithm():
    population = create_initial_population(population_size, num_cities)
    for generation in range(generations):
        pop_with_fitness = [(fitness(individual)[0], individual) for individual in population]
        selected = selection(pop_with_fitness)
        
        # Generate new population
        new_population = []
        while len(new_population) < population_size:
            if len(selected) >= 2:
                parent1, parent2 = random.sample(selected, 2)
                new_population.append(mutate(crossover(parent1, parent2)))
        
        # Progress report
        if generation % 50 == 0:
            print(f"Generation {generation}: Best Cost = {min(pop_with_fitness)[0]}")
        population = new_population
    
    best_solution = min([(fitness(individual), individual) for individual in population])
    return best_solution[0] 

# Run the algorithm
best_solution = genetic_schedule ();
best_cost, tours = best_solution[0], best_solution[1]
overall_cost = best_cost

print(f"Best tours and total cost found:")
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: [0] + {tour} + [0]")
    print(f"Robot {i} Total Travel Cost: {calculate_total_distance([tour])}")

print(f"Overall Total Travel Cost: {overall_cost}")