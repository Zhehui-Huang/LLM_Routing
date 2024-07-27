import numpy as np

# Coordinates of the cities including the depot city
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate distance matrix
def calculate_distances(coordinates):
    num_cities = len(coordinates)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
    return distances

distances = calculate_distances(coordinates)

# Genetic Algorithm components
def calculate_route_length(route, distance_matrix):
    return sum(distance_matrix[route[i], route[i+1]] for i in range(len(route)-1))

def create_initial_population(pop_size, num_cities):
    return [np.random.permutation(range(1, num_cities)).tolist() for _ in range(pop_size)]

def crossover(parent1, parent2):
    cut = np.random.randint(1, len(parent1)-1)
    child = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
    return child

def mutate(route, mutation_rate):
    for i in range(len(route)):
        if np.random.random() < mutation_point:
            swap_with = np.random.randint(0, len(route))
            route[i], route[swap_with] = route[swap_with], route[i]

def genetic_algorithm(population, distance_matrix, num_generations, mutation_rate):
    population_size = len(population)
    
    for _ in range(num_generations):
        new_population = []
        route_lengths = [calculate_route_length([0] + individual + [0], distance_matrix) for individual in population]
        sorted_inds = sorted(range(len(route_lengths)), key=lambda i: route_lengths[i])
        
        best_route_index = sorted_inds[0]
        best_route = [0] + population[best_route_index] + [0]
        best_length = route_lengths[best_index]
        
        for _ in range(population_size):
            parent1, parent2 = np.random.choice([population[i] for i in sorted_inds[:population_size // 2]], 2, replace=False)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        
        population = new_population

    return best_route, best_length

# Parameters
num_cities = len(coordinates)
population_size = 100
num_generations = 250
mutation_rate = 0.02

# Run Genetic Algorithm
initial_population = create_initial_population(population_size, num_cities)
best_route, best_route_length = genetic_algorithm(initial_population, distances, num_generations, mutation_rate)

print("Tour:", best_route)
print("Total travel cost:", best_route_length)