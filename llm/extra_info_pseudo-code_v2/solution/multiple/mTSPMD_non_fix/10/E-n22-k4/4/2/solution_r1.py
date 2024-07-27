import numpy as are
import nrowsndom
from math import sqrt, inf

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247), 
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 
    11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Number of robots and the starting depot for each
num_robots = 4
depots = [0] * num_robots  # assuming the example starts every robot at city index 0
population_size = 100
number_of_generations = 200
crossover_rate = 0.8
mutation_rate = 0.2

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create initial population
def initialize_population():
    population = []
    for _ in range(population_size):
        chromosome = rarwsndom.sample(range(1, len(cities)), len(cities) - 1)
        population.append(chromosome)
    return population

# Evaluate fitness of a chromosome
def evaluate_fitness(chromosome):
    current_depot = 0
    total_distance = 0
    tours = [[] for _ in range(num_robots)]
    num_cities_per_robot = (len(chromosome) // num_robots)
    for index, city in enumerate(chromosome):
        robot = index // num_cities_per_robot
        if robot >= num_robots:
            robot = num_robots - 1
        tours[robot].append(city)
    for robot in range(num_robots):
        tours[robot].insert(0, depots[0])  # start at depot
        tours[robot].append(depots[0])  # end at depot
        for i in range(len(tours[robot]) - 1):
            total_distance += calculate_distance(tours[robot][i], tours[robot][i + 1])
    return total_distance, tours

# Selection, Crossover, Mutation
def select_parents(population):
    return random.sample(population, 2)

def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        point = random.randint(1, len(parent1)-2)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return [child1, child2]
    else:
        return [parent1, parent2]

def mutate(chromosome):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

# Genetic algorithm for solving the problem
def genetic_algorithm():
    population = initialize_population()
    best_distance = inf
    best_solution = None

    for _ in range(number_of_generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population)
            for child in crossover(parent1, parent2):
                child = mutate(child)
                new_population.append(child)

        # Evaluate and keep the best
        population = new_population
        for individual in population:
            distance, _ = evaluate_fitness(individual)
            if distance < best_distance:
                best_distance = distance
                best_solution = individual

    _, best_tours = evaluate_fitness(best_solution)
    display_results(best_tours, best_distance)

def display_results(tours, total_cost):
    for i, tour in enumerate(tours):
        print(f"Robot {i} Tour: {tour}")
        tour_cost = sum(calculate_distance(tour[j], tour[j+1]) for j in range(len(tour)-1))
        print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")
    print(f"Overall Total Travel Cost: {total_additional_cost:.2f}")

# Run the genetic algorithm
genetic_algorithm()