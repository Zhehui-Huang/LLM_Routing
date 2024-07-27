import numpy as np
import random
from scipy.spatial.distance import euclidean

# Coordinates of cities, indexed from 0 to 15
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64),
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of cities and robots
num_cities = len(coords)
num_robots = 8

# Create distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean(coords[i], coords[j])

# Initial population setup
population_size = 50
chromosome_length = num_cities + num_robots  # One depot per robot

def initialize_population():
    population = []
    for _ in range(population_size):
        # Create a sequence of city indices
        tour = list(range(1, num_cities))
        random.shuffle(tour)
        separators = sorted(random.sample(range(1, num_cities-1), num_robots-1))
        tour = [0] + tour  # Start from depot 0
        for sep in separators:
            tour.insert(sep, 0)  # Insert depots
        population.append(tour)
    return population

population = initialize_population()

# Genetic algorithm parameters
generations = 500
mutation_rate = 0.05

# Evaluate population
def evaluate_cost(chromosome):
    cost = 0
    for i in range(1, len(chromosome)):
        cost += distance_matrix[chromosome[i-1], chromosome[i]]
    return cost

# GA operations
def crossover(parent1, parent2):
    # Two-point crossover
    pt1, pt2 = sorted(random.sample(range(1, len(parent1)-1), 2))
    child = parent1[:pt1] + parent2[pt1:pt2] + parent1[pt2:]
    return child

def mutate(chromosome):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(1, len(chromosome)-1), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return chromosome

# Main genetic algorithm
best_solution = None
best_cost = float('inf')

for _ in range(generations):
    new_population = []
    for i in range(population_size):
        if random.random() < 0.7:  # Crossover probability
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
        else:
            child = random.choice(population).copy()
        child = mutate(child)
        new_population.append(child)
    
    # Selection based on the cost
    population = sorted(new_population, key=evaluate_cost)[:population_size]
    current_best = population[0]
    current_cost = evaluate_cost(current_best)
    
    if current_cost < best_cost:
        best_cost = current_cost
        best_solution = current_best

# Printing results
def print_solution(solution):
    tour_cost = 0
    tours = []
    current_tour = []
    
    for city in solution:
        if city == 0 and current_tour:
            cost = evaluate_cost(current_tour)
            tour_cost += cost
            tours.append((current_tour.copy(), cost))
            current_tour = [0]
        current_tour.append(city)
    
    if current_tour:
        cost = evaluate_cost(current_tour)
        tour_cost += cost
        tours.append((current_tour, cost))
    
    overall_cost = 0
    for idx, (tour, cost) in enumerate(tours):
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {cost:.2f}")
        overall_cost += cost
    
    print(f"Overall Total Travel Cost: {overall_cost:.2f}")

print_solution(best_solution)