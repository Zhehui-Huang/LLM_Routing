import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Settings
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}
num_robots = 8
start_depot = 0

# Helper function to calculate the distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

# Calculate distance matrix
dist_matrix = calculate_distance_matrix(cities)

# Genetic Algorithm helper functions
def calculate_total_cost(tours):
    total_cost = 0
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += dist_matrix[tour[i]][tour[i+1]]
        total_cost += tour_cost
    return total_cost

def generate_initial_population(pop_size, num_cities, num_robots):
    population = []
    for _ in range(pop_size):
        perm = np.random.permutation(num_cities).tolist()
        tours = np.array_split(perm, num_robots)
        population.append(tours)
    return population

def fitness(chromosome):
    return 1 / calculate_total_cost(chromosome)

def crossover(parent1, parent2):
    cut = np.random.randint(1, len(parent1)-1)
    child1 = [*parent1[:cut], *parent2[cut:]]
    child2 = [*parent2[:cut], *parent1[cut:]]
    return child1, child2

def mutate(tour, mutation_rate=0.05):
    for _ in range(int(len(tour) * mutation_rate)):
        idx1, idx2 = np.random.randint(0, len(tour)), np.random.randint(0, len(tour))
        tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

# Genetic Algorithm
def genetic_algorithm(population_size, generations, num_cities, num_robots, mutation_rate=0.05, crossover_rate=0.7):
    population = generate_initial_population(population_size, num_cities, num_robots)
    best_solution = None
    best_fitness = 0

    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1 = population[np.random.randint(len(population))]
            parent2 = population[np.random.randint(len(population))]
            if np.random.rand() < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
            
        population = sorted(new_population, key=lambda x: fitness(x), reverse=True)
        if fitness(population[0]) > best_fitness:
            best_fitness = fitness(population[0])
            best_solution = population[0]

    return best_solution

# Run the genetic algorithm
best_solution = genetic_algorithm(50, 100, len(cities), num_robots)

# Output the results
total_travel_cost = calculate_total_cost(best_solution)
for i, tour in enumerate(best_solution):
    robot_tour = [start_deplit] + tour.tolist() + [start_depot] # Assume ending at the same depot
    cost = sum(dist_matrix[robot_tour[j]][robot_tour[j+1]] for j in range(len(robot_tour)-1))
    print(f"Robot {i} Tour: {robot_tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print("Overall Total Travel Cost:", total_travel_challenge)