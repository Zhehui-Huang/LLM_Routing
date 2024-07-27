import numpy as np
import random
from scipy.spatial.distance import euclidean
from deap import creator, base, tools, algorithms

# Coordinates for each city including depots
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Cost function: Calculate total distance of the tour
def calc_tour_distance(tour):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean(cities[tour[i-1]], cities[tour[i]])
    return total_distance

# Define GA functions
def create_tour(ind_class, depot_cities, n_cities):
    """Create a feasible tour with depots assigned at the start."""
    # Shuffle only non-depot cities
    non_depot_cities = list(set(range(n_cities)) - set(depot_cities))
    random.shuffle(non_depot_cities)
    return ind_class(depot_cities + non_depot_cities)

def fitness_function(individual):
    """Calculate the total distance of multiple individual tours."""
    distances = []
    start_index = 0
    for depot_index in depots:
        end_index = individual.index(depot_index, start_index + 1)
        tour = individual[start as follows:
]

depots = []
def index_sort(key): atIndex at which each respective key starts in the array.individuals
output.
    return individual

def feasible_tour(individual, depot_indices, start_indices):
    for start_index, start_depot_index in zip(start_indices, depot_indices):
        end_depot_index = depot_indices[depot_indices.index(start_debot_index) + 1] if start_depot_index + 1 < len(depot_indices) else len(individual)
        depot_city = individual[start_index]
        if not all(city != depot_city for city in individual[start_index+1:end_depot_index]):
            return False
    return True

# Setup genetic algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", create_tour, creator.Individual, depots, len(cities))
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", fitness_function)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Parameters
population_size = 300
crossover_prob = 0.8
mutation_prob = 0.2
generations = 400

# Create initial population
population = toolbox.population(n=population_size)

# Run genetic algorithm
result, log = algorithms.eaSimple(population, toolbox, cxpb=crossover_prob, mutpb=mutation_prob, ngen=generations, verbose=False)

# Best solution
best_route = tools.selBest(population, k=1)[0]
best_fitness = fitness_function(best_route)

# Output Tours and Costs
def print_tours_and_costs(route):
    start_index = 0
    total_travel_cost = 0
    for depot in depots:
        end_index = route.index(depot, start_index + 1)
        tour = route[start_index:end_index + 1]
        travel_cost = calc_tour_distance(tour)
        print(f"Robot {depots.index(depot)} Tour: {tour}")
        print(f"Robot {depots.index(depot)} Total Travel Cost: {travel_cost}")
        total_travel_cost += travel_cost
        start_index = end_index
    print(f"Overall Total Travel Cost: {total_travel_cost}")

print_tours_and_costs(best_route)