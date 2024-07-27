import random
import numpy as np
from scipy.spatial.distance import euclidean

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
    number_cities = len(cities) - num_robots
    for _ in range(num_individuals):
        # All cities except the depots
        shuffled_cities = random.sample(range(2, len(cities)), number_cities)
        division_points = sorted(random.sample(range(1, number_cities), num_robots-1))
        divided = [shuffled_cities[i:j] for i, j in zip([0]+division_points, division_points+[None])]
        population.append(divided)
    return population

def fitness(individual, depot_indices, distance_matrix):
    total_cost = 0
    tours = []
    for robot_id, cities in enumerate(individual):
        tour = [depot_indices[robot_id]] + cities + [depot_indices[robot_id]]
        tours.append(tour)
        total_cost += sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_cost, tours

def select_parents(population, fitness_scores):
    weights = [1/f for f in fitness_scores]
    parent1, parent2 = random.choices(population, weights=weights, k=2)
    return parent1, parent2

def crossover(parent1, parent2):
    child = []
    for (p1, p2) in zip(parent1, parent2):
        if random.random() > 0.5:
            child.append(p1)
        else:
            child.append(p2)
    return child

def mutation(individual, mutation_rate=0.1):
    for tour in individual:
        if random.random() < mutation_rate:
            i, j = random.sample(range(len(tour)), 2)
            tour[i], tour[j] = tour[j], tour[i]
    return individual

def genetic_algorithm(cities, num_robots, num_generations, population_size):
    depot_indices = [0, 1]
    population = create_initial_population(cities, population_size, num_robots)
    distance_matrix = calculate_distance_matrix(cities)

    for generation in range(num_generations):
        fitnesses = [fitness(ind, depot_indices, distance_matrix)[0] for ind in population]
        new_population = []
        while len(new_population) < len(population):
            parent1, parent2 = select_parents(population, fitnesses)
            child = crossover(parent1, parent2)
            mutated_child = mutation(child)
            new_population.append(mutated_child)
        population = new_population

    best_individual = min(population, key=lambda ind: fitness(ind, depot_indices, distance_matrix)[0])
    best_cost, best_tours = fitness(best_individual, depot_indices, distance_matrix)
    return best_tours, best_cost

cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
          (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

best_tours, total_cost = genetic_algorithm(cities, 2, 500, 50)

for robot_id, tour in enumerate(best_tours):
    print(f"Robot {robot_id} Tour: {tour}")
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")