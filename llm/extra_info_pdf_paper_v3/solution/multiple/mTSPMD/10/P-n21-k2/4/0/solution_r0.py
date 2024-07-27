import random
import numpy as np

# City coordinates as given
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Compute Euclidean distance
def dist(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + 
                   (coordinates[city1][1] - coordinates[city2][1])**2)

# Fitness evaluation
def fitness(tours):
    total_cost = 0
    for tour in tours:
        tour_cost = sum(dist(tour[i], tour[i+1]) for i in range(len(tour)-1))
        total_cost += tour_cost
    return total_cost

# Genetic algorithm parameters
population_size = 50
generations = 300
mutation_rate = 0.1

# Create initial population
def create_individual():
    cities = list(range(2, 21))  # all cities except depots
    random.shuffle(cities)
    split = random.randint(1, len(cities) - 1)
    return [cities[:split], cities[split:]]

# Tournament selection
def tournament_selection(population, scores, k=3):
    selection_ix = np.random.randint(len(population))
    for ix in np.random.randint(0, len(population), k-1):
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    return population[selection_ix]

# Order Crossover
def ordered_crossover(parent1, parent2):
    cut1, cut2 = sorted(random.sample(range(1, 19), 2))
    child1_mid = parent1[cut1:cut2]
    child1 = [city for city in parent2 if city not in child1_mid]
    child1 = child1[:cut1] + child1_mid + child1[cut1:]
    child2_mid = parent2[cut1:cut2]
    child2 = [city for city in parent1 if city not in child2_mid]
    child2 = child2[:cut1] + child2_mid + child2[cut1:]
    return child1, child2

# Mutation
def mutate(individual):
    if random.random() < mutation_rate:
        i, j = random.sample(range(19), 2)
        individual[i], individual[j] = individual[j], individual[i]

# Genetic algorithm main loop
population = [create_individual() for _ in range(population_size)]
best_score = float('inf')
best_solution = None

for generation in range(generations):
    # Evaluate all individuals
    scores = [fitness([[0] + ind[0] + [0], [1] + ind[1] + [1]]) for ind in population]
    for i in range(len(population)):
        if scores[i] < best_score:
            best_score = scores[i]
            best_solution = population[i]
    
    # Select parents
    selected = [tournament_selection(population, scores) for _ in range(population_size)]
    
    # Create next generation
    children = []
    for i in range(0, population_size, 2):
        parent1, parent2 = selected[i], selected[i+1]
        for child in ordered_crossover(parent1.copy(), parent2.copy()):
            mutate(child)
            children.append(child)
    population = children

# Output best solution
robot0_tour = [0] + best_solution[0] + [0]
robot1_tour = [1] + best_solution[1] + [1]
robot0_cost = fitness([robot0_tour])
robot1_cost = fitness([robot1_tour])
overall_cost = robot0_cost + robot1_cost

# Output results
print("Robot 0 Tour:", robot0_tour)
print("Robot 0 Total Travel Cost:", round(robot0_cost, 2))
print("Robot 1 Tour:", robot1_tour)
print("Robot 1 Total Travel Cost:", round(robot1_cost, 2))
print("Overall Total Travel Cost:", round(overall_cost, 2))