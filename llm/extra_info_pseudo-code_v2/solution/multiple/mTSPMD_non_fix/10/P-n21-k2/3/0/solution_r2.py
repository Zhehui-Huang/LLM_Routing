import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}
num_cities = len(cities)

# Calculate distance between two cities
def distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Generate initial random solution
def create_random_solution():
    all_cities = list(range(2, num_cities))
    random.shuffle(all_cities)
    split = random.randint(1, len(all_cities) - 1)
    return ([0] + all_cities[:split] + [0], [1] + all_cities[split:] + [1])

# Evaluate the total cost of tours for both robots
def evaluate_solution(solution):
    return sum(evaluate_tour(tour) for tour in solution)

# Evaluate single tour cost
def evaluate_tour(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Genetic algorithm implementation
def genetic_algorithm(generations=1000, population_size=20):
    population = [create_random_solution() for _ in range(population_size)]
    for _ in range(generations):
        population.sort(key=evaluate_solution)
        next_generation = population[:population_size // 2]
        
        while len(next_generation) < population_size:
            if random.random() < 0.7:  # Crossover probability
                parent1, parent2 = random.sample(next_generation, 2)
                child1, child2 = crossover(parent1, parent2)
                next_generation.extend([child1, child2])
            
            for individual in next_generation:  # Mutation
                if random.random() < 0.1:
                    mutate(individual)

        population = next_generation

    best_solution = min(population, key=evaluate_solution)
    return best_solution

# One-point crossover operation
def crossover(parent1, parent2):
    split = random.randint(1, len(parent1[0]) - 2)
    child1 = (parent1[0][:split] + parent2[0][split:], parent1[1])
    child2 = (parent2[0][:split] + parent1[0][split:], parent2[1])
    return child1, child2

# Mutation operation: swapping two cities in a tour
def mutate(individual):
    tour = individual[random.randint(0, 1)]
    idx1, idx2 = random.sample(range(1, len(tour) - 1), 2)
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

# Execute the genetic algorithm and display results
best_solution = genetic_algorithm()
total_cost = evaluate_solution(best_solution)
print("Optimal tours and costs:")
for robot_id, tour in enumerate(best_solution):
    tour_cost = evaluate_tour(tour)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")