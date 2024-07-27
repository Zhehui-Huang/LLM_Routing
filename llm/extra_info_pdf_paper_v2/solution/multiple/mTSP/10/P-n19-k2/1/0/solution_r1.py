import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates indexed by city number (from 0 to 18)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),  # Cities 0-4
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),  # Cities 5-9
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),  # Cities 10-14
    (61, 33), (62, 63), (63, 69), (45, 35)             # Cities 15-18
]

# Number of robots
num_robots = 2

def calculate_distance(city1, city2):
    return euclidean(coordinates[city1], coordinates[city2])

def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def evaluate_population(population):
    return [sum(calculate_tour_cost(tour) for tour in individual) for individual in population]

def generate_initial_population(pop_size, num_cities):
    population = []
    city_list = list(range(1, num_cities + 1))
    for _ in range(pop_size):
        random.shuffle(city_list)
        mid_point = len(city_list) // num_robots
        tours = [[0] + city_list[i * mid_point: (i + 1) * mid_point] + [0] for i in range(num_robots)]
        population.append(tours)
    return population

def select_parents(population, fitnesses):
    idx = np.argsort(fitnesses)
    return [population[i] for i in idx[:2]]

def crossover(parent1, parent2):
    child1, child2 = [], []
    size = len(parent1[0]) - 2
    cut1, cut2 = random.sample(range(1, size), 2)
    cut_start, cut_end = min(cut1, cut2), max(cut1, cut2)
    
    for idx in range(num_robots):
        temp_tour = [-1] * (size + 2)
        temp_tour[0], temp_tour[-1] = 0, 0
        temp_tour[cut_start+1:cut_end+1] = parent1[idx][cut_start+1:cut_end+1]
        needed = set(parent2[idx][1:-1]) - set(temp_tour)
        placements = [i for i in range(1, size+1) if temp_tour[i] == -1]
        
        for place, city in zip(placements, needed):
            temp_tour[place] = city
        
        child1.append(temp_tour) if idx == 0 else child2.append(temp_tour)

    return [child1, child2]

def mutate(tour, mutation_rate=0.15):
    length = len(tour)
    for _ in range(round(mutation_rate * (length - 2))):
        i, j = random.sample(range(1, length-1), 2)
        tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm(coordinates, generations=100, population_size=50):
    num_cities = len(coordinates) - 1
    population = generate_initial_population(population_size, num_cities)
    
    for generation in range(generations):
        fitnesses = evaluate_population(population)
        parents = select_parents(population, fitnesses)
        
        offspring = []
        for parent1, parent2 in zip(parents, parents[::-1]):
            child1, child2 = crossover(parent1, parent2)
            mutate(child1[0])
            mutate(child1[1])
            mutate(child2[0])
            mutate(child2[1])
            offspring.extend([child1, child2])
        
        population = offspring
        
    best_solution_idx = np.argmin(evaluate_population(population))
    best_solution = population[best_solution_idx]
    tour_costs = [calculate_tour_cost(tour) for tour in best_solution]
    
    return best_solution, tour_costs

# Run Genetic Algorithm
best_solution, tour_costs = genetic_algorithm(coordinates)
overall_cost = sum(tour_costs)

# Output Results
for i, (tour, cost) in enumerate(zip(best_solution, tour_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall']),