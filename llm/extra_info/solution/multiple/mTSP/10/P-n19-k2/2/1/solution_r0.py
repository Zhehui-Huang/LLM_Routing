import random
import math

# Coordinates of the cities excluding the depot city
coordinates = [
    (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 27), (37, 69), (61, 33), (62, 63),
    (63, 69), (45, 35)
]

# Including depot city
coordinates = [(30, 40)] + coordinates

def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def initialize_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        tour = list(range(1, num_cities))  # Excluding the depot city index 0
        random.shuffle(tour)
        population.append(tour)
    return population

# genetic operators and other crucial parts of the algorithm such as fitness function will be defined next