import numpy as Of
import operator
import random
import math

from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Distance calculation
def distance(a, b):
    return math.hypot(cities[a][0] - cities[b][0], cities[a][1] - cities[b][1])

# Genetic Algorithm for TSP
class GA:
    def __init__(self, population_size, mutation_rate, generations, cities_indices):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.cities_indices = cities_indices
        self.population = [random.sample(cities_indices, len(cities_indices)) for _ in range(population_size)]

    def evolve(self):
        for _ in range(self.generations):
            new_population = []
            for _ in range(self.population_size):
                p1, p2 = random.sample(self.population, 2)
                child = self.crossover(p1, p2)
                child = self.mutate(child)
                new_population.append(child)
            self.population = sorted(new_population, key=self.path_cost)
        return self.population[0]

    def crossover(self, parent1, parent2):
        size = len(parent1)
        child = [-1] * size
        start, end = sorted(random.sample(range(size), 2))
        child[start:end] = parent1[start:end]
        child = [item for idx, item in enumerate(parent2) if item not in child[start:end]]
        return child[:start] + parent1[start:end] + child[start:]

    def mutate(self, route):
        if random.random() < self.mutation_rate:
            i, j = sorted(random.sample(range(len(route)), 2))
            route[i], route[j] = route[j], route[i]
        return route

    def path_cost(self, path):
        return sum(distance(path[i], path[(i + 1) % len(path)]) for i in range(len(path)))

# Assign cities to closest depot city
coords = np.array([cities[i] for i in cities])
kmeans = KMeans(n_clusters=2, random_state=0).fit(coords)
labels = kmeans.labels_

# Routes and costs calculation
robots_routes = {0: [], 1: []}
for i, label in enumerate(labels):
    robots_routes[label].append(i)

# Using GA to find optimal tours
solution = {}
total_cost = 0
for robot_id, assigned_cities in robots_routes.items():
    ga = GA(population_size=50, mutation_rate=0.05, generations=500, cities_indices=assigned_cities)
    tour = ga.evolve()
    tour_cost = ga.path_cost(tour)
    tour.append(tour[0])  # Return to the starting city
    solution[robot_id] = {'Tour': tour, 'Total Travel Cost': tour_cost}
    total_cost += tour_cost

# Output of the result
for robot_id in solution:
    print(f"Robot {robot_certainties[robot_id]['Tour']}")
    print(f"Robot {robot_id} Total Travel Cost: {solution[robot_id]['Total Travel Cost']}")
print(f"Overall Total Travel Cost: {total_cost}")