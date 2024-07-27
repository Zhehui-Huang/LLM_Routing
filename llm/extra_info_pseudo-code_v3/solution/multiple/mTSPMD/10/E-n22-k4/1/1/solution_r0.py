import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
city_coords = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Depot assignments and robot IDs
depot_robots = {0: 0, 1: 1, 2: 2, 3: 3}  # depot_id : robot_id

# Calculate distance matrix
def calculate_dist_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

dist_matrix = calculate_dist_matrix([city_coords[i] for i in sorted(city_coords)])

# Genetic Algorithm parameters
number_of_iterations = 1000
population_size = 50
mutation_rate = 0.1
tournament_size = 5
crossover_rate = 0.8

def get_random_solution():
    cities = list(city_coords.keys())
    robots = list(depot_robots.keys())
    random.shuffle(cities)
    return [city for city in cities if city not in robots]  # Removing depots

# Initialize population
def initialize_population():
    return [get_random_solution() for _ in range(population_size)]

# Calculate tour cost
def calculate_tour_cost(tour, depot):
    tour = [depot] + tour + [depot]
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Fitness function
def fitness(individual):
    segments = np.array_split(individual, len(depot_robots))
    total_cost = 0
    for depot, segment in zip(sorted(depot_robots), segments):
        total_cost += calculate_tour_cost(list(segment), depot)
    return total_cost

# Selection via tournament
def tournament_selection(population):
    best = None
    for i in range(tournament_size):
        ind = random.choice(population)
        if best is None or fitness(ind) < fitness(best):
            best = ind
    return best

# Crossover: Ordered Crossover (OX)
def ordered_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end+1] = parent1[start:end+1]
    
    filled_positions = set(range(start, end+1))
    insert_position = (end + 1) % len(parent1)
    
    for gene in parent2:
        if gene not in child:
            child[insert_position] = gene
            insert_position = (insert_position + 1) % len(parent1)
            
    return child

# Mutation: Swap mutation
def mutate(individual):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Genetic Algorithm execution
population = initialize_population()
best_solution = None

for iteration in range(number_of_iterations):
    new_population = []
    while len(new_population) < population_size:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        if random.random() < crossover_rate:
            child = ordered_crossover(parent1, parent2)
        else:
            child = parent1[:]
        child = mutate(child)
        new_population.append(child)
    population = new_population
    current_best = min(population, key=fitness)
    if best_solution is None or fitness(current_best) < fitness(best_solution):
        best_solution = current_best[:]
        
# Compute and print solutions
final_costs = []
chunks = np.array_split(best_solution, len(depot_robots))
for depot, tour_segment in zip(sorted(depot_robots), chunks):
    tour = [depot] + list(tour_segment) + [depot]
    tour_cost = calculate_tour_cost(list(tour_segment), depot)
    final_costs.append(tour_cost)
    print(f"Robot {depot_robots[depot]} Tour: {tour}")
    print(f"Robot {depot_robots[depot]} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {sum(final_costs)}")