import numpy as np
import random
from scipy.spatial import distance

# Cities and their coordinates
coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Distance matrix using Euclidean formula
def create_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = distance.euclidean(coords[i], coords[j])
    return dist_matrix

dist_matrix = create_distance_matrix(coords)

# Genetic Algorithm Settings
num_robots = 8
population_size = 50
max_generations = 300
mutation_rate = 0.15
crossover_rate = 0.85

# Helper functions
def calculate_cost(tour):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def create_initial_population():
    population = []
    cities = list(coords.keys())[1:]  # Assuming depot 0 is starting point
    for _ in range(population_size):
        random.shuffle(cities)
        split_points = sorted(random.sample(range(1, len(cities)), num_robots - 1))
        tours = [cities[i:j] for i, j in zip([0]+split_points, split_points+[None])]
        population.append([[0] + tour + [0] for tour in tours])  # End at depot for simplicity
    return population

def breed(parent1, parent2):
    child1, child2 = [], []
    for tour1, tour2 in zip(parent1, parent2):
        if random.random() < crossover_rate:
            crossover_point = random.randint(1, len(tour1) - 2)
            new_tour1 = tour1[:crossover_point] + tour2[crossover_point:]
            new_tour2 = tour2[:crossover_point] + tour1[crossover_point:]
            child1.append(new_tour1)
            child2.append(new_tour2)
        else:
            child1.append(tour1)
            child2.append(tour2)
    return child1, child2

def mutate(tour):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            a, b = random.sample(range(1, len(tour[i]) - 1), 2)
            tour[i][a], tour[i][b] = tour[i][b], tour[i][a]
    return tour

# Genetic Algorithm Execution
population = create_initial_population()
best_solution = None
best_cost = float('inf')

for _ in range(max_generations):
    new_population = []
    costs = []
    for i in range(0, population_size, 2):
        parent1, parent2 = population[i], population[i + 1]
        child1, child2 = breed(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        new_population.extend([child1, child2])
        costs.extend([calculate_cost(sum(child1, [])), calculate_cost(sum(child2, []))])
    
    # Selection based on cost
    sorted_pop = [pop for _, pop in sorted(zip(costs, new_population), key=lambda x: x[0])]
    population = sorted_pop[:population_size]
    current_best = population[0]
    current_cost = min(costs)
    
    if current_cost < best_cost:
        best_solution = current_best
        best_cost = current_cost

# Output results
overall_cost = 0
for idx, tour in enumerate(best_solution):
    tour_cost = calculate_cost(tour)
    overall_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")