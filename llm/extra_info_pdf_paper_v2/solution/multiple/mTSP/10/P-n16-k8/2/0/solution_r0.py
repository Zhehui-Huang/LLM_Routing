import numpy asjson
import math
import random
from operator import attrgetter

# Define the city coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Define the number of robots
num_robots = 8

# Euclidean distance calculation
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate random initial population for the genetic algorithm
def generate_individual():
    cities_tour = list(range(1, len(cities)))  # Start from 1 to exclude the depot
    random.shuffle(cities_tour)
    return cities_tour

# Fitness function to evaluate tours
def evaluate(individual):
    chunks = [individual[i::num_robots] for i in range(num_robots)]
    total_cost = 0
    tours = []
    for robot in range(num_robots):
        tour = [0] + chunks[robot] + [0]
        tours.append(tour)
        cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        total_cost += cost
    return total_cost, tours

# Genetic operators: Crossover and mutation
def crossover(parent1, parent2):
    child = parent1[:] 
    start, end = sorted(random.sample(range(len(parent1)), 2))
    middle = parent2[start:end+1]
    child = [city for city in child if city not in middle]
    return child[:start] + middle + child[start:]

def mutate(individual):
    idx1, idx2 = random.sample(range(len(individual)), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Main Genetic Algorithm execution
def genetic_algorithm(population_size=100, generations=500):
    population = [generate_individual() for _ in range(population_size)]
    best_individual = None
    
    for generation in range(generations):
        evaluated_population = [(evaluate(ind), ind) for ind in population]
        evaluated_population.sort(key=lambda x: x[0][0])  # sort by total cost
        if not best_individual or evaluated_population[0][0][0] < best_individual[0][0][0]:
            best_individual = evaluated_population[0]

        # Create the next generation
        new_population = [best_individual[1]]
        while len(new_population) < population_size:
            parents = random.sample(population, 2)
            child = crossover(parents[0], parents[1])
            if random.random() < 0.1:  # mutation chance
                mutate(child)
            new_population.append(child)
        
        population = new_population
    
    return best_individual

# Run the genetic algorithm
best_solution = genetic_algorithm()

# Output results
best_cost, best_tours = best_solution[0]
overall_total_cost = best_cost
print("Overall Total Travel Cost:", overall_total_cost)
for idx, tour in enumerate(best_tours):
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")