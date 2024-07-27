import numpy as np
import random
from scipy.spatial.distance import euclidean
from itertools import permutations

# Given city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

num_cities = len(cities)
robots = 2  # Number of robots
depots = [0, 1]  # Depot indices

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Generate a random solution (initial chromosome)
def create_random_solution():
    all_cities = list(range(2, num_cities))
    random.shuffle(all_cities)
    split = random.randint(1, len(all_cities) - 1)
    return ([0] + all_cities[:split] + [0], [1] + all_cities[split:] + [1])

def evaluate_tour(tour):
    cost = 0
    for i in range(len(tour)-1):
        cost += distance(tour[i], tour[i+1])
    return cost

def evaluate_solution(solution):
    return sum(evaluate_tour(tour) for tour in solution)

def crossover(tour1, tour2):
    tour1_middle = tour1[1:-1]
    tour2_middle = tour2[1:-1]
    random.shuffle(tour1_middle)
    random.shuffle(tour2_middle)
    split = random.randint(1, min(len(tour1_middle), len(tour2_middle)) - 1)
    new_tour1 = [tour1[0]] + tour1_middle[:split] + tour2_middle[split:] + [tour1[-1]]
    new_tour2 = [tour2[0]] + tour2_middle[:split] + tour1_middle[split:] + [tour2[-1]]
    return new_tour1, new_tour2

def mutate(tour):
    idx1, idx2 = random.sample(range(1, len(tour)-1), 2)
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

def genetic_algorithm(generations=1000, population_size=10):
    # Initialize population
    population = [create_random_solution() for _ in range(population_size)]
    for _ in range(generations):
        # Evaluate current population
        evaluated = [(evaluate_solution(ind), ind) for ind in population]
        evaluated.sort()  # Sort by total cost
        # Elitism - keep the best solutions
        next_population = [ind for _, ind in evaluated[:population_size // 2]]
        # Crossover and mutation
        while len(next_population) < population_size:
            if random.random() < 0.85:  # Crossover rate
                p1, p2 = random.sample(next_population, 2)
                offspring1, offspring2 = crossover(p1, p2)
                next_population += [offspring1, offspring2]
            for individual in next_population:
                if random.random() < 0.15:  # Mutation rate
                    mutate(individual[0])
                    mutate(individual[1])
        population = next_population

    # Best solution
    best_solution = min(population, key=evaluate_solution)
    return best_solution

# Running the Genetic Algorithm to find the solution
best_solution = genetic_algorithm()

print("Optimal tours and costs:")
total_cost = 0
for robot_id, tour in enumerate(best_solution):
    tour_cost = evaluate_tour(tour)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")