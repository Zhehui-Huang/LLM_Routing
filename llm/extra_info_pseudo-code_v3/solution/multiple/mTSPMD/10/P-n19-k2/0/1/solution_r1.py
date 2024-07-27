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
def calc_distance(city1: int, city2: int) -> float:
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + 
                     (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# Function to compute total travel cost of a tour
def tour_cost(tour: List[int]) -> float:
    return sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Genetic algorithm operators and functions

def crossover(tour1: List[int], tour2: List[int]) -> List[int]:
    start = tour1[0]
    size = len(tour1)
    p, q = sorted(random.sample(range(1, size-1), 2))
    middle = tour1[p:q]
    new_tour = [city for city in tour2 if city not in middle]
    return [start] + new_tour[:p-1] + middle + new_tour[p-1:]

def mutate(tour: List[int], mutation_rate: float=0.05) -> List[int]:
    if random.random() < mutation_rate:
        i, j = sorted(random.sample(range(1, len(tour) - 1), 2))
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Main genetic algorithm function
def genetic_algorithm(start_depot: int, num_cities: int, num_generations: int=500, population_size: int=50, mutation_rate: float=0.1) -> List[int]:
    population = [random.sample(range(num_cities), num_cities) for _ in range(population_size)]
    for _ in range(num_generations):
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

# Append the depot city at the start and end of the tour
robot_0_tour = [0] + robot_0_tour + [0]
robot_1_tour = [1] + robot_1_tour + [1]

# Output the results
print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", round(robot_0_cost, 2))
print("Robot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", round(robot_1_cost, 2))
print("Overall Total Travel Cost:", round(total_cost, 2))