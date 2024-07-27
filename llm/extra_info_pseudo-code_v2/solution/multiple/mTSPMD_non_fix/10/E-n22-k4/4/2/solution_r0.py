import numpy as np
import random
from math import sqrt

# Define city coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247), 
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 
    11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Parameters
num_robots = 4
depots = [0] * num_robots  # All robots start from city 0
population_size = 100
number_of_generations = 500
crossover_rate = 0.7
mutation_rate = 0.2

# Euclidean distance calculation
def calculate_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initialize the first population
def initialize_population():
    population = []
    for _ in range(population_size):
        perm = list(range(1, len(cities)))
        random.shuffle(perm)
        split_points = sorted(random.sample(range(1, len(perm)), num_robots - 1))
        chromosome = []
        start = 0
        for split_point in split_points:
            chromosome.extend(perm[start:split_point])
            chromosome.append(-999)  # Special marker for depot change
            start = split_point
        chromosome.extend(perm[start:])
        population.append(chromosome)
    return population

# Fitness evaluation
def evaluate_fitness(chromosome):
    total_cost = 0
    tours = []
    current_tour = [depots[0]]
    for gene in chromosome:
        if gene == -999:
            current_tour.append(depots[0])
            tours.append(current_tour)
            current_tour = [depots[0]]
        else:
            current_tour.append(gene)
    current_tour.append(depots[0])
    tours.append(current_tour)

    cost_per_tour = []
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(tour[i], tour[i + 1])
        cost_per_tour.append(tour_cost)
        total_cost += tour_cost
    return total_cost, tours, cost_per_tour

# Selection (tournament)
def tournament_selection(population):
    best = None
    for _ in range(2):  # Binary tournament
        ind = random.choice(population)
        if (best is None) or (evaluate_fitness(ind)[0] < evaluate_fitness(best)[0]):
            best = ind
    return best

# Crossover
def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return parent1, parent2
    size = min(len(parent1), len(parent2))
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    temp1 = parent1[:cxpoint1] + parent2[cxpoint1:cxpoint2] + parent1[cxpoint2:]
    temp2 = parent2[:cxpoint1] + parent1[cxpoint1:cxpoint2] + parent2[cxpoint2:]
    # Ensure all cities exist in offspring and handle depots
    def repair(temp):
        fixed = []
        seen = set()
        for gene in temp:
            if gene not in seen or gene == -999:
                fixed.append(gene)
                seen.add(gene)
            elif gene != -999:
                options = set(range(1, len(cities))) - seen
                fixed.append(random.choice(list(options)))
                seen.update(options)
        return fixed
    child1, child2 = repair(temp1), repair(temp2)
    return child1, child2

# Mutation
def mutate(chromosome):
    if random.random() > mutation_rate:
        return chromosome
    index1, index2 = random.sample(range(len(chromosome)), 2)
    chromosome[index1], chromosome[index2] = chromosome[index2], chromosome[index1]
    return chromosome

# Genetic algorithm execution
def genetic_algorithm():
    population = initialize_population()
    best_solution = None

    for generation in range(number_of_generations):
        new_population = []
        while len(new_population) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.append(child1)
            new_population.append(child2)

        # Elitism: always carry the best found so far
        population = new_population[:population_size]
        best_in_pop = min(population, key=lambda c: evaluate_fitness(c)[0])
        if best_solution is None or evaluate_fitness(best_in_pop)[0] < evaluate_fitness(best_solution)[0]:
            best_solution = best_in_pop

    total_cost, tours, cost_per_tour = evaluate_fitness(best_solution)
    output_result(tours, cost_per_tour, total_cost)

def output_result(tours, cost_per_tour, total_cost):
    for i, (tour, cost) in enumerate(zip(tours, cost_per_tour)):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost:.2f}")
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

# Call the genetic algorithm function to solve the problem
genetic_algorithm()