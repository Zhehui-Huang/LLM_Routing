import numpy as np
import random
from itertools import permutations

# Define the coordinates of each city and the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate the Euclidean distance between two cities
def distance(i, j):
    dx = coordinates[i][0] - coordinates[j][0]
    dy = coordinates[i][1] - coordinates[j][1]
    return np.sqrt(dx**2 + dy**2)

# Genetic Algorithm parameters
num_robots = 2
depots = [0, 1]
mutation_rate = 0.1
population_size = 50
num_generations = 500
tournament_size = 5

def initial_population():
    # Create an initial population dispersed among robots
    population = []
    for _ in range(population_size):
        cities = list(range(2, len(coordinates)))  # excluding depot cities
        random.shuffle(cities)
        # Divide cities among robots
        split_index = random.randint(1, len(cities) - 1)
        tours = [cities[:split_index], cities[split_index:]]
        population.append(tours)
    return population

def evaluate_tour(tour, depot):
    # compute the full route from depot and back to depot including the route cost
    full_route = [depot] + tour + [depot]
    return sum(distance(full_route[i], full_route[i+1]) for i in range(len(full_route) - 1))

def fitness(population):
    # Evaluate each individual
    fitness_scores = []
    for tours in population:
        total_cost = 0
        for i, tour in enumerate(tours):
            total_cost += evaluate_tour(tour, depots[i])
        fitness_scores.append((tours, total_cost))
    fitness_scores.sort(key=lambda x: x[1])  # sort by total travel cost
    return fitness_scores

def crossover(parent1, parent2):
    # One point crossover for tours of robots
    child1 = [parent1[0][:], parent2[1][:]]
    child2 = [parent2[0][:], parent1[1][:]]
    return child1, child2

def mutate(tours):
    # Swap mutation within each robot's tour
    for tour in tours:
        if random.random() < mutation_rate:
            i, j = random.sample(range(len(tour)), 2)
            tour[i], tour[j] = tour[j], tour[i]
    return tours

def genetic_algorithm():
    pop = initial_population()
    for generation in range(num_generations):
        pop = fitness(pop)
        new_population = [pop[i][0] for i in range(len(pop)//2)]  # elitism: keep the best half
        while len(new_population) < population_size:
            if random.random() < 0.7:  # crossover probability
                parents = random.sample(pop, 2)
                child1, child2 = crossover(parents[0][0], parents[1][0])
                new_population.extend([mutate(child1), mutate(child2)])
            else:
                new_population.append(mutate(random.choice(pop)[0]))  # mutation only
        pop = new_population

    best_solution = fitness(pop)[0]
    return best_solution

best_solution = genetic_algorithm()

# Output the tours and costs
for i, tour in enumerate(best_solution[0]):
    robot_tour = [depots[i]] + tour + [depots[i]]
    tour_cost = evaluate_tour(tour, depots[i])
    print(f"Robot {i} Tour: {robot_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {best_solution[1]}")