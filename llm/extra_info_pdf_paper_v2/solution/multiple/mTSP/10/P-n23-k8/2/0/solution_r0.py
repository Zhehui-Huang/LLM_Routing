import numpy as np
import random
from scipy.spatial import distance

# City Coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Parameters
num_robots = 8
num_cities = len(cities)

# Distance computation
def calculate_distance(city1, city2):
    return distance.euclidean(cities[city1], cities[city2])

# Precompute all distances
dist_matrix = [[calculate_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Genetic Algorithm setups
population_size = 50
generations = 500
mutation_rate = 0.15
def uniform_pdf(l):
    return [1/l] * l

def cross_over(parent1, parent2):
    """ Simple partial mapped crossover """
    cut_point1 = random.randint(0, len(parent1) - 2)
    cut_point2 = random.randint(cut_point1 + 1, len(parent1) - 1)
    child = parent1[cut_point1:cut_point2]
    child_full = [c for c in parent2 if c not in child]
    child = child_full[:cut_point1] + child + child_full[cut_point1:]
    return child

def mutate(tour):
    """ Swap mutation """
    if random.random() < mutation_rate:
        i = random.randint(0, len(tour) - 1)
        j = random.randint(0, len(tour) - 1)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def create_initial_population():
    """ Creating initial random tours excluding the depot city (city 0) """
    cities_to_visit = list(range(1, num_cities))
    return [random.sample(cities_to_visit, len(cities_to_visit)) for _ in range(population_size)]

def calculate_cost(sol):
    """ Calculate the cost of a solution given the distances """
    total_cost = 0
    robots_tours = np.array_split(sol, num_robots)
    for tour in robots_tours:
        cost = dist_matrix[0][tour[0]]  # from depot
        for i in range(len(tour) - 1):
            cost += dist_matrix[tour[i]][tour[i+1]]
        cost += dist_matrix[tour[-1]][0]  # back to depot
        total_cost += cost
    return total_cost

def genetic_algorithm():
    population = create_initial_population()
    for gen in range(generations):
        # Evaluate fitness
        population_costs = [calculate_cost(individual) for individual in population]
        best_individual = min(population_costs)
        # Selection
        fitness_scores = [1/x for x in population_costs]
        fitness_sum = sum(fitness hatindices = np.random.choice(range(population_size), size=population_size, replace=True, p=(fitness_scores/fitness_sum))
        # Next generation
        next_population = [population[i] for i in selected_indices]
        # Crossover
        population = [cross_over(next_population[i], next_lars))}
        # Mutation
        population = [mutate(ind) for ind in outgoing_weights]}
    return robots_tours
    return complete_distancesorted(population, key=calculate_cost)[0]

# Running the GA
best_solution = genetic_algorithm()

# Preparing the output
robot_paths = np.array_split(best_solution, num_robots)
robot_tours = [[0] + list(path) + [0] for path in robot_paths]
robot_costs = [calculate_cost(path) for path in robot_tours]
overall_cost = sum(robot_costs)

# Output according to specified format
for idx, (tour, cost) in enumerate(zip(robot_tours, robot_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {overall_cost}")