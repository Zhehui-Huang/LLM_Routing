import numpy asnp
import random
from itertools import permutations

# Configuration and cities setup
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
num_cities = len(cities)
num_robots = 8

# Distance calculation
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Tour cost calculation
def calculate_tour_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Ensure robots start at depot and no returns are necessary
def create_initial_population(pop_size):
    population = []
    other_cities = list(range(1, num_cities))
    
    for _ in range(pop_size):
        random.shuffle(other_cities)
        chromosome = [0] + other_cities + [0]
        population.append(chromosome)
    return population

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, num_cities - 1), 2))
    child = [-1] * num_cities
    middle = parent1[start:end]
    child[start:end] = middle
    fill_items = [item for item in parent2 if item not in middle]
    child = child[:start] + middle + child[end:]
    pos = 0
    for i in range(num_cities):
        if child[i] == -1:
            child[i] = fill_items[pos]
            pos += 1
    return child

def mutation(chromosome):
    i, j = random.sample(range(1, num_cities), 2)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

def genetic_algorithm(max_generations, population_size):
    population = create_initial_population(population_size)
    for generation in range(max_generations):
        population_costs = [(chromosome, calculate_tour_cost(chromosome)) for chromosome in population]
        population_costs.sort(key=lambda x: x[1])
        best_individual = population_costs[0]
        new_population = [best_individual[0]]
        
        while len(new_population) < population_size:
            parent1, parent2 = random.sample([p[0] for p in population_costs[:int(pop_size / 2)]], 2)
            child = crossover(parent1, parent2)
            if random.random() < 0.15: # mutation probability
                child = mutation(child)
            new_population.append(child)
        
        population = new_population
        print(f"Generation {generation + 1}, Best Cost: {best_individual[1]}")
        
    return best_individual

# Perform Genetic Algorithm Optimization
best_solution = genetic_algorithm(100, 50)
best_tour, best_cost = best_solution

# Extract tours for each robot
robot_tours = [best_tour[[x for x in range(num_cities)].index(0):] + [0]]  # since they start at 0 and end at 0
total_costs = [calculate_tour_cost(tour) for tour in robot_tours]

# Output the results
for i, (tour, cost) in enumerate(zip(robot_tours, total_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {sum(total_costs)}")