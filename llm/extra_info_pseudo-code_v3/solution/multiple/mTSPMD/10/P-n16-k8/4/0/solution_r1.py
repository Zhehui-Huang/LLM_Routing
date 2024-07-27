import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates, including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Number of robots (Salesmen), and their respective depots
num_robots = 8
robot_depot_mapping = list(range(num_robots))  # robots start at first 8 depots

# Euclidean distance calculator
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i, j] = euclidean(coords[i], coords[j])
    return dist_matrix

distance_matrix = calculate_distance_matrix(coordinates)

# Helper function to calculate the cost of any given tour
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Genetic algorithm components
class Chromosome:
    def __init__(self):
        self.permutation = list(range(8, 16))  # cities excluding depots
        random.shuffle(self.permutation)
        slice_points = sorted(random.sample(range(1, len(self.permutation)), num_robots - 1))
        self.division = [self.permutation[i:j] for i, j in zip([0] + slice_points, slice_points + [None])]
    
    def mutate(self):
        if random.random() < 0.1:  # mutation chance
            idx1, idx2 = random.sample(range(len(self.permutation)), 2)
            self.permutation[idx1], self.permutation[idx2] = self.permutation[idx2], self.permutation[idx1]

    def get_tours(self):
        tours = []
        for depot, cities in zip(robot_depot_mapping, self.division):
            tour = [depot] + cities + [depot]
            tours.append(tour)
        return tours

    def fitness(self):
        return sum(calculate_tour_cost(tour, distance_matrix) for tour in self.get_tours())

def crossover(parent1, parent2):
    child = Chromosome()
    child.permutation = list(parent1.permutation)
    for i in range(len(child.permutation)):
        if random.random() < 0.5:
            child.permutation[i] = parent2.permutation[i]
    return child

def genetic_algorithm(population_size=10, generations=100):
    population = [Chromosome() for _ in range(population_size)]
    for _ in range(generations):
        population.sort(key=lambda x: x.fitness())
        next_generation = population[:2]  # elitism: carry forward top 2
        while len(next_generation) < population_size:
            parents = random.sample(population[:5], 2)  # tournament selection among top 5
            child = crossover(parents[0], parents[1])
            child.mutate()
            next_generation.append(child)
        population = next_generation
    best_solution = sorted(population, key=lambda x: x.fitness())[0]
    return best_solution

# Run genetic algorithm
best_solution = genetic_algorithm()
tours = best_solution.get_tours()
total_cost = sum(calculate_tour_cost(tour, distance_system) for tour in tours)

# Output the results
for idx, tour in enumerate(tours):
    cost = calculate_tour_cost(tour, distance_system)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
print("Overall Total Travel Cost:", total_cost)