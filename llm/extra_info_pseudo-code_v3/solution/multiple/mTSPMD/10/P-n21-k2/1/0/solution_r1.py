import random
import numpy as np
from operator import itemgetter

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_cost(tour, cities):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return cost

def initialize_population(pop_size, total_cities):
    population = []
    base_tour = list(range(2, total_cities))  # start from city 2 as 0 and 1 are depots
    for _ in range(pop_size):
        random_tour = random.sample(base_tour, len(base_tour))
        population.append([0] + random_tour + [0] + [1] + random_tour + [1])  # robot 0 and robot 1 tours
    return population

def crossover(parent1, parent2, crossover_point):
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(tour, mutation_rate):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = int(random.random() * len(tour))
            tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm(cities, pop_size, num_generations, mutation_rate):
    population = initialize_population(pop_size, len(cities))
    best_solution = None
    best_cost = float('inf')
    
    for generation in range(num_generations):
        new_population = []
        scores = []
        
        for indiv in population:
            robot0_tour = indiv[:len(indiv)//2]
            robot1_tour = indiv[len(indiv)//2:]
            cost0 = calculate_cost(robot0_tour, cities)
            cost1 = calculate_cost(robot1_tour, cities)
            total_cost = cost0 + cost1
            scores.append((indiv, total_cost))
        
        scores.sort(key=itemgetter(1))
        if scores[0][1] < best_cost:
            best_cost = scores[0][1]
            best_solution = scores[0][0]
        
        elite = scores[:int(0.1 * len(scores))]
        for elite_indiv in elite:
            new_population.append(elite_indiv[0])

        while len(new_population) < pop_size:
            p1, p2 = random.sample(population, 2)
            crossover_point = random.randint(1, len(cities)-3)
            child = crossover(p1, p2, crossover_point)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    robot0_tour = best_solution[:len(best_solution)//2]
    robot1_tour = best_solution[len(best_solution)//2:]
    robot0_cost = calculate_cost(robot0_tour, cities)
    robot1_cost = calculate_cost(robot1_tour, cities)

    return robot0_tour, robot0_cost, robot1_tour, robot1_cost, best_cost

# Configuration
num_cities = len(cities)
pop_size = 100
num_generations = 500
mutation_rate = 0.05

# Running the genetic algorithm
result = genetic_algorithm(cities, pop_size, num_generations, mutation_rate)
print("Robot 0 Tour:", result[0])
print("Robot 0 Total Travel Cost:", result[1])
print("\nRobot 1 Tour:", result[2])
print("Robot 1 Total Travel Cost:", result[3])

print("\nOverall Total Travel Cost:", result[4])