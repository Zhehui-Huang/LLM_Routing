import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
import random
import copy

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculate distance matrix
city_coords = np.array(list(cities.values()))
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(city_coords)):
    for j in range(len(city_coords)):
        distance_matrix[i][j] = euclidean(city_coords[i], city_coords[j])

# K-means to allocate cities to depots
kmeans = KMeans(n_clusters=8).fit(city_coords)
labels = kmeans.labels_

cities_by_robot = {i: [i] for i in range(8)}  # each robot starts with its depot
for city, label in enumerate(labels):
    if city >= 8:
        cities_by_robot[label].append(city)

def calculate_total_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance_matrix[tour[i-1]][tour[i]]
    return cost

# Basic genetic algorithm setup
def genetic_algorithm(cities, population_size=100, generations=1000, mutation_rate=0.01):
    def create_individual(cities):
        route = cities[1:]  # exclude depot initially
        random.shuffle(route)
        route = [cities[0]] + route + [cities[0]] # depot at start and end
        return route
    
    def crossover(parent1, parent2):
        start, end = sorted(random.sample(range(1, len(parent1)-1), 2))
        child = [None]*len(parent1)
        child[start:end+1] = parent1[start:end+1]
        pointer = 1
        for i in range(1, len(parent2)-1):
            if not parent2[i] in child:
                while child[pointer] is not None:
                    pointer += 1
                child[pointer] = parent2[i]
        child[0] = parent1[0]
        child[-1] = parent1[0]
        return child

    def mutate(individual):
        i1, i2 = sorted(random.sample(range(1, len(individual)-1), 2))
        individual[i1], individual[i2] = individual[i2], individual[i1]

    def fitness(individual):
        return -calculate_total_cost(individual)

    population = [create_individual(cities) for _ in range(population_size)]
    for generation in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        new_population = population[:2]  # elitism: top 2 always survive
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population[:50], 2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                mutate(child)
            new_population.append(child)
        population = new_population
    best_solution = sorted(population, key=fitness, reverse=True)[0]
    return best_solution

# Apply genetic algorithm for each robot
tours = {}
total_costs = {}

for robot, cities in cities_by_robot.items():
    tour = genetic_algorithm(cities, population_size=100, generations=500)
    tours[robot] = tour
    total_costs[robot] = calculate_total_cost(tour)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]}")

overall_cost = sum(total_costs.values())
print(f"Overall Total Travel Cost: {overall_cost}")