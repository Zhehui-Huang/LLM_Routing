import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Define the robots and their depots
robot_depot_mapping = [0, 1, 2, 3, 4, 5, 6, 7]

# Number of iterations for the GA
NUM_ITERATIONS = 500
POPULATION_SIZE = 50
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
TOURNAMENT_SIZE = 5
INDIVIDUAL_LENGTH = len(city_coords) - len(robot_depot_mapping)

# Helper function to calculate tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean(city_coords[tour[i-1]], city_coords[tour[i]])
    return cost

# Initialize population
def initialize_population():
    population = []
    all_cities = list(range(len(city_coords)))
    for _ in range(POPULATION_SIZE):
        tour_part = [city for city in all_cities if city not in robot_depot_mapping]
        random.shuffle(tour_part)
        population.append(tour_part)
    return population

# Selection using tournament selection
def tournament_selection(population):
    tournament = random.sample(population, TOURNAMENT_SIZE)
    tournament.sort(key=lambda indiv: calculate_tour_cost(indiv))
    return tournament[0]

# Order Crossover (OX)
def order_crossover(parent1, parent2):
    child = [None] * INDIVIDUAL_LENGTH
    start, end = sorted(random.sample(range(INDIVIDUAL_LENGTH), 2))
    child[start:end+1] = parent1[start:end+1]
    filled_positions = set(range(start, end+1))
    position = (end + 1) % INDIVIDUAL_LENGTH
    for city in parent2:
        if city not in child:
            child[position] = city
            position = (position + 1) % INDIVIDUAL_LENGTH
    return child

# Mutate using swap mutation
def mutate(individual):
    idx1, idx2 = random.sample(range(INDIVIDUAL_LENGTH), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Create the next generation
def create_next_generation(population):
    new_population = []
    while len(new_population) < POPULATION_SIZE:
        if random.random() < CROSSOVER_RATE:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = order_crossover(parent1, parent2)
            if random.random() < MUTATION_RATE:
                mutate(child)
            new_population.append(child)
        else:
            new_population.append(tournament_selection(population))
    return new_population

# Run the genetic algorithm
population = initialize_population()
best_individual = None
best_cost = float('inf')

for _ in range(NUM_ITERATIONS):
    population = create_next_generation(population)
    current_best = min(population, key=lambda indiv: calculate_tour_cost(indiv))
    current_cost = calculate_tour_cost(current_best)
    if current_cost < best_cost:
        best_cost = current_cost
        best_individual = current_best

# Extract tours for each robot
tours = [[] for _ in robot_depot_mapping]
cities_assigned = best_individual
index = 0

for robot_id, depot in enumerate(robot_depot_mapping):
    tour = [depot]
    while len(tour) < (INDIVIDUAL_LENGTH // len(robot_depot_mapping) + 1):
        tour.append(cities_assigned[index])
        index = (index + 1) % INDIVIDUAL_LENGTH
    tour.append(depot)  # return to depot
    tours[robot_id] = tour

# Display the results
overall_cost = 0
for robot_id, tour in enumerate(tours):
    cost = calculate_tour_cost(tour)
    overall_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")