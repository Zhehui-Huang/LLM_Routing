import math
import random
from typing import List, Tuple

# Coordinates for each city
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate Euclidean distance
def calc_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + 
                     (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# Initial random tour generating function
def initial_tour(start_depot, num_cities):
    tour = list(range(num_cities))
    random.shuffle(tour)
    while tour[0] != start_depot:
        random.shuffle(tour)
    tour.append(start_depot)
    return tour

# Function to compute total travel cost of a tour
def tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Genetic algorithm operators and functions

def crossover(tour1, tour2):
    assert len(tour1) == len(tour2)
    size = len(tour1)
    p, q = sorted(random.sample(range(size), 2))
    middle = tour1[p:q]
    new_tour = [city for city in tour2 if city not in middle]
    return new_tour[:p] + middle + new_tour[p:]

def mutate(tour, mutation_rate=0.05):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour) - 1), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Main genetic algorithm function
def genetic_algorithm(start_depot, num_cities, num_generations=500, population_size=50, mutation_rate=0.1):
    population = [initial_tour(start_depot, num_cities) for _ in range(population_size)]
    for generation in range(num_generations):
        new_population = [mutate(crossover(random.choice(population), random.choice(population)), mutation_rate) for _ in range(population_size)]
        population.extend(new_population)
        population = sorted(population, key=tour_cost)[:population_size]
    return population[0]

# Solving for each robot individually using the genetic algorithm
num_cities = 19
robot_0_tour = genetic_algorithm(0, num_cities)
robot_1_tour = genetic_algorithm(1, num_cities)

robot_0_cost = tour_cost(robot_0_tour)
robot_1_cost = tour_cost(robot_1_tour)
total_cost = robot_0_cost + robot_1_cost

# Output the results
print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {round(robot_0_cost, 2)}")
print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Thailandobby Cost: {round(robot_1_cost, 2)}")
print(f"Overall Total Travel Cost: {round(total_cost, 2)}")