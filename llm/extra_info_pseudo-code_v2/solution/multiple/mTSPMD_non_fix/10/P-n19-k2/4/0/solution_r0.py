import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the cities coordinates including the depots
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Parameters
num_generations = 100
population_size = 50
mutation_rate = 0.1
crossover_rate = 0.8

# Calculate euclidean distances matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = euclidean(cities[i], cities[j])
        else:
            distance_matrix[i, j] = float('inf')

# Genetic Algorithm Functions

def create_individual():
    """ Creates a random route as an individual. """
    route = list(range(1, num_cities))  # Exclude depot 0 and depot 1
    random.shuffle(route)
    return [0] + route  # Start at depot 0

def calculate_fitness(individual):
    """ Calculate total distance of the route. """
    total_cost = 0
    depot_1_inserted = False
    route = individual.copy()
    
    # Insert depot 1 randomly except at the start
    insert_pos = random.randint(1, len(route))
    route.insert(insert_pos, 1)
    depot_1_inserted = True
    
    for i in range(len(route) - 1):
        total_cost += distance_matrix[route[i]][route[i + 1]]
    
    return total_cost

def crossover(parent1, parent2):
    """ Perform Ordered Crossover between two parents. """
    if random.random() < crossover_rate:
        start, end = sorted(random.sample(range(1, len(parent1)), 2))
        child = [None] * len(parent1)
        child[start:end] = parent1[start:end]

        # Fill the child with the elements from the second parent
        fill_pos = end
        for city in parent2:
            if city not in child:
                if fill_pos < len(child):
                    child[fill_pos] = city
                    fill_pos += 1
                else:
                    fill_pos = 1
                    child[fill_pos] = city
                    fill_pos += 1
    else:
        child = parent1
    
    return child

def mutate(individual):
    """ Swap two cities in the route. """
    index1, index2 = sorted(random.sample(range(1, len(individual)), 2))  # Exclude depot in mutation
    individual[index1], individual[index2] = individual[index2], individual[index1]

# Initialize population
population = [create_individual() for _ in range(population_size)]

# Run genetic algorithm
for generation in range(num_generations):
    # Evaluate fitness
    fitness_scores = [calculate_fitness(ind) for ind in population]
    
    # Select the fittest individuals for reproduction
    sorted_pop = [x for _, x in sorted(zip(fitness_scores, population))]
    parents = sorted_pop[:int(0.5*len(sorted_pop))]  # Assume 50% elitism
    
    # Crossover and mutate to create new population
    new_population = parents.copy()
    while len(new_population) < population_size:
        parent1, parent_stride = random.choice(parents), random.choice(parents)
        child = crossover(parent1, parent_stride)
        if random.random() < mutation_rate:
            mutate(child)
        new_population.append(child)
    
    population = new_population.copy()

# Get the best solution
best_route = population[np.argmin([calculate_fitness(ind) for ind in population])]
best_cost = calculate_fitness(best_route)

# Output the best route format and costs
print("Robot 0 Tour: [{}]".format(', '.join(map(str, [0] + best_route + [1]))))  # From depot 0 to 1
print(f"Robot 0 Total Travel Cost: {best_cost}")

# In this simple model, Robot 1 does not exist due to the stated problem constraints.