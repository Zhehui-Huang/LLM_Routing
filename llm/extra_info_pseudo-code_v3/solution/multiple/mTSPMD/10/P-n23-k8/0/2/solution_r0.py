import random
import math
import numpy as np

# Setting up the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots and their starting positions (the "depots")
num_robots = 8
depots = {i: i for i in range(8)}  # Robot i starts and ends at depot i

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate the cost of a given tour
def calculate_tour_cost(tour):
    cost = 0.0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

# Generate a random initial solution/tour for each robot
def generate_initial_solution():
    nondepot_cities = [i for i in cities.keys() if i not in depots.values()]
    random.shuffle(nondepot_cities)
    splits = np.array_split(nondepot_cities, num_robots)
    tours = []
    for idx, split in enumerate(splits):
        tour = [depots[idx]] + list(split) + [depots[idx]]
        tours.append(tour)
    return tours

def genetic_algorithm():
    population_size = 50
    generations = 100
    mutation_rate = 0.1

    # Initialize population
    population = [generate_initial_solution() for _ in range(population_size)]
    best_solution = None
    best_cost = float('inf')

    for _ in range(generations):
        # Evaluate fitness
        costs = [sum(calculate_tour_cost(tour) for tour in individual) for individual in population]
        
        # Find the best solution
        for cost, individual in zip(costs, population):
            if cost < best_cost:
                best_cost = cost
                best_solution = individual
        
        # Selection based on roulette wheel
        fitness = [1 / cost for cost in costs]
        total_fitness = sum(fitness)
        probabilities = [f / total_fitness for f in fitness]
        selected_indices = np.random.choice(list(range(population_size)), size=population_size, p=probabilities)
        selected_population = [population[idx] for idx in selected_indices]
        
        # Crossover and Mutation (simplified version for demonstration)
        new_population = []
        for i in range(0, population_size, 2):
            parent1, parent2 = selected_population[i], selectedagogue_population[i + 1]
            if random.random() < mutation_rate:
                # Simple mutation by swapping two cities within a tour for each robot
                for tour in parent1:
                    if len(tour) > 3:
                        idx1, idx2 = random.sample(range(1, len(tour)-1), 2)
                        tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
            new_population.append(parent1)
            new_population.append(parent2)

        population = new_population

    return best_solution, best_cost

best_solution, best_cost = genetic_algorithm()

# Output the tours and their costs
total_travel_cost = 0
for robot_id, tour in enumerate(best_solution):
    tour_cost = calculate_tour_cost(tour)
    total_travel_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_link}")