import numpy as np
from scipy.spatial import distance_matrix
from geneticalgorithm import geneticalgorithm as ga

# Define cities and coordinates
cities = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
])

# Calculate distance matrix
distances = distance_matrix(cities, cities)

def fitness(sol):
    cost = 0
    routes = decode_chromosome(sol)
    for route in routes:
        for i in range(len(route) - 1):
            cost += distances[int(route[i]), int(route[i+1])]
    return cost

def decode_chromosome(sol):
    sorted_indices = np.argsort(sol)
    cities1 = [0]
    cities2 = [1]
    for index in sorted_indices[2:]:
        if fitness([cities1 + [index]]) < fitness([cities2 + [index]]):
            cities1.append(index)
        else:
            cities2.append(index)
    return [cities1, cities2]

# GA parameters
varbound = np.array([[0,1]]*len(cities))
algorithm_param = {
    'max_num_iteration': 100,
    'population_size': 100,
    'mutation_probability': 0.1,
    'elit_ratio': 0.01,
    'crossover_probability': 0.5,
    'parents_portion': 0.3,
    'crossover_type': 'uniform',
    'max_iteration_without_improv': 100
}

model = ga(function=fitness, dimension=len(cities), variable_type='real', variable_boundaries=varbound, algorithm_parameters=algorithm_param)
model.run()

best_solution = model.output_dict['variable']
routes = decode_chromosome(best_solution)

# Collect output and calculate costs
total_cost = 0
result_output = ""
for index, route in enumerate(routes):
    route_cost = sum(distances[route[i], route[(i+1)%len(route)]] for i in range(len(route)-1))
    total_cost += route_cost
    result_output += f"Robot {index} Tour: {route}\n"
    result_output += f"Robot {index} Total Travel Cost: {route_cost}\n"

result_output += f"Overall Total Travel Cost: {total_cost}\n"
print(result_output)