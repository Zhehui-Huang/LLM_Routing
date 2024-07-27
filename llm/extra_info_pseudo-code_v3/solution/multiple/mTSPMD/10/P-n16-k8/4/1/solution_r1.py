import random
import numpy as np

# Define cities and coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculate distances with Euclidean method
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Precompute distance matrix
distance_matrix = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities}

# Parameters for Genetic Algorithm
num_robots = 8
depots = list(range(num_robots))

# Create a chromosome with random assignment of cities to robots
def create_chromosome():
    city_indices = list(set(cities.keys()) - set(depots))
    random.shuffle(city_indices)
    parts = sorted(random.sample(range(1, len(city_indices)), num_robots - 1))
    return city_indices, parts

def decode_chromosome(chromosome):
    city_list, partitions = chromosome
    customer_division = [city_list[i:j] for i, j in zip([0] + partitions, partitions + [None])]
    robot_tours = [[depot] + part + [depot] for depot, part in zip(depots, customer_division)]
    return robot_tours

def tour_cost(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

def fitness(chromosome):
    tours = decode_chromosome(chromosome)
    return -sum(tour_cost(t) for t in tours)  # Minimize total tour cost

def crossover(parent1, parent2, crossover_point):
    p1, partitions1 = parent1
    p2, partitions2 = parent2
    point = random.choice(range(len(p1)))
    new_p1 = p1[:point] + p2[point:]
    new_p2 = p2[:point] + p1[point:]
    return (new_p1, partitions1), (new_p2, partitions2)

def mutate(chromosome, mutation_rate=0.1):
    p, parts = chromosome
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(p)), 2)
        p[i], p[j] = p[j], p[i]
    return p, parts

# Initialize population
population_size = 50
population = [create_chromosome() for _ in range(population_size)]
generations = 200

# Genetic Algorithm main loop
for _ in range(generations):
    population = sorted(population, key=fitness)
    new_population = population[:2]  # elitism
    while len(new_population) < population_size:
        parent1, parent2 = random.sample(population[:int(0.2 * population_size)], 2)
        child1, child2 = crossover(parent1, parent2, crossover_point=random.randint(1, len(cities)-2))
        new_population.extend([mutate(child1), mutate(child2)])
    population = new_population

# Retrieve best solution
best_solution = population[0]
best_tours = decode_chromosome(best_solution)
total_cost = sum(tour_cost(tour) for tour in best_tours)

# Output Results
for idx, tour in enumerate(best_tours):
    cost = tour_cost(tour)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")