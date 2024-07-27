import random
import math
import numpy as np

# City coordinates: each entry corresponds to a city's (x, y) coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initialize population
def init_population(pop_size, cities):
    population = []
    number_of_cities = len(cities)
    all_cities = list(range(1, number_of_cities))  # Starting from 1 since 0 is the depot
    for _ in range(pop_size):
        random.shuffle(all_cities)
        # Insert depots for robots, ensure correct structure
        chromosome = [0] + all_cities[:number_of_cities//2] + [-1] + all_cities[number_of_cities//2:] + [0]
        population.append(chromosome)
    return population

# Tournament selection
def tournament_selection(population):
    fighter1, fighter2 = random.sample(population, 2)
    if evaluate(fighter1) < evaluate(fighter2):
        return fighter1
    else:
        return fighter2

# Crossover
def crossover(parent1, parent2):
    cut1, cut2 = sorted(random.sample(range(1, len(parent1) - 2), 2))
    child = [-1] * len(parent1)
    middle = parent1[cut1:cut2]
    child[cut1:cut2] = middle
    remaining = [city for city in parent2 if city not in middle and city >= 0]
    child = [0] + remaining[:cut1-1] + middle + remaining[cut1-1:] + [0]
    return child

# Mutation
def mutate(chromosome):
    idx1, idx2 = sorted(random.sample(range(1, len(chromosome) - 1), 2))
    chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return chromosome

def evaluate(chromosome):
    cost = 0
    for i in range(1, len(chromosome)):
        if chromosome[i] >= 0:
            cost += distance(cities[chromosome[i-1]], cities[chromosome[i]])
    return cost

def genetic_algorithm(cities):
    population = init_population(pop_size, cities)
    for _ in range(G_max):
        new_population = [tournament_selection(population) for _ in range(int(rr * pop_size))]
        while len(new_population) < pop_size:
            if random.random() < cr:
                parent1 = tournament_selection(population)
                parent2 = tournament_selection(population)
                child1 = crossover(parent1, parent2)
                new_population.append(child1)
            else:
                mutant = mutate(tournament_selection(population))
                new_population.append(mutant)
        population = new_population
    
    best_solution = min(population, key=evaluate)
    tours = parse_tour(best_solution)
    return tours

def parse_tour(chromosome):
    tours = {0: [], 1: []}
    current_robot = 0
    for node in chromosome:
        if node == -1:
            current_robot = 1 if current_robot == 0 else 0 # switch robot on depots
        else:
            tours[current_robot].append(node)
    return tours

# Run the Genetic Algorithm
tours = genetic_algorithm(cities)

for robot_id, tour in tours.items():
    cost = calculate_tour_cost(tour)
    print(f"Robot {robot_id} Tour: {[0]+tour+[0]}")  # Start and end at depot
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")