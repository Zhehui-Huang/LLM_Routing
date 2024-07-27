import random
import math

# Function to calculate Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Coordinates of the cities including depots
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Calculate distance matrix
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Genetic Algorithm implementation
population_size = 50
generations = 1000
mutation_rate = 0.1

def create_individual():
    """ Create a random route as a list of city indices. """
    non_depots = list(set(cities.keys()) - {0, 1, 2, 3})
    random.shuffle(non_depots)
    return non_depots

def evaluate(individual, depot):
    """ Evaluate the route starting and ending at specified depot. """
    route = [depot] + individual + [depot]
    cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    return cost, route

# GA operations
def crossover(parent1, parent2):
    """ Crossover between two parent routes. """
    cut1, cut2 = sorted(random.sample(range(len(parent1)), 2))
    child = [None]*len(parent1)
    middle = parent1[cut1:cut2]
    child[cut1:cut2] = middle
    left = [item for item in parent2 if item not in middle]
    child = left[:cut1] + middle + left[cut1:]
    return child

def mutate(individual):
    """ Mutate an individual by swapping two cities. """
    idx1, idx2 = random.sample(range(len(individual)), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Initialize Population
population = [create_individual() for _ in range(population_size)]

# Genetic Algorithm Loop
best_solution = None
best_route = None
best_cost = float('inf')

for generation in range(generations):
    # Evaluate current generation
    scores = []
    for individual in population:
        costs_routes = [evaluate(individual, depot) for depot in range(4)]
        cost, route = min(costs_routes, key=lambda x: x[0])
        scores.append((cost, individual, route))
        if cost < best_cost:
            best_cost, best_solution, best_route = cost, individual, route
    
    # Selection
    scores.sort(key=lambda x: x[0])
    selected = [x[1] for x in scores[:len(popissance)//2]]

    # Next generation
    children = selected[:]
    while len(children) < population_size:
        if random.random() < mutation_rate:
            mutant = random.choice(selected).copy()
            mutate(mutant)
            children.append(mutant)
        else:
            parent1, parent2 = random.sample(selected, 2)
            child = crossover(parent1, parent2)
            children.append(child)

    population = children

# Output the results
cost, tour = evaluate(best_solution, best_route[0])
print(f"Best Tour: {tour}")
print(f"Total Travel Cost: {cost}")