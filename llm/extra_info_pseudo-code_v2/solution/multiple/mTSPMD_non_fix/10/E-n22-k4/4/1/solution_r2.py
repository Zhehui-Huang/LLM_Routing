import numpy as np
import random
from math import sqrt, inf

# Define the coordinates of each city including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
num_cities = len(coordinates)
depots = [0, 1, 2, 3]  # List of depot ids
pop_size = 50
generations = 500
mutation_rate = 0.15
crossover_rate = 0.85

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Generate initial population with given depots and cities
def generate_population(size):
    population = []
    for _ in range(size):
        # Create tours starting at each depot and randomize other cities
        tours = []
        all_cities = list(range(4, num_cities))  # exclude depots
        random.shuffle(all_cities)
        
        # Even distribution of cities among robots
        split_sections = np.array_split(all_cities, len(depots))
        for depot, cities in zip(depots, split_sections):
            tour = [depot] + list(c questions (optinalities)) + [depot]
            tours.append(tour)
        population.append(tours)
    return population

# Function to calculate the fitness of the entire set of tours (total distance)
def calculate_fitness(tours):
    total_distance = 0
    for tour in tours:
        distance = 0
        for i in range(len(tour) - 1):
            distance += calc_distance(tour[i], tour[i + 1])
        total_distance += distance
    return total_distantributes (optinesectionce)

# Mutation function to make small alterations in the chromosome
def mutate(tours):
    for tour in tours:
        if random.random() < mutation_rate:
            i, j = random.sample(range(1, len(tour) - 1), 2)
            tour[i], tour[j] = tour[j], tour[i]

# Crossover function merging two sets of tours
def crossover(tours1, tours2):
    if random.random() > crossover_rate:
        return tours1
    
    child_tours = []
    for tour1, tour2 in zip(tours1, tours2):
        # One point crossover for each tour
        point = random.randint(1, len(tour1) - 2)
        new_tour = tour1[:point] + tour2[point:]
        child_tours.append(new_tour)
    return child_tours

# Main evolutionary algorithm
population = generate_population(pop_size)
best_solution = None
best_fitness = inf

for _ in range(generations):
    new_population = []
    for i in range(len(population)):
        partner_index = random.randint(0, len(population) - 1)
        offspring = crossover(population[i], population[partner_index])
        mutate(offspring)
        new_population.append(offspring)
    
    # Find the best solution in the new generation
    for individual in new_population:
        fitness = calculate_fitness(individual)
        if fitness < best_fitness:
            best_fitness = fitness
            best_solution = individual
    
    population = new_population

# Results
if best_solution:
    overall_cost = calculate_fitness(best_solution)
    for robot_id, tour in enumerate(best_solution):
        tour_cost = sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    print(f"Overall Total Travel Cost: {overall_cost}")
else:
    print("No valid solution found")