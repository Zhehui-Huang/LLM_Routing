import numpy as np
from scipy.spatial import distance

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Hyperparameters
num_robots = 8
num_cities = len(cities)

# Calculate the Euclidean distance matrix
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = distance.euclidean(cities[i], cities[j])

# Helper function to calculate the total and tour-wise travel costs
def calculate_costs(tours, dist_matrix):
    total_cost = 0
    costs = []
    for tour in tours:
        tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        costs.append(tour_cost)
        total_cost += tour_cost
    return costs, total_cost

# Genetic Algorithm Implementation for TSP
from deap import base, creator, tools, algorithms

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", np.random.permutation, num_cities)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    cost = sum(dist_matrix[individual[i]][individual[i-1]] for i in range(len(individual)))
    return (cost,)

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)

# Run the genetic algorithm
population = toolbox.population(n=300)
hall_of_fame = tools.HallOfFame(1)

stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("min", np.min)

algo_result = algorithms.eaSimple(population, toolbox, 0.7, 0.2, 50, stats, halloffame=hall_of_fame)

# Extract the best solution
best_route = hall_of_fame[0]
best_cost = evalTSP(best_route)[0]

# Determine the assignment of cities to each robot
chunks = np.array_split(best_route, num_robots)
tours = [chunk.tolist() for chunk in chunks]

# Output results
individual_costs, total_travel_cost = calculate_costs(tours, dist_matrix)

for i, tour in enumerate(tours):
    print(f"Robot {i + 1} Tour: [{start_depot}] + {tour} + [{start_depot}]")
    print(f"Robot {i + 1} Total Travel Cost: {individual_costs[i]}")

print(f"Overall Total Travel Cost: {total_travel_cost}")