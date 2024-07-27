import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates and depots indexing:
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

depots = [0, 1, 2, 3]

# Genetic Algorithm Parameters:
pop_size = 50
generations = 100
mutation_rate = 0.1
num_robots = len(depots)

def initialize_population():
    population = []
    non_depot_cities = [city for city in cities if city not in depots]
    for _ in range(pop_size):
        np.random.shuffle(non_depot_cities)
        segments = np.array_split(non_depot_cities, num_robots)
        population.append(list(segments))
    return population

def calculate_total_distance(tour):
    total_distance = 0
    previous_city = tour[0]
    for city in tour[1:]:
        total_distance += euclidean(cities[previous_city], cities[city])
        previous_city = city
    # Close the tour by returning to the depot
    total_distance += euclidean(cities[tour[-1]], cities[tour[0]])
    return total_distance

def fitness(population):
    fitness_scores = []
    for chromosome in population:
        total_cost = 0
        for i, tour in enumerate(chromosome):
            tour = [depots[i]] + tour + [depots[i]]
            total_cost += calculate_total_distance(tour)
        fitness_scores.append(total_cost)
    return fitness_scores

def select_parents(population, fitness_scores):
    fit_idx = np.argsort(fitness_scores)
    selected = np.array(population)[fit_idx[:len(fit_idx)//2]].tolist()
    return selected

def crossover(parent1, parent2):
    child = []
    cut = np.random.randint(1, len(parent1))
    for i in range(num_robots):
        if i % 2 == 0:
            child.append(parent1[i][:cut] + parent2[i][cut:])
        else:
            child.append(parent2[i][:cut] + parent1[i][cut:])
    return child

def mutate(chromosome):
    for tour in chromosome:
        if np.random.rand() < mutation_rate:
            i, j = np.random.choice(range(len(tour)), 2, replace=False)
            tour[i], tour[j] = tour[j], tour[i]
    return chromosome

# Initialize population:
population = initialize_population()

for _ in range(generations):
    fitness_scores = fitness(population)
    selected = select_parents(population, fitness_scores)
    next_generation = []
    
    while len(next_generation) < pop_size:
        parent1, parent2 = np.random.choice(selected, 2, replace=False)
        child = crossover(parent1, parent2)
        child = mutate(child)
        next_generation.append(child)
    population = next_generation

# Get the best solution:
best_solution = min(population, key=lambda x: sum([calculate_total_distance([depots[i]] + tour + [depots[i]]) for i, tour in enumerate(x)]))

# Outputting the solution:
total_cost = 0
for i, tour in enumerate(best_solution):
    robot_tour = [depots[i]] + tour + [depots[i]]
    cost = calculate_total_distance(robot_tour)
    total_cost += cost
    print(f'Robot {i} Tour: {robot_tour}')
    print(f'Robot {i} Total Travel Cost: {cost}')

print(f'Overall Total Travel Cost: {total_cost}')