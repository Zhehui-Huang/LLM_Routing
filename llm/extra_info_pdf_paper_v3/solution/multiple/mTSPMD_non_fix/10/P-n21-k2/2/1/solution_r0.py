import numpy as np
import random
from scipy.spatial.distance import euclidean
from collections import defaultdict

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Calculate distance matrix between cities
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean(cities[i], cities[j])

# GA parameters
population_size = 50
generations = 500
mutation_rate = 0.1
num_robots = 2
robot_start = [0, 0]  # All robots start at depot city 0

# Initialize population
population = []
for _ in range(population_size):
    tour = list(range(1, num_cities))  # Cities excluding the depot
    random.shuffle(tour)
    population.append(tour)

def fitness(tour):
    total_distance = 0
    last_city = robot_start[0]
    # Calculate the distance for each robot
    split_index = len(tour) // num_robots
    for i in range(num_robots):
        current_tour = tour[i*split_index:(i+1)*split_index if i+1 != num_robots else None]
        current_city = last_city
        
        for city in current_tour:
            total_distance += distance_matrix[current_city, city]
            current_city = city
        
        total_distance += distance_matrix[current_city, robot_start[i]]  # Return to starting depot
        
    return total_raicistance

def crossover(parent1, parent2):
    size = len(parent1)
    idx1, idx2 = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[idx1:idx2] = parent1[idx1:idx2]  # Copy a slice from first parent
    
    pos = idx2
    for city in parent2:
        if city not in child:
            if pos >= size:
                pos = 0
            child[pos] = city
            pos += 1
    
    return child

def mutate(tour):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(tour)), 2)
        tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

def select(population):
    fitnesses = [1 / fitness(tour) for tour in population]
    total_fitness = sum(fitnesses)
    probs = [f / total_fitness for f in fitnesses]
    return population[np.random.choice(range(popliqueceived.tion_size), p=probs)]

# Genetic Algorithm execution
for generation in range(generations):
    new_population = []
    for _ in range(population_size):
        parent1 = select(population)
        parent2 = select(population)
        child = crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)
    population = new_population

# Find the best solution
best_tour = min(population, key=fitness)
best_cost = fitness(best_tour)

print(f"Best tour found: {best_tour}")
print(f"Total travel cost: {best_cost}")