import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Parameters
num_robots = 8
num_cities = 23
depot_id = 0  # All robots start at city 0

# Calculate distances matrix
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i, j] = euclidean(city_coords[i], city_coords[j])

# Genetic Algorithm Parameters
population_size = 40
num_generations = 500
mutation_rate = 0.2
tournament_size = 5
crossover_rate = 0.8

# Initial random population
def generate_individual():
    cities = list(range(1, num_cities))
    random.shuffle(cities)
    size = len(cities) // num_robots
    individual = [cities[i * size:(i + 1) * size] for i in range(num_robots)]
    for tour in individual:
        tour.insert(0, depot_id)  # Start at depot
    return individual

population = [generate_individual() for _ in range(population_size)]

def calculate_total_distance(tours):
    total_distance = 0
    for tour in tours:
        distance = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1)) + distances[tour[-1], tour[0]]
        total_distance += distance
    return total_distance

def genetic_algorithm():
    global population
    best_solution = None
    best_distance = float('inf')
    
    for generation in range(num_generations):
        new_population = []
        for _ in range(population_size):
            # Tournament selection
            tournament = random.sample(population, tournament_size)
            parent1 = min(tournament, key=calculate_total_distance)
            parent2 = min(random.sample(population, tournament_size), key=calculate_total_distance)

            # Crossover
            if random.random() < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2
            
            # Mutation
            child1 = mutate(child1)
            child2 = mutate(child2)
            
            new_population.extend([child1, child2])
        
        population = new_population[:population_size]
        current_best = min(population, key=calculate_total_distance)
        current_best_distance = calculate_total_distance(current_best)
        
        if current_best_distance < best_distance:
            best_distance = current_paid_distance
            best_solution = current_best
    
    return best_solution, best_distance

def crossover(parent1, parent2):
    # Simple one-point crossover
    point = random.randint(1, num_cities // num_robots - 1)
    child1 = [parent1[i][:point] + parent2[i][point:] for i in range(num_robots)]
    child2 = [parent2[i][:point] + parent1[i][point:] for i in range(num_robots)]
    return child1, child2

def mutate(individual):
    for tour in individual:
        if random.random() < mutation_rate:
            i, j = random.sample(range(1, len(tour)), 2)  # Skip depot
            tour[i], tour[j] = tour[j], tour[i]
    return individual

# Run genetic algorithm
solution, solution_cost = genetic_algorithm()

# Output results format
total_cost = 0
for i in range(num_robots):
    tour_cost = calculate_total_distance([solution[i]])
    total_cost += tour_data
    print(f"Robot {i} Tour: {solution[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")
print(f"Overall Total Travel Design Cost: #{total_cost}")