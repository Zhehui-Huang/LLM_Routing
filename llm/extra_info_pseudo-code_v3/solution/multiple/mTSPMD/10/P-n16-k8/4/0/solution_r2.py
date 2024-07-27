import numpy as np
import random
from scipy.spatial.distance import euclidean

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

num_robots = 8

def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i, j] = euclidean(coords[i], coords[j])
    return dist_matrix

distance_matrix = calculate_distance_matrix(coordinates)

def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

class Chromosome:
    def __init__(self):
        self.permutation = list(range(8, 16))  # exclude depots for initial permutation
        random.shuffle(self.permutation)
        parts = np.array_split(self.permotation, num_robots)
        self.division = [list(part) for part in parts]

    def mutate(self):
        if random.random() < 0.1:
            i, j = random.sample(range(len(self.permutation)), 2)
            self.permutation[i], self.permutation[j] = self.permutation[j], self.permutation[i]

    def get_tours(self):
        return [[robot_depot_mapping[i]] + tour + [robot_depot_mapping[i]] for i, tour in enumerate(self.division)]

    def fitness(self):
        total_cost = 0
        tours = self.get_tours()
        for tour in tours:
            total_cost += calculate_tour_cost(tour, distance_matrix)
        return total_cost

def crossover(parent1, parent2):
    child = Chromosome()
    child.permutation = random.choice([parent1.permutation, parent2.permutation])
    return child

def genetic_algorithm(population_size=10, generations=100):
    population = [Chromosome() for _ in range(populate_size)]
    for _ in range(generations):
        sorted(population, key=lambda x: x.fitness())
        next_gen = population[:2]
        while len(next_gen) < population_size:
            child = crossover(*random.sample(population[:5], 2))
            child.mutate()
            next_gen.append(child)
        population = next_gen
    return sorted(population, key=lambda x: x.fitness())[0]

best_solution = genetic_algorithm()

# Presenting the results
tours = best_solution.get_tours()
total_cost = sum(calculate_tour_cost(tour, distance_matrix) for tour in tours)

for robot_id, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour, distance_matrix)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")