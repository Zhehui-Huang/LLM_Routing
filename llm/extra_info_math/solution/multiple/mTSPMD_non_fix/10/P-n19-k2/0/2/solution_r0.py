import numpy as np
import random
from scipy.spatial.distance import euclidean

# Coordinates of all cities including depots
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Parameters for GA
num_generations = 100
population_size = 50
mutation_rate = 0.1
num_cities = len(cities)
num_robots = 2
depots = [0, 1]  # Depots from where robots start

# Helper function to calculate euclidean distance
def calculate_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean(cities[tour[i-1]], cities[tour[i]])
    return total_cost

# Initialize population
def initialize_population():
    population = []
    non_depot_cities = list(range(2, num_cities))
    for _ in range(population_size):
        random.shuffle(non_depot_cities)
        # Each chromosome is a full round trip starting and ending at the depot
        split_point = random.randint(1, len(non_depot_cities)-1)
        robot1_tour = [depots[0]] + non_depot_cities[:split_point] + [depots[0]]
        robot2_tour = [depots[1]] + non_depot_cities[split_point:] + [depots[1]]
        population.append([robot1_tour, robot2_tour])
    return population

# Genetic operations
def crossover(parent1, parent2):
    # One point crossover for each robot's tour sublist
    def one_point_crossover(sub1, sub2):
        pt = random.randint(1, len(sub1) - 2)
        new_sub1 = sub1[:pt] + sub2[pt:]
        new_sub2 = sub2[:pt] + sub1[pt:]
        return new_sub1, new_sub2

    new_robot1_tour1, new_robot1_tour2 = one_point_crossover(parent1[0], parent2[0])
    new_robot2_tour1, new_robot2_tour2 = one_point_crossover(parent1[1], parent2[1])
    return [[new_robot1_tour1, new_robot2_tour1], [new_robot1_tour2, new_robot2_tour2]]

def mutate(tour):
    # Simple swap mutation, avoiding depots
    if len(tour) > 4:  # Ensure there's room to mutate
        i, j = random.sample(range(1, len(tour) - 1), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Evolution function
def evolve(population):
    new_population = []
    scores = [(sum(calculate_cost(tour) for tour in individual), individual) for individual in population]
    scores.sort()  # Sort by total traveling cost
    elite = scores[:2]  # Top 2 low-cost solutions go unchanged

    # Tournament selection and breeding
    tournament_size = 5
    while len(new_population) < population_size:
        parent1 = min(random.sample(scores, tournament_size))[1]
        parent2 = min(random.sample(scores, tournament_1_size))[1]
        offspring1, offspring2 = crossover(parent1, parent2)
        new_population.append(offspring1)
        new_population.append(offspring2)
  
    # Mutation
    new_population = [mutate(tour) for individual in new_population for tour in individual]

    # Add back elite
    new_population.extend(individual for _, individual in elite)
  
    return new_population

# Initialize and run GA
population = initialize_population()
for _ in range(num_generations):
    population = evolve(population)

# Extract best solution
best_solution = min(population, key=lambda indiv: sum(calculate_cost(tour) for tour in indiv))

# Printing the solution found
for i, tour in enumerate(best_o_worker do_something_with(worker); (solution):
    cost = calculate_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")
overall_cost = sum(calculate_cost(tour) for tour in best_solution)
print(f"Overall Total Travel Cost: {overall_cost:.2f}")