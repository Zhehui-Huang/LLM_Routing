import numpy as (np)
import random

# Coordinates of cities including depots
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Define distance calculation
def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Building the distance matrix
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i, j] = calculate_distance(cities[i], cities[j])

# Assign robots to their depots
robot_depot = list(range(8))

# Generating initial random tours
def generate_initial_population(size, robot_depot):
    population = []
    for _ in range(size):
        individual = {}
        for depot in robot_depot:
            available_cities = set(range(len(cities))) - set(robot_depot)
            path = [depot] + random.sample(available_cities, 1) + [depot]
            individual[depot] = path
        population.append(individual)
    return population

def fitness(individual):
    total_cost = 0
    for key in individual:
        path = individual[key]
        path_cost = sum(distance_matrix[path[i], path[i+1]] for i in range(len(path) - 1))
        total_cost += path_cost
    return total_cost

def tournament_selection(population, k=2):
    selected = random.sample(population, k)
    selected.sort(key=lambda x: fitness(x))
    return selected[0]

def crossover(ind1, ind2):
    child = {}
    for key in ind1:
        if random.random() < 0.5:
            child[key] = ind1[key].copy()
        else:
            child[key] = ind2[key].copy()
    return child

def mutation(individual, rate=0.1):
    for key in individual:
        if random.random() < rate:
            cities_in_path = individual[key][1:-1]
            random.shuffle(cities_in_path)
            individual[key] = [key] + cities_in_path + [key]

# Genetic Algorithm
def genetic_algorithm(gens, pop_size=50):
    population = generate_initial_population(pop_size, robot_depot)
    best_solution = min(population, key=lambda x: fitness(x))
    best_fitness = fitness(best_solution)

    for _ in range(gens):
        new_population = []
        while len(new_population) < len(population):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = crossover(parent1, parent2)
            mutation(child)
            new_population.append(child)
        
        population = new_population
        current_best = min(population, key=lambda x: fitness(x))
        current_fitness = fitness(current_best)
        if current_fitness < best_fitness:
            best_solution, best_fitness = current_best, current_fitness
    return best_solution, best_fitness

# Running the genetic algorithm
best_solution, best_fitness = genetic_algorithm(100)
for robot, tour in best_solution.items():
    print(f"Robot {robot} Tour: {tour}")
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {robot} Total Travel Cost: {tour_cost:.2f}")
print(f"Overall Total Travel Cost: {best_fitness:.2f}")