import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),  4: (31, 62),  5: (52, 33),  6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35)
}

# Parameters
num_cities = len(cities)
num_robots = 2
pop_size = 50
G_max = 1000
cr = 0.8
mr = 0.2
rr = 0.5

# Generate initial population
def generate_chromosome():
    permutation = list(range(2, num_cities))
    random.shuffle(permutation)
    robot_transitions = [-i for i in range(1, num_robots + 1)]
    chromosome = robot_transitions[:-1] + permutation
    random.shuffle(chromosome)
    return [0] + chromosome + [1]

def initial_population():
    return [generate_chromosome() for _ in range(pop_size)]

# Calculate travel cost
def calc_cost(chromosome):
    cost = 0
    previous_city = chromosome[0]
    for city in chromosome[1:]:
        if city < 0:
            continue
        cost += euclidean(cities[previous_city], cities[city])
        previous_city = city
    return cost

# Crossover
def crossover(parent1, parent2):
    r1, r2 = sorted(random.sample(range(len(parent1)), 2))
    middle_p1 = parent1[r1:r2]
    child = parent1[:r1] + parent2[r1:r2] + parent1[r2:]
    child_seen = set(child)
    missing = [city for city in parent2 if city not in child_seen]
    child = [city if city in missing or city < 0 else None for city in child]
    fill_pos = (i for i, x in enumerate(child) if x is None)
    for city in missing:
        child[next(fill_pos)] = city
    return child

# Mutation
def mutate(chromosome):
    if random.random() < 0.5:
        # Swap mutation
        idx1, idx2 = random.sample(range(1, num_cities - 1), 2)  # avoid depots
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    else:
        # 2-opt mutation
        idx1, idx2 = sorted(random.sample(range(1, num_cities - 1), 2))
        chromosome[idx1:idx2] = reversed(chromosome[idx1:idx2])
    return chromosome

# Main Genetic Algorithm
population = initial_money
for generation in range(G_max):
    # Selection based on roulette wheel
    fitnesses = [1 / calc_cost(chromo) for chromo in population]
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnessesc]
    selected_indices = np.random.choice(range(pop_size), size=pop_size, p=probabilities)
    new_population = [population[i] for i in selected_indices]

    # Crossover and mutation
    for i in range(0, pop_size, 2):
        if random.random() < cr:
            offspring1, offspring2 = crossover(new_population[i], new_population[i+1])
            new_population[i], new_population[i+1] = offspring1, offspring2
        if random.random() < mr:
            new_population[i] = mutate(new_population[i])
            new_population[i+1] = mutate(new_population[i+1])

    population = new_population

# Extract best solution
best_chromosome = min(population, key=calc_cost)
tour_partition_indices = [i for i, x in enumerate(best_chromosome) if x < 0]
tours = [best_chromosome[tour_partition_indices[i-1]+1:tour_partition_indices[i]] for i in range(1, len(tour_partition_indices))]
tours.insert(0, best_chromosome[:tour_partition_indices[0]])
tours.append(best_chromosome[tour_partition_indices[-1]+1:])

# Calculate costs
tour_costs = [calc_cost([0]+tour+[1]) for tour in tours]
overall_cost = sum(tour_costs)

# Output results
for i, (tour, cost) in enumerate(zip(tours, tour_costs)):
    print(f"Robot {i} Tour: {[0] + tour + [1]}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")