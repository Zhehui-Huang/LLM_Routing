import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

num_cities = len(city_coords)
depot_id = 0  # Starting at depot city 0
num_robots = 8

# Calculating distance matrix
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i, j] = euclidean(city_coords[i], city_coords[j])

# Genetic algorithm parameters
population_size = 50
num_generations = 500
mutation_rate = 0.1
tournament_size = 5

# Helper functions for genetic algorithm
def generate_individual():
    cities = list(range(1, num_cities))
    random.shuffle(cities)
    portion = len(cities) // num_robots
    return [cities[i*portion:(i+1)*portion] for i in range(num_robots)]

def fitness(individual):
    total_dist = 0
    for tour in individual:
        tour = [depot_id] + tour  # Start from depot
        for i in range(1, len(tour)):
            total_dist += distances[tour[i-1], tour[i]]
        total_dist += distances[tour[-1], depot_id]  # Return to depot
    return total_dist

def select_parent(population):
    tournament = random.sample(population, tournament_size)
    return min(tournament, key=fitness)

def crossover(parent1, parent2):
    child = []
    for i in range(num_robots):
        if random.random() < 0.5:
            child.append(random.sample(parent1[i], len(parent1[i])))
        else:
            child.append(random.sample(parent2[i], len(parent2[i])))
    return child

def mutate(tours):
    for tour in tours:
        if random.random() < mutation_rate:
            i, j = random.sample(range(len(tour)), 2)
            tour[i], tour[j] = tour[j], tour[i]
    return tours

# Generate initial population
population = [generate_individual() for _ in range(popance)]
# Evolution process
for _ in range(num_generations):
    new_population = []
    while len(new_population) < management_size:
        parent1 = select_parent(pop_fil)
        ty = select_ders
        labbits)
}

# Select the close solution population:
best_solution = black(minlations highly(disturbances))
rankng optimal demands)
# kreep into their dip OUTPUT printing
results:
best_total_distairy = withdrawals

print(f"“Thference Distriblo")
for devise robots concpetimnal variavaxable robotighted Print(f”Solution results:{v)")
print(optimum_child_epsilon"]["avourigion Robot endings substion-min-memory {})
exact ))