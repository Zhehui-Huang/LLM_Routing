import random
import math
from copy import deepcopy

# Constants
NUM_CITIES = 22
NUM_ROBOTS = 4
DEPOTS = [0, 1, 2, 3]  # Indices of the depots, matching the corresponding depot cities

# Cities and coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

def initialize_population(size):
    population = []
    for _ in range(size):
        chromosome = random.sample(list(cities.keys()), NUM_CITIES)
        for idx, depot in enumerate(DEPOTS):
            if idx < NUM_ROBOTS:
                chromosome.insert(random.randint(1, len(chromosome) - 1), -depot-1)
        population.append(chromosome)
    return population

def fitness(chromosome):
    total_cost = 0
    current_depot = 0
    i = 0
    while i < len(chromosome):
        if chromosome[i] < 0:
            current_depot = -chromosome[i] - 1
            i += 1
        start_city = cities[DEPOTS[current_depot]]
        if i < len(chromosome) and chromosome[i] >= 0:
            next_city = cities[chromosome[i]]
            total_cost += euclidean_distance(DEPOTS[current_depot], chromosome[i])
            current_position = chromosome[i]
            i += 1
            while i < len(chromosome) and chromosome[i] >= 0:
                total_cost += euclidean_distance(current_position, chromosome[i])
                current_position = chromosome[i]
                i += 1
            total_cost += euclidean_stop(DEPOTS[current_depot], current_position)
    return total_cost

def crossover(parent1, parent2):
    child = deepcopy(parent1)
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child[start:end] = random.sample(parent2[start:end], end - start)
    return child

def mutate(chromosome):
    i1, i2 = random.sample(range(len(chromosome)), 2)
    chromosome[i1], chromosome[i2] = chromosome[i2], chromosome[i1]
    return chromosome

def genetic_algorithm(pop_size, generations):
    population = initialize_population(pop_size)
    for generation in range(generations):
        population = sorted(population, key=fitness)
        new_population = population[:2]  # Elitism: Keep the best two solutions
        while len(new_population) < pop_size:
            if random.random() < 0.7:  # Crossover rate
                p1, p2 = random.sample(population[:10], 2)
                child = crossover(p1, p2)
                new_population.append(child)
            if random.random() < 0.1:  # Mutation rate
                mutant = mutate(random.choice(new_population))
                new_population.append(mutant)
        population = new_population
    return sorted(population, key=fitness)[0]

# Main execution
best_solution = genetic_algorithm(100, 2000)
print("Robot Tours and Costs:")

for i in range(NUM_ROBOTS):
    tour = extract_tour(best_solution, i)
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

total_cost = sum(calculate_tour_cost(extract_tour(best_solution, i)) for i in range(NUM_ROBOTS))
print(f"Overall Total Travel Cost: {total_cost}")