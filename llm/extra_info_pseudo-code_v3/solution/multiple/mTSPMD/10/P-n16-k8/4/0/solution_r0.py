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
robot_depot_mapping = {i: i for i in range(num_robots)}

# Function to calculate Euclidean distances between cities
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i, j] = euclidean(coords[i], coords[j])
    return dist_matrix

# Using numpy array for faster computation
distance_matrix = calculate_true_distance_matrix(coordinates)

# Genetic Algorithm Implementation
class Chromosome:
    def __init__(self):
        # Generate random permutations of city indices for tours
        self.permutation = list(range(1, len(coordinates)))
        random.shuffle(self.permutation)
        # Assign starting part of perm to each robot roughly evenly
        self.division = []
        cities_per_robot = len(self.permutation) // num_robots
        leftover_cities = len(self.permutation) % num_robots
        
        current = 0
        for _ in range(num_robots):
            next = current + cities_per_robot + (1 if leftover_cities > 0 else 0)
            self.division.append(self.permutation[current:next])
            current = next
            leftover_cities -= 1

    def get_tours(self):
        # Each sublist in result represents a robot tour starting and ending at its depot
        tours = []
        for idx, robot_cities in enumerate(self.division):
            depot = robot_depot_mapping[idx]
            tour = [depot] + robot_cies + [depot]
            tours.append(tour)
        return tours

    def fitness(self):
        # Calculate total distance of the tours
        total_cost = 0
        for tour in self.get_tours():
            tour_cost = 0
            for i in range(len(tour) - 1):
                tour_cost += distance_matrix[tour[i]][tour[i + 1]]
            total_cost += tour_cost
        return total_cost


def genetic_algorithm():
    # Assuming a population size of 10 and running for 30 generations
    population = [Chromosome() for _ in range(10)]
    for _ in range(30):
        # Evaluate the population
        sorted_population = sorted(population, key=lambda x: x.fitness())
        # Select top performers (simple elitist selection, 4 best)
        population = sorted_population[:4]
        # Crossover and mutation to generate new members
        while len(population) < 10:
            p1, p2 = random.sample(population, 2)
            offspring = crossover(p1, p2)
            offspring.mutate()
            population.append(offspring)

    # Select the best solution
    best_solution = sorted(population, key=lambda x: x.fitness())[0]
    return best_solution

# Running the genetic_algorithm function will produce the output
best_chromosome = genetic_algorithm()
for idx, tour in enumerate(best.chromosome.get_tours()):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {calculate_tour_cost(tour, distance_matrix)}")

print("Overall Total Travel Cost:", best_chromosome.fitness())