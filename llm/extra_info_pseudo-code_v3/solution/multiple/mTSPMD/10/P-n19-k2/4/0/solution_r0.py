import random
import numpy as np
from scipy.spatial.distance import euclidean
from heapq import nsmallest

def calculate_distance_matrix(cities):
    size = len(cities)
    distance_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i != j:
                distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

def create_initial_population(cities, num_individuals, num_robots):
    population = []
    for _ in range(num_individuals):
        shuffled_cities = list(range(2, len(cities)))  # cities excluding depots
        random.shuffle(shuffled_cities)
        # divide cities between robots arbitrarily
        split_points = sorted(random.sample(range(1, len(shuffled_cities)), num_robots - 1))
        individual = [shuffled_cities[i:j] for i, j in zip([0]+split_points, split_points+[None])]
        population.append(individual)
    return population

def fitness(individual, depot_indices, distance_matrix):
    total_cost = 0
    tours = []
    for robot, cities in enumerate(individual):
        tour = [depot_indices[robot]] + cities + [depot_indices[robot]]
        tours.append(tour)
        cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        total_cost += cost
    return total_cost, tours

def selection(population, fitness_scores, k=3):
    chosen = random.choices(population, weights=fitness_scores, k=k)
    return min(chosen, key=lambda ind: fitness(ind, [0, 1], distance_matrix))

def crossover(parent1, parent2, crossover_rate=0.8):
    if random.random() < crossover_rate:
        point1, point2 = sorted(random.sample(range(len(parent1[0])), 2))
        child1_segment = parent1[0][point1:point2]
        child1 = [city for city in parent2[0] if city not in child1_segment]
        return [child1[:point1] + child1_segment + child1[point1:]]
    return parent1

def mutation(individual, mutation_rate=0.2):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(individual[0])), 2)
        individual[0][i], individual[0][j] = individual[0][j], individual[0][i]
    return individual

def genetic_algorithm(cities, num_robots, num_generations, population_size):
    depot_indices = [0, 1]
    population = create_initial_population(cities, population_size, num_robots)
    distance_matrix = calculate_distance_matrix(cities)

    for generation in range(num_generations):
        fitness_scores = [fitness(indv, depot_indices, distance_matrix)[0] for indv in population]
        new_population = []
        for _ in range(len(population)):
            parent1 = selection(population, fitness_scores)
            parent2 = selection(population, fitness_scores)
            child = crossover(parent1, parent2)
            mutated_child = mutation(child)
            new_population.append(mutated_child)
        population = new_population

    best_individual = min(population, key=lambda ind: fitness(ind, depot_indices, distance_matrix)[0])
    best_cost, best_tours = fitness(best_next_individual, depot_indices, distance_matrix)
    return best_tours, best_cost

# Cities including depots
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
          (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

best_tours, best_cost = genetic_algorithm(cities, num_robots=2, num_generations=200, population_size=50)

for robot_id, tour in enumerate(best_tours):
    print(f'Robot {robot_id} Tour: {tour}')
    robot_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f'Robot {robot_id} Total Travel Cost: {robot_cost}')

print(f'Overall Total Travel Cost: {best_cost}')