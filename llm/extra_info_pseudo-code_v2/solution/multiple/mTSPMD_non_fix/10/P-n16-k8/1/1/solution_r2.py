import numpy as np
import random
import math
from copy import deepcopy

# Coordinates (x, y) for each city including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Define utility functions
def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.hypot(x2 - x1, y2 - y1)

def create_initial_population(population_size, num_cities=16, num_robots=8):
    """Generate the initial population of tours."""
    population = []
    for _ in range(population_size):
        # Create a permutation of cities except the depot city 0
        cities = list(range(1, num_cities))
        random.shuffle(cities)

        # Distribute cities among robots
        tours = [[] for _ in range(num_robots)]
        for i, city in enumerate(cities):
            tours[i % num_robots].append(city)

        # Ensure each robot starts and ends at the depot city 0
        for tour in tours:
            tour.insert(0, 0)
            tour.append(0)
        population.append(tours)
    return population

def total_distance(tour):
    """Calculate the total distance for a tour."""
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def fitness(population):
    """Calculate the total fitness for the population."""
    return [sum(total_distance(tour) for tour in individual) for individual in population]

def select_parents(population, fitnesses):
    """Select pairs of parents using a tournament selection mechanism."""
    selected = []
    for _ in range(len(population)):
        competitors = random.sample(list(zip(population, fitnesses)), k=3)
        selected.append(min(competitors, key=lambda item: item[1])[0])
    return selected

def crossover(parent1, parent2):
    """Perform crossover between two parent tours."""
    point = random.randint(1, len(parent1) - 2)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return [child1, child2]

def mutate(tour, mutation_rate=0.2):
    """Perform mutation on a tour."""
    for i in range(1, len(tour)-1):
        if random.random() < mutation_rate:
            j = random.randint(1, len(tour)-2)
            tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm(population_size, num_generations, num_cities=16, num_robots=8):
    """Run the genetic algorithm to optimize the tours."""
    population = create_initial_population(population_size, num_cities, num_robots)
    for generation in range(num_generations):
        # Calculate fitness for each individual in the population
        fit_vals = fitness(population)
        
        # Selection of parents
        parents = select_parents(population, fit_vals)
        
        # Crossover and mutation
        children = []
        for i in range(0, len(parents), 2):
            for child in crossover(parents[i], parents[(i+1) % len(parents)]):
                children.append([mutate(tour) for tour in child])
                
        # Replace old population with new one
        population = children
        best_individual = min(population, key=lambda x: sum(total_distance(tour) for tour in x))
        best_cost = sum(total_distance(tour) for tour in best_individual)

        # Optionally print the best cost in each generation
        print(f"Generation {generation}: Best Cost {best_cost}")
    
    return best_individual, best_cost

# Parameters
population_size = 50
num_generations = 100

best_solution, best_cost = genetic_algorithm(population_size, num_generations)

# Output the results
print("Best solution tours and costs:")
total_cost = 0
for idx, tour in enumerate(best_solution):
    tour_cost = total_distance(tour)
    total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")