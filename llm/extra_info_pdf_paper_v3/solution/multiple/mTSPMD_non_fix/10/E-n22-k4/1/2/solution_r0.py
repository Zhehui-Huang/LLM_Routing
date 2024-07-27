import math
import random
from operator import attrgetter

# Define the cities with their coordinates
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206),
    (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

def calculate_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities given their indices """
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Genetic Algorithm Settings
num_generations = 1000
population_size = 100
mutation_rate = 0.05
crossover_rate = 0.8
tour_size = (len(city_coords) - num_robots) // num_robots

class Chromosome:
    def __init__(self):
        self.routes = [[] for _ in range(num_robots)]
        self.total_cost = 0

    def calculate_fitness(self):
        self.total_cost = sum(
            sum(calculate_distance(self.routes[i][j], self.routes[i][j + 1]) 
                for j in range(len(self.routes[i]) - 1)) 
            for i in range(num_robots)
        )
        return self.total_cost

    def random_initialization(self):
        available_cities = list(range(4, len(city_coords)))  # Assuming the depots are city 0 through city 3
        random.shuffle(available_cities)
        for i in range(num_robots):
            self.routes[i].append(i)  # Start each route at its corresponding depot
            for _ in range(tour_size):
                self.routes[i].append(available_cities.pop())
            self.routes[i].append(i)  # End at the depot (not needed if non-returning)

def create_initial_population():
    population = [Chromosome() for _ in range(population_size)]
    for chromosome in population:
        chromosome.random_initialization()
        chromosome.calculate_fitness()
    return population

def select_parents(population):
    """ Tournament selection """
    return random.sample(population, 2)

def crossover(parent1, parent2):
    """ Implement partially mapped crossover (PMX) for routes """
    # Simplified for this approach, directly swapping sections
    if random.random() < crossover_rate:
        child = Chromosome()
        for i in range(num_robots):
            cutpoint1, cutpoint2 = sorted(random.sample(range(1, tour_size), 2))
            child.routes[i] = parent1.routes[i][:cutpoint1] + parent2.routes[i][cutpoint1:cutpoint2] + parent1.routes[i][cutpoint2:]
        return child
    return parent1 or parent2

def mutate(chromosome):
    """ Swap mutation """
    for route in chromosome.routes:
        if random.random() < mutation_rate:
            idx1, idx2 = random.sample(range(1, len(route) - 2), 2)
            route[idx1], route[idx2] = route[idx2], route[idx1]

def genetic_algorithm():
    population = create_initial_population()

    for generation in range(num_generations):
        next_population = []
        while len(next_population) < population_size:
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            mutate(child)
            child.calculate_fitness()
            next_population.append(child)
        population = sorted(next_population, key=attrgetter('total_cost'))[:population_size]
        if generation % 100 == 0:
            print(f"Generation {generation}: Best cost = {population[0].total_cost}")

    # Finish and display the final best solution
    best_solution = min(population, key=attrgetter('total_cost'))
    return best_solution

# Run the GA
best_solution = genetic_algorithm()
for idx, route in enumerate(best_solution.routes):
    print(f"Robot {idx} Tour: {route}")
    route_cost = sum(calculate_distance(route[i], route[i+1]) for i in range(len(route)-1))
    print(f"Robot {idx} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {best_solution.total_cost}")