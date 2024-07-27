import numpy as np
import random

# City coordinates (index corresponds to city number)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Genetic Algorithm Parameters
population_size = 50
num_generations = 500
mutation_rate = 0.1

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return total_distance

def create_initial_population():
    population = []
    cities = list(range(2, len(coordinates)))  # Exclude depots
    for _ in range(population_size):
        random.shuffle(cities)
        # Splitting at random point for two robots
        split_point = random.randint(1, len(cities)-1)
        robot0_tour = [0] + cities[:split_point] + [0]
        robot1_tour = [1] + cities[split_point:] + [1]
        population.append((robot0_tour, robot1_tour))
    return population

def crossover(parent1, parent2):
    """ Partially Matched Crossover (PMX) """
    # Note: Implement this based on your understanding
    # This is a placeholder implementation.
    return parent1, parent2

def mutate(tour):
    """ Swap mutation """
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(tour)-1), 2)  # Avoid depots
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm():
    population = create_initial_population()
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(num_generations):
        new_population = []
        costs = []
        for tour_pair in population:
            cost = calculate_total_distance(tour_pair[0]) + calculate_total_distance(tour_pair[1])
            costs.append(cost)
            if cost < best_cost:
                best_cost = cost
                best_solution = tour_pair
                
        # Selection based on costs (roulette wheel or tournament)
        # Crossover and mutation
        # Populate `new_population`
        
        # Update population
        population = new_population
        
    return best_solution, best_cost

best_solution, best_cost = genetic_algorithm()

print(f"Robot 0 Tour: {best_solution[0]}")
print(f"Robot 0 Total Travel Cost: {calculate_total_distance(best_solution[0])}")

print(f"Robot 1 Tour: {best_solution[1]}")
print(f"Robot 1 Total Travel Cost: {calculate_total_distance(best_solution[1])}")

print(f"Overall Total Travel Cost: {best_cost}")