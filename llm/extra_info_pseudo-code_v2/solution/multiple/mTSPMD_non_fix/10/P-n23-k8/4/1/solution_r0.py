import numpy as np
import random
from scipy.spatial import distance_matrix

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate Distance matrix
coords = list(cities.values())
dist_matrix = distance_matrix(coords, coords)

# GA Parameters
num_generations = 1000
population_size = 50
mutation_rate = 0.05
num_cities = len(cities)
num_robots = 8

def create_initial_population():
    population = []
    for _ in range(population_size):
        tour = list(range(1, num_cities))  # start tour from city 1 to city N-1 (city 0 is the depot)
        random.shuffle(tour)
        separators = sorted(random.sample(range(1, num_cities - 1), num_robots - 1))
        for sep in separators:
            tour.insert(sep, -1)
        tour.insert(0, -1)  # Starting depot for the first robot
        tour.append(-1)  # Ending depot for the last robot
        population.append(tour)
    return population

def calculate_cost(tour):
    cost = 0
    start = 0
    current_tour = [0]  # Start from depot city 0
    for city in tour:
        if city == -1:
            if len(current_tour) > 1:  # End current tour at the last city before -1
                current_tour.append(current_tour[0])  # Back to start depot (circular)
                for i in range(len(current_tour) - 1):
                    cost += dist_matrix[current_tour[i]][current_tour[i + 1]]
                current_tour = [0]  # Restart at depot city 0
        else:
            current_tour.append(city)
    return cost

def mutation(tour):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(1, len(tour) - 1), 2)
        tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
    return tour

def genetic_algorithm():
    population = create_initial_population()
    for _ in range(num_generations):
        population = sorted(population, key=calculate_cost)
        next_gen = population[:10]  # elitism: top 10 solutions go directly to the next generation
        while len(next_gen) < population_size:
            parent1, parent2 = random.sample(population[:20], 2)  # tournament selection
            child1, child2 = crossover(parent1, parent2)
            next_gen.extend([mutation(child1), mutation(child2)])
        population = next_gen

    best_solution = min(population, key=calculate_cost)
    print_solution(best_solution)

def crossover(parent1, parent2):
    child1, child2 = parent1[:], parent2[:]
    return child1, child2

def print_solution(solution):
    robot_tour = []
    total_cost = 0
    current_tour = [0]  # Start from depot
    for city in solution:
        if city == -1:
            if len(current_tour) > 1:
                current_tour.append(0)  # end tour at depot
                robot_cost = sum(dist_matrix[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))
                total_cost += robot_cost
                print(f"Robot {len(robot_tour)} Tour: {current_tour}")
                print(f"Robot {len(robot_tour)} Total Travel Cost: {robot_cost}")
                current_tour = [0]
        else:
            current_tour.append(city)
    
    print(f"Overall Total Travel Cost: {total_cost}")

genetic_algorithm()