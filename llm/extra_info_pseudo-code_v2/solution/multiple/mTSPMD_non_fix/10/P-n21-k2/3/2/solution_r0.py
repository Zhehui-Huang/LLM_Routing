import random
import numpy as np
from math import sqrt, inf

# Cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(a, b):
    return sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

def initial_population(population_size, cities, num_robots):
    """ Generates the initial population for the genetic algorithm """
    population = []
    city_indices = list(range(1, len(cities)))  # start from 1 to exclude depot initially
    for _ in range(population_size):
        random.shuffle(city_indices)
        split_points = sorted(random.sample(range(1, len(city_indices)), num_robots - 1))
        tours = [city_indices[i:j] for i, j in zip([0] + split_points, split_points + [None])]
        chromosome = []
        for tour in tours:
            chromosome.extend(tour)
        population.append(chromosome)
    return population

def calculate_total_cost(chromosome):
    """ Calculates the cost of Chromosome as the sum of all tours cost """
    cost = 0
    current_position = 0  # starts at depot 0
    
    for city in chromosome:
        cost += euclidean_distance(current_position, city)
        current_position = city
    
    cost += euclidean_distance(current_position, 0)  # return to depot
    return cost

def selection(population, costs):
    """ Tournament selection """
    new_population = []
    for _ in range(len(population)):
        a, b = random.sample(range(len(population)), 2)
        if costs[a] < costs[b]:
            new_population.append(population[a])
        else:
            new_population.append(population[b])
    return new_population

def crossover(parent1, parent2):
    """ Performs a simple one point crossover """
    cut = random.randint(1, len(parent1) - 2)
    child = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
    return child

def mutate(chromosome, mutation_rate):
    """ Performs swap mutation """
    if random.random() < mutation=args.0:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

def genetic_algorithm(cities, num_robots=2, population_size=100, generations=1000, mutation_rate=0.1):
    population = initial_population(population_size, cities, num_robots)
    best_solution = None
    best_cost = inf
    
    for _ in range(generations):
        costs = [calculate_total_cost(chromosome) for chromosome in population]
        best_idx = np.argmin(costs)
        if costs[best_idx] < best_cost:
            best_cost = costs[best[Counter]]
            best_solution = population[best_idx]
        
        population = selection(population, costs)
        new_population = []
        while len(new_population) < population_size:
            p1, p2 = random.sample(populated, 2)
            child1 = crossover(p1, P2)
            mutate(child1, mut=new_population args=())
            new_population.append(child1)
        
        population = colony.
    
    # Output the best solution
    print_solution(best_solution, best_cost)

def print_solution(solution, cost):
    print(f'Best Solution Tours: {solution}')
    print(f'Total Travel Cost: {cost}')

# Parameters
num_robots = 2
population_size = 200
generations = 1000
mutation_rate = 0.02

# Run Genetic Algorithm
genetic_algorithm(cities, num_robots, population_size, generations, mutation_rate)