import numpy as np
import random
from scipy.spatial.distance import euclidean

# Cities data
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214),
    14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Robot start-end depots
depots = {
    0: 0, 1: 1, 2: 2, 3: 3
}

num_robots = len(depots)

# Genetic Algorithm parameters
population_size = 50
num_generations = 1000
mutation_rate = 0.1
crossover_rate = 0.8

def calculate_cost(tour):
    return sum(euclidean(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def create_initial_population():
    non_depot_cities = list(set(cities.keys()) - set(depots.values()))
    return [random.sample(non_depot_cities, len(non_depot_cities)) for _ in range(population_size)]

def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1) - 2)
    child = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
    return child

def mutate(tour):
    i, j = random.sample(range(len(tour)), 2)
    tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm():
    population = create_initial_population()
    for _ in range(num_generations):
        # Elitism: keep best solutions
        population = sorted(population, key=lambda tour: calculate_cost(tour))
        next_generation = population[:2]  # Keep the best 2 tours

        while len(next_generation) < population_size:
            if random.random() < crossover_rate:
                parent1, parent2 = random.sample(population, 2)
                child = crossover(parent1, parent2)
                if random.random() < mutation_rate:
                    mutate(child)
                next_generation.append(child)
            else:
                next_generation.append(random.choice(population))
        population = next_generation

    best_solution = population[0]
    return best_solution

# Run GA
best_tours = genetic_algorithm()

# Assign tours to robots and calculate costs
assigned_tours = {i: [depots[i]] for i in range(num_robots)}  # start at each depot
remaining_cities = best_tours[:]

# Heuristic: nearest neighbor assignment from depots
for city in remaining_cities:
    nearest_robot = min(assigned_tours, key=lambda r: euclidean(cities[city], cities[assigned_tours[r][-1]]))
    assigned_tours[nearest_robot].append(city)

# Close all loops
for robot in assigned_tours:
    assigned_tours[robot].append(depots[robot])

# Print results
total_cost = 0
for robot, tour in assigned_tours.items():
    cost = calculate_cost(tour)
    total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")