import numpy as np
import random

# City coordinates, including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.linalg.norm(np.array(coordinates[city1]) - np.array(coordinates[city2]))

# Genetic Algorithm Parameters
num_generations = 200
population_size = 50
mutation_rate = 0.1
crossover_rate = 0.85
num_robots = 2
depots = [0, 1]  # Depots for the robots

# Initialize cities excluding depots
cities = list(range(len(coordinates)))
for depot in depots:
    cities.remove(depot)

# Generate a valid initial population
def generate_initial_population(pop_size, cities, num_robots):
    population = []
    for _ in range(pop_size):
        remaining_cities = cities[:]
        random.shuffle(remaining_cities)
        splits = sorted(random.sample(range(1, len(remaining_cities)), num_robots-1))
        individual = []
        start = 0
        for i in range(num_robots):
            end = splits[i] if i < len(splits) else len(remaining_cities)
            individual.append([depots[0]] + remaining_cities[start:end] + [depots[0]])
            start = end
        population.append(individual)
    return population

# Calculate total travel cost for the tours of a solution
def calculate_total_cost(solution):
    total_cost = 0
    for tour in solution:
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Select parents for crossover
def select_parents(population, fitness):
    # Roulette wheel selection
    max_fitness = sum(fitness)
    pick = random.uniform(0, max_fitness)
    current = 0
    for i, individual in enumerate(population):
        current += fitness[i]
        if current > pick:
            return individual

def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return [parent1, parent2]
    cut1, cut2 = sorted(random.sample(range(1, len(parent1[0]) - 1), 2))
    child1 = [parent1[0][:cut1] + parent2[0][cut1:cut2] + parent1[0][cut2:]]
    child2 = [parent2[0][:cut1] + parent1[0][cut1:cut2] + parent2[0][cut2:]]
    return [child1, child2]

# Mutate a solution by swapping two cities
def mutate(tour):
    if random.random() < mutation_rate:
        i, j = random.randint(1, len(tour[0]) - 2), random.randint(1, len(tour[0]) - 2)
        tour[0][i], tour[0][j] = tour[0][j], tour[0][i]
    return tour

# Genetic Algorithm to find the best solution
def genetic_algorithm():
    population = generate_initial_population(population_size, cities, num_robots)
    best_cost = float('inf')
    best_solution = None

    for generation in range(num_generations):
        fitness = [calculate_total_cost(individual) for individual in population]
        sorted_individuals = sorted(zip(fitness, population), key=lambda x: x[0])
        best_current = sorted_individuals[0]
        if best_current[0] < best_cost:
            best_cost = best_current[0]
            best_solution = best_current[1]

        new_population = [individual for _, individual in sorted_individuals[:len(population)//2]]
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(new_population, fitness), select_parents(new_population, fitness)
            for child in crossover(parent1, parent2):
                new_population.append(mutate(child))

        population = new_population[:population_size]

    return best_solution, best_cost

# Run the genetic algorithm and print the optimal tours and costs
final_solution, final_cost = genetic_algorithm()
print("Optimal Tours and Costs:")
for idx, robot_tour in enumerate(final_solution):
    print(f"Robot {idx + 1} Tour: {robot_tour}")
    robot_tour_cost = calculate_total_cost([robot_tour])
    print(f"Robot {idx + 1} Total Travel Cost: {robot_tour_cost}")
print(f"Overall Total Travel Cost: {final_cost}")