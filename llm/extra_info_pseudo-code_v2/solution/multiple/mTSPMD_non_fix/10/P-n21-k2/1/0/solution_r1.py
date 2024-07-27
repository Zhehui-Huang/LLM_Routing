import numpy as np
from scipy.spatial.distance import euclidean
import random

# Coordinates of the cities including depots
coordinates = [
    (30, 40), (37, 52), # Depot 0, Depot 1
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), # Cities 2-9
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), # Cities 10-17
    (62, 63), (63, 69), (45, 35)  # Cities 18-20
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return euclidean(coordinates[city1], coordinates[city2])

# class encapsulation of GA operations
class GeneticAlgorithm:
    def __init__(self, num_robots=2, pop_size=100, generations=1000, mutation_rate=0.1, crossover_rate=0.9):
        self.num_robots = num_robots
        self.pop_size = pop_size
        self.generations = generations
        self.mutation_rate = mutation���rate
        self.crossover_rate = crossover_rate
        self.num_cities = len(coordinates)
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for _ in range(self.pop_size):
            # Create a path including all cities
            path = list(range(2, self.num_cities))
            random.shuffle(path)
            # Insert depots at random to create tours for the robots
            splits = sorted(random.sample(range(1, len(path)), self.num_robots - 1))
            tours = [path[i:j] for i, j in zip([0] + splits, splits + [None])]
            chromosome = []
            for idx, tour in enumerate(tours):
                chromosome.append(idx)  # Each tour starts from depot idx (0 or 1)
                chromosome.extend(tour)
                chromosome.append(idx)  # Return to depot idx
            population.append(chromosome)
        return population

    def evaluate(self, chromosome):
        total_cost = 0
        idx = 0
        while idx < len(chromosome):
            depot = chromosome[idx]
            idx += 1
            tour_cost = 0
            start_city = depot
            while idx < len(chromosome) and isinstance(chromosome[idx], int):
                end_city = chromosome[idx]
                tour_cost += distance(start_city, end_city)
                start_city = end_city
                idx += 1
            total_cost += tour_cost
            if idx < len(chromosome):
                idx += 1  # skip over the depot return entry
        return total_cost

    def run(self):
        best_solution = None
        best_cost = float('inf')
        for _ in range(self.generations):
            new_pop = []
            for _ in range(self.pop_size):
                chromosome = random.choice(self.population)
                if random.random() < self.mutation_rate:
                    self.mutate(chromosome)
                if random.random() < self.crossover_rate:
                    partner = random.choice(self.population)
                    chromosome = self.crossover(chromosome, partner)
                new_pop.append(chromosome)
                cost = self.evaluate(chromosome)
                if cost < best_cost:
                    best_cost = cost
                    best_solution = chromosome
            self.population = new.pop
        return best_solution, best_cost

    def mutate(self, chromosome):
        # Simple mutation: swap two cities in a tour
        a, b = random.sample(range(len(chromosome)), 2)
        chromosome[a], chromosome[b] = chromosome[b], chromosome[a]

    def crossover(self, parent1, parent2):
        # Simple crossover: take the first half from parent1 and the second from parent2
        cut = len(parent1) // 2
        return parent1[:cut] + parent2[cut:]

# Main execution
ga = GeneticAlgorithm()
best_solution, best_cost = ga.run()

# Constructing tours from the solution
tours = [[] for _ in range(ga.num_robots)]
current_robot = None
for item in best_solution:
    if isinstance(item, int) and item < ga.num_robots:  # This is a depot index
        current_robot = item
    else:
        tours[current_robot].append(item)

# Output the results
print('Optimized Tours and Costs:\n')
total_travel_cost = 0
for idx, tour in enumerate(tours):
    robot_tour = [idx] + tour + [idx]  # Start and end at the same depot
    total_cost = sum(distance(robot_tour[i], robot_tour[i + 1]) for i in range(len(robot_tour) - 1))
    total_travel_cost += total_cost
    print(f'Robot {idx} Tour:', robot_tour)
    print(f'Robot {idx} Total Travel Cost:', total_cost)

print('\nOverall Total Travel Cost:', total_travel_cost)