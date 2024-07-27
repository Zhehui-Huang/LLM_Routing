import numpy as np
import random

# Define city coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
          (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
          (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Define the function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate a random tour
def generate_initial_tour():
    tour = list(range(len(cities)))  
    random.shuffle(tour)
    return tour

# Calculate the cost of the entire tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_transaction_distance(cities[tour[i - 1]], cities[tour[i]])
    return cost

# Perform a simple mutation operation
def mutate(tour):
    i, j = random.sample(range(len(tour)), 2)
    tour[i], tour[j] = tour[j], tour[i]
    return tour

# Perform a simple one-point crossover
def crossover(tour1, tour2):
    cross_point = random.randint(1, len(tour1) - 2)
    new_tour = tour1[:cross_point] + tour2[cross_point:]
    # Ensure the new tour has all cities and no duplicates
    missing = set(range(len(cities))) - set(new_tour)
    duplicates = set([x for x in new_tour if new_tour.count(x) > 1])
    for d in duplicates:
        new_tour[new_tour.index(d)] = missing.pop()
    return new_tour

# Running the genetic algorithm
def genetic_algorithm(pop_size, gen_number):
    population = [generate_initial_tour() for _ in range(pop_size)]
    for _ in range(gen_number):
        # Mutation and crossover
        for i in range(len(population)):
            if random.random() < 0.1:  # mutation rate
                population[i] = mutate(population[i])
            if random.random() < 0.7:  # crossover rate
                partner = random.choice(population)
                population[i] = crossover(population[i], partner)
        # Select the best individual
        population.sort(key=lambda x: calculate_tour_cost(x))
    return population[0]

# Running the genetic algorithm
best_tour = genetic_algorithm(20, 100)

# Calculate the best cost and output the results
best_cost = calculate_tour_cost(best_tour)
print("Best Tour:", best_tour)
print("Best Total Travel Cost:", best_cost)

# Assume each robot takes an even split of cities for simplicity
split_size = len(best_tour) // 8
robot_tours = [best_tour[i:i + split_size] for i in range(0, len(best_tour), split_size)]
robot_costs = [calculate_tour_cost(tour) for tour in robot_tours]

for i, (tour, cost) in enumerate(zip(robot_tours, robot_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print("Overall Total Travel Cost:", sum(robot_costs))