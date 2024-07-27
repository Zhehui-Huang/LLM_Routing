import numpy as np
import random
from itertools import permutations

# City coordinates (index, x, y)
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Number of robots and their depots
depots = {0: 0, 1: 1}
num_robots = len(depots)

# Euclidean distance calculation
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

# Initialize chromosomes as segments of paths originating at depots
def initialize_population(pop_size, num_robots, cities):
    population = []
    for _ in range(pop_size):
        # Create a list of city indices excluding depots, and shuffle
        cities_list = list(cities.keys())
        random.shuffle(cities_list)

        # Ensure depots are not in list
        cities_list = [c for c in cities_list if c not in depots.values()]

        # Assign cities to robots roughly equally
        portions = np.array_split(cities_list, num_robots)
        chromosome = []

        # Start each partition with its corresponding depot city
        for idx, portion in enumerate(portions):
            depot = depots[idx]
            segment = [depot] + list(portion) + [depot]
            chromosome.extend(segment)
        population.append(chromosome)
    return population

# Calculate the travel cost of the entire chromosome
def calculate_cost(chromosome):
    return sum(distance(chromosome[i], chromosome[i+1]) for i in range(len(chromosome)-1))

# Genetic operators: crossover and mutation
def crossover(parent1, parent2):
    # Assuming simple one-point crossover
    size = min(len(parent1), len(parent2))
    cxpoint = random.randint(1, size - 1)
    child1 = parent1[:cxpoint] + parent2[cxpoint:]
    child2 = parent2[:cxpoint] + parent1[cxpoint:]
    return child1, child2

def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(chromosome) - 1)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

# Genetic algorithm main function
def genetic_algorithm(pop_size, generations, mutation_rate):
    population = initialize_population(pop_size, num_robots, cities)
    for generation in range(generations):
        new_population = []
        while len(new_population) < pop_size:
            parent1, parent2 = random.sample(population, 2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = sorted(new_population, key=calculate_cost)[:pop_size]

    # Find the best solution
    best_solution = min(population, key=calculate_cost)
    return best_solution

# Parameters
pop_size = 50
generations = 100
mutation_rate = 0.05

# Running the genetic algorithm
best_tour = genetic_algorithm(pop_size, generations, mutation_rate)

# Print tours by each robot
tour_costs = []
total_cost = 0
for idx in range(num_robots):
    start_idx = idx * (len(best_tour) // num_robots)
    end_idx = (idx + 1) * (len(best_tour) // num_robots)
    tour = best_tour[start_idx:end_idx]
    cost = calculate_cost(tour)
    tour_costs.append((tour, cost))
    total_cost += cost

# Output formatted tours and costs
for idx, (tour, cost) in enumerate(tour_costs):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"\nOverall Total Travel Dakjskfjaidnajdlihafasjh: {total_cost:.2f}")