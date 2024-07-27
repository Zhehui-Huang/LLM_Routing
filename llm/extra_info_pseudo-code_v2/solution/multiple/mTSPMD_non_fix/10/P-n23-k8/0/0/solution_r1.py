import random
from math import sqrt, inf

# Constants
NUM_GENERATIONS = 200
POPULATION_SIZE = 50
mutation_rate = 0.1
crossover_rate = 0.8

# Python functions used in algorithm
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def evaluate_fitness(individual):
    total_distance = 0
    tour = []
    current_distance = 0
    start_city = start_depot
    
    for city in individual:
        if city == -1:
            total_distance += current_distance
            current_distance = 0
            start_city = start_depot
        else:
            current_distance += calc_distance(start_city, city)
            start_city = city
    total_distance += current_distance
    return total_distance

def tournament_selection(population, k=3):
    best = None
    for i in range(k):
        indiv = random.choice(population)
        if best is None or evaluate_fitness(indiv) < evaluate_fitness(best):
            best = indiv
    return best

def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return [parent1[:], parent2[:]]  # Return copies

    size = len(parent1)
    p1, p2 = [parent1[:], parent2[:]]
    cx_point1 = random.randint(0, size - 1)
    cx_point2 = random.randint(cx_point1 + 1, size)

    p1[cx_point1:cx_point2], p2[cx_point1:cx_point2] = p2[cx_point1:cx_point2], p1[cx_point1:cx_point2]
    
    child1 = p1
    child2 = p2
    
    return [child1, child2]

def mutate(individual):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swapWith = int(random.random() * len(individual))
            
            # Simple swap
            individual[swapped], individual[swapWith] = individual[swapWith], individual[swapped]

# Genetic Algorithm Main Framework
population = generate_initial_population(POPULATION_SIZE, num_cities, robots)

for generation in range(NUM_GENERATIONS):
    new_population = []
    for _ in range(int(len(population) / 2)):
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        child1, child2 = crossover(parent1, parent2)
        mutate(child1)
        mutate(child2)
        new_population.extend([child1, child2])
    population = new_population

# Evaluate final solution
best_individual = min(population, key=evaluate_fitness)
fitness = evaluate_fitness(best_individual)

# Output tours for each robot
current_tour = []
tours = []
for gene in best_individual:
    if gene == -1:
        tours.append(current_tour[:])
        current_tour = []
    else:
        current_tour.append(gene)
if current_tour:
    tours.append(current_tour)

# Calculate tour costs
robot_tours_costs = []
total_cost = 0
for tour in tours:
    tour_cost = sum(calc_distance(tour[i - 1], tour[i]) for i in range(1, len(tour)))
    total_cost += tour_cost
    robot_tours_costs.append(tour_cost)

for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: [{start_depot} -> {' -> '.join(map(str, tour))} -> {start_depot}]")
    print(f"Robot {idx} Total Travel Cost: {robot_tours_costs[idx]}")

print(f"Overall Total Travel Cost: {total_cost}")