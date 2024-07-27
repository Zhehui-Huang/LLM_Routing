import numpy as np
import random
import math
from sklearn.cluster import KMeans

# City and Coordinate Data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculating Euclidean Distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Generate Initial Population for Genetic Algorithm
def generate_population(size, chromosome_length):
    return [random.sample(range(chromosome_length), k=chromosome_length) for _ in range(size)]

# Fitness Function
def calculate_fitness(solution):
    return sum(distance(solution[i], solution[i+1]) for i in range(len(solution) - 1))

# Crossover Function
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None]*len(parent1)
    child[start:end] = parent1[start:end]
    index = 0
    for num in parent2:
        if num not in child:
            while child[index] is not None:
                index += 1
            child[index] = num
    return child

# Mutation Function
def mutate(solution, mutation_rate=0.01):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(solution)), 2)
        solution[i], solution[j] = solution[j], solution[i]
    return solution

# Genetic Algorithm
def genetic_algorithm(cities, population_size, generations):
    population = generate_population(population_size, len(cities))
    for _ in range(generations):
        population = sorted(population, key=calculate_fitness)
        next_generation = population[:2]  # Elitism, keep the best solutions
        while len(next_generation) < population_size:
            parents = random.sample(population[:10], 2)  # Tournament selection
            child = crossover(parents[0], parents[1])
            child = mutate(child)
            next_generation.append(child)
        population = next_generation
    best_solution = min(population, key=calculate_fitness)
    return best_solution, calculate_fitness(best_solution)

# Dividing cities based on closest depot
coords = np.array([cities[i] for i in range(len(cities))])
kmeans = KMeans(n_clusters=2).fit(coords)
depots = [0, 1]
robots_routes = {depot: [depot] for depot in depots}

for idx, label in enumerate(kmeans.labels_):
    if idx not in depots:
        robots_routes[depots[label]].append(idx)

total_travel_cost = 0
# Solve TSP for each robot using Genetic Algorithm
for robot_id, itinerary in robots_routes.items():
    tour, tour_cost = genetic_algorithm(itinerary, population_size=50, generations=1000)
    tour.append(tour[0])  # Complete the tour by returning to initial city
    total_travel_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_weights}")

print(f"Overall Total Travel Cost: {total_traffic_cost}")