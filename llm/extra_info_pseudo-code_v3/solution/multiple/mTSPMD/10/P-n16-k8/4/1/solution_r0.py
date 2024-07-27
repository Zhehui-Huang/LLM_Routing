import random
import numpy as np

### Define cities and coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

### Calculate distances:
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distance_matrix = {}
for i in cities:
    for j in cities:
        distance_matrix[(i, j)] = euclidean_distance(cities[i], cities[j])

### Parameters
num_robots = 8
depots = range(num_robots)

### Genetic Algorithm Components
# Chromosome: permutation of cities and partition of who visits which city
def create_chromosome():
    customer_cities = list(cities.keys())[num_robots:] # excluding depots
    random.shuffle(customer_cities)
    partitions = sorted(random.sample(range(1, len(customer_cities)), num_robots - 1))
    return customer_cities, partitions

def decode_chromosome(chromosome):
    customer_cities, partitions = chromosome
    # Assign the cities to each robot based on partitions
    tours = []
    prev_index = 0
    for index in partitions + [len(customer_cities)]:
        tours.append(customer_cities[prev, index])
        prev = index
    return [[depots[i]] + tour + [depots[i]] for i, tour in enumerate(tours)]

def compute_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[(tour[i], tour[i+1])]
    return cost

def fitness(chromosome):
    tours = decode_chromosome(chromosome)
    total_cost = sum(compute_tour_cost(tour) for tour in tours)
    return -total_cost  # maximizing fitness, hence negative cost

def crossover(parent1, parent2):
    # Implementing a simple Ordered Crossover (OX)
    customer_cities1, partitions1 = parent1
    customer_cities2, partitions2 = parent2

    size = len(customer_cities1)
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    child_cities = [None]*size
    
    child_cities[cxpoint1:cxpoint2] = customer_cities1[cxpoint1:cxpoint2]
    fill_pos = 0
    for city in customer_cities2:
        if city not in child_cities:
            while fill_pos < size and child_cities[fill_pos] is not None:
                fill_pos += 1
            child_cities[fill_pos] = city
    
    return child_cities, sorted(random.sample(range(1, len(customer_cities1)), num_robots - 1))

def mutate(chromosome, mutation_rate=0.02):
    customer_cities, partitions = chromosome
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(customer_cities)), 2)
        customer_cities[idx1], customer_cities[idx2] = customer_cities[idx2], customer_cities[idx1]
    return customer_cities, partitions

### Genetic Algorithm Execution
population_size = 50
generations = 100
mutation_rate = 0.01

population = [create_chromosome() for _ in range(population_size)]
for generation in range(generations):
    population = sorted(population, key=fitness)
    next_generation = population[:2]  # elitism
    while len(next_generation) < population_size:
        parents = random.sample(population[:20], 2)  # tournament selection
        offspring_cities, offspring_partitions = crossover(parents[0], parents[1])
        offspring_cities, offspring_partitions = mutate((offspring_cities, offspring_partitions), mutation_rate)
        next_generation.append((offspring_cities, offspring_partitions))
    population = next_generation

### Evaluate final solution
best_solution = population[0]
decoded_tours = decode_chromosome(best_solution)
tour_costs = [compute_tour_cost(tour) for tour in decoded_tours]
overall_cost = sum(tour_costs)

for idx, tour in enumerate(decoded_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_costs[idx]}")

print(f"\nOverall Total Travel