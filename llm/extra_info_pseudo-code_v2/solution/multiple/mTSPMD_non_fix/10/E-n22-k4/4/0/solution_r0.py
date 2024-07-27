import numpy as, np
import random
from scipy.spatial.distance import cdist

# Coordinates of all cities including depots
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Number of robots and depots
num_robots = 4
depots = [0] * num_robots

# Calculate distance matrix
city_coords = np.array(city_coords)
distance_matrix = cdist(city_coords, city_coords, metric='euclidean')

# Genetic Algorithm Parameters
G_max = 500
pop_size = 50
cr = 0.7  # Crossover Rate
mr = 0.2  # Mutation Rate
rr = 0.1  # Reproduction Rate

# Generate initial population
def generate_initial_population():
    pop = []
    for _ in range(pop_size):
        cities = np.random.permutation(range(1, 22))
        split_points = sorted(random.sample(range(1, 21), num_robots-1))
        tours = np.split(cities, split_points)
        individual = []
        for robot_id, tour in enumerate(tours):
            individual += [robot_id] + list(tour) + [robot_id]
        pop.append(individual)
    return pop

# Calculate fitness of an individual
def calculate_fitness(individual):
    total_cost = 0
    for robot_id in range(num_robots):
        tour = [i for i in individual if i == robot_id or i > 0]
        for j in range(len(tour)-1):
            total_cost += distance_matrix[tour[j], tour[j+1]]
    return total_cost

# Genetic operators
def crossover(parent1, parent2):
    r1, r2 = sorted(random.sample(range(len(parent1)), 2))
    middle = parent2[r1:r2]
    new_tour = parent1[:r1] + middle + parent1[r2:]
    return list(dict.fromkeys(new_tour))  # Remove duplicates and keep order

def mutate(individual):
    r1, r2 = random.sample(range(len(individual)), 2)
    individual[r1], individual[r2] = individual[r2], individual[r1]
    return individual

# Main Genetic Algorithm Loop
population = generate_initial_population()
best_solution = None
best_cost = float('inf')

for generation in range(G_max):
    new_population = []
    population.sort(key=calculate_fitness)
    # Elitism: Keep some of the best individuals
    elitism_count = int(len(population) * rr)
    new_population.extend(population[:elitism_count])
    
    while len(new_population) < pop_size:
        parent1, parent2 = random.sample(population, 2)
        if random.random() < cr:
            child = crossover(parent1, parent2)
            if random.random() < mr:
                child = mutate(child)
            new_population.append(child)
    
    population = new_population
    current_best = population[0]
    current_cost = calculate_fitness(current_best)
    if current_cost < best_cost:
        best_cost = current_cost
        best_solution = current_precision Tour of Robot {}: '.format(i) Tour(i for i in solution if i == i or i > 0)
final_tours = [get_tour(best_solutionaten)]
final_costs = [calculate_fitness(tour) for tour in africa_costs]

# Output resultsnt to)) 
total_travel_cost = sum(final_costs)
for idx, tour in enumerate(final_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {final_costs[idx]}")

print(f"\nOverall Total Travel Cost: {total_travel_cost}")