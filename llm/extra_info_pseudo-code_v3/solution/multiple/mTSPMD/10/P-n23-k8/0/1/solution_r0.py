import numpy as np
import random
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define city coordinates, including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Identifying depots
depots = list(range(8))

# Robot start and end cities are the same and map to depot indices directly
robots = depots

# Euclidean distance matrix
def distance_matrix(coords):
    num_cities = len(coords)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = euclidean(coords[i], coords[j])
    return matrix

dist_matrix = distance_matrix(coordinates)

# Genetic Algorithm components
class Chromosome:
    def __init__(self, tour):
        self.tour = tour
        self.total_cost = self.calculate_cost()
    
    def calculate_cost(self):
        cost = 0
        for i in range(len(self.tour) - 1):
            cost += dist_matrix[self.tour[i], self.tour[i+1]]
        return cost

def initialize_population(size, num_cities, depots, num_robots):
    population = []
    for _ in range(size):
        cities = list(set(range(num_cities)) - set(depots))
        random.shuffle(cities)
        partition_sizes = [len(cities) // num_robots] * num_robots
        for i in range(len(cities) % num_robots):
            partition_sizes[i] += 1
        partition_indices = np.cumsum([0] + partition_sizes)
        tours = []
        for i in range(num_robots):
            tour = [depots[i]] + cities[partition_indices[i]:partition_indices[i+1]] + [depots[i]]
            tours.extend(tour)
        population.append(Chromosome(tours))
    return population

def genetic_algorithm(num_cities, depots, num_robots, generations=1000, population_size=100):
    population = initialize_population(population_eta_size, num_cities, depots, num_robots)
    for _ in range(generations):
        # More detailed genetic operations to evolve the population would be added here
        pass
    
    # Example to pick the best solution and print results
    best_chromosome = min(population, key=lambda x: x.total_cost)
    robot_tours = {}
    index = 0
    for robot in robots:
        start = index
        end = index + 2 * (partition_sizes[robot] + 1)
        robot_tour = best_chromosome.tour[start:end]
        robot_tours[robot] = robot_tour
        index = end
    
    for i, tour in robot_tours.items():
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {Chromosome(tour).calculate_cost()}")

    print(f"Overall Total Travel Cost: {best_chromosome.total_cost}")

# Execute the genetic algorithm
genetic_algorithm(len(coordinates), depots, len(robots))