import numpy as np
from scipy.spatial.distance import euclidean
import random

# City coordinates (index: coordinates)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}
depots = [0, 1] # Depot indices
num_robots = 2

# Distance matrix
def compute_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i, j] = euclidean(cities[i], cities[j])
            else:
                dist_matrix[i, j] = float('inf')
    return dist_matrix

dist_matrix = compute_distance_matrix(cities)

# Genetic Algorithm settings 
pop_size = 100
generation_limit = 500 
crossover_rate = 0.7
mutation_rate = 0.3
num_cities = len(cities)

# Genetic algorithm functions
def create_initial_population():
    population = []
    for _ in range(pop_size):
        # Create a valid route
        route = list(np.random.permutation(list(range(2, num_cities))))  # start from 2 to avoid depots
        split = np.random.randint(1, len(route)-1)
        # Robot starts from depot 0 and can stop at any city
        robot1 = [0] + route[:split] + [np.random.choice(depots)]
        robot2 = [0] + route[split:] + [np.random.choice(depots)]
        population.append(robot1 + [-1] + robot2 + [-1])
    return np.array(population)

def evaluate_population(population):
    scores = []
    for individual in population:
        tour_indices = np.where(individual == -1)[0]
        cost = 0
        for k in range(len(tour_indices) - 1):
            tour = individual[tour_indices[k]+1:tour_indices[k+1]+1]
            for i in range(len(tour)-1):
                cost += dist_matrix[tour[i], tour[i+1]]
        scores.append(cost)
    return np.array(scores)

def select_parents(scores):
    parents_indices = np.argsort(scores)[:2]  # select top 2
    return parents_indices

def crossover(parent1, parent2):
    # Single point crossover
    point = np.random.randint(1, len(parent1) - 1)
    child1 = np.concatenate([parent1[:point], parent2[point:]])
    child2 = np.concatenate([parent2[:point], parent1[point:]])
    return np.array([child1, child2])

def mutate(individual):
    mutation_idx = np.random.randint(0, len(individual))
    swap_idx = np.random.randint(0, len(individual))
    individual [mutation_idx], individual[swap_idx] = individual[swap_idx], individual[mutation_idx]
    return individual

def genetic_algorithm():
    population = create_initial_population()
    best_solution = None
    best_score = float('inf')

    for generation in range(generation_limit):
        scores = evaluate_population(population)
        best_idx = np.argmin(scores)
        if scores[best_idx] < best_score:
            best_score = scores[best_idx]
            best_solution = population[best_idx]
        
        new_population = []
        while len(new_population) < pop_size:
            parent_indices = select_parents(scores)
            for parent_idx in parent_indices:
                child = np.copy(population[parent_idx])
                if random.random() < mutation_rate:
                    child = mutate(child)
                new_population.append(child)
            if random.random() < crossover_rate:
                children = crossover(population[parent_indices[0]], population[parent_indices[1]])
                new_population.extend(children)
        population = np.array(new_population[:pop_size])
   
    return best_solution, best_score

best_solution, best_score = genetic_algorithm()
print("Best Solution:", best_solution)
print("Best Score:", best_score)

# Parsing best solution into readable format
def parse_solution(solution):
    tours = []
    current_tour = []
    for city in solution:
        if city == -1:
            if current_tour:
                tours.append(current_tour)
                current_tour = []
        else:
            current_tour.append(city)
    if current_tour:
        tours.append(current_tour)
    
    for index, tour in enumerate(tours):
        route_cost = sum([dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1)])
        print(f"Robot {index} Tour: {tour}")
        print(f"Robot {index} Total Travel Cost: {route_cost}")
    print("Overall Total Travel Cost:", best_score)

parse_solution(best_solution)