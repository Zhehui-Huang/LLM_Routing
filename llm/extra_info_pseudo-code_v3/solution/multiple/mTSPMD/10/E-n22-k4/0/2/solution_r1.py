import numpy as np
from scipy.spatial import distance_matrix
import random

# Define cities and their coordinates as given
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Robot depot assignments
depots = [0, 1, 2, 3]
num_robots = 4

# Calculate distance matrix using Euclidean distance
coordinates = np.array(cities)
dist_matrix = distance_matrix(coordinates, coordinates)

# Genetic Algorithm parameters
population_size = 50
generations = 500
mutation_rate = 0.15
tournament_size = 5

def generate_initial_population():
    population = []
    for _ in range(population_size):
        for start_depot in depots:
            tour = random.sample(range(len(cities)), len(cities))
            tour.remove(start_depot)
            tour.insert(0, start_depot)
            tour.append(start_depot)
            population.append(tour)
    return population

def calculate_cost(tour):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

def crossover(parent1, parent2):
    cut1, cut2 = sorted(random.sample(range(1, len(parent1)-1), 2))
    middle = parent1[cut1:cut2+1]
    child = [parent2[0]] + [c for c in parent2[1:-1] if c not in middle] + [parent2[-1]]
    child[cut1:cut1+len(middle)] = middle
    return child

def mutate(tour):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(tour)-1), 2)
        tour[i], tour[j] = tour[j], tour[i]

def tournament_selection(population):
    contenders = random.sample(population, tournament_size)
    contender_costs = [calculate_cost(tour) for tour in contenders]
    winner_index = np.argmin(contender_costs)
    return contenders[winner_index]

# Initialize population
population = generate_initial_population()

# Run genetic algorithm
for _ in range(generations):
    new_population = []
    while len(new_population) < population_size:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        child = crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)
    population = new_population

# Determine the best solution and its cost
best_solution = min(population, key=calculate_cost)
best_cost = calculate_cost(best_solution)

# Output results
print("Best tour:", best_solution)
print("Tour cost:", best_cost)

# Further segregate tours by each robot, considering return to start
robot_tours = {d: [d] for d in depots}
current_robot = best_solution[0]
for city in best_solution[1:]:
    if city in depots:
        current_robot = city
    robot_tours[current_robot].append(city)

for robot, tour in robot_tours.items():
    tour_cost = calculate_cost(tour)
    print(f"Robot from Depot {robot}: Tour = {tour}, Cost = {tour_cost}")