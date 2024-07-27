import random
import math

# Data Setup
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}
depots = [0, 1]

# Utility functions
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

# Genetic Algorithm components
def create_chromosome():
    non_depot_cities = list(cities.keys())[2:]
    random.shuffle(non_depot_cities)
    split_point = len(non_depot_cities) // 2
    tours = [depots[0]] + non_depot_cities[:split_point] + [depots[0]], \
            [depots[1]] + non_depot_cities[split_point:] + [depots[1]]
    return tours

def crossover(parent1, parent2):
    # Simple one-point crossover for tours
    child = [parent1[0], parent2[1]]
    return child

def mutate(tour):
    # Simple swap mutation in each tour
    for i in range(2):
        idx1, idx2 = random.sample(range(1, len(tour[i]) - 1), 2)
        tour[i][idx1], tour[i][idx2] = tour[i][idx2], tour[i][idx1]

def genetic_algorithm():
    population = [create_chromosome() for _ in range(50)]
    for _ in range(100):  # Number of generations
        new_population = []
        for _ in range(25):  # Generate new offspring
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
            new_population.append(parent1)
            new_population.append(parent2)
        # Compute fitness and select the best 50 to continue
        population = sorted(new_population, key=lambda x: sum(calculate_tour_cost(t) for t in x))[:50]
    return population[0]

# Run the algorithm
best_solution = genetic=algorithm()

# Output the results
robot0_tour = best_solution[0]
robot1_tour = best_solution[1]
robot0_cost = calculate_tour_cost(robot0_tour)
robot1_cost = calculate_tour_cost(robot1_tour)
total_cost = robot0_cost + robot1_cost

print("Robot 0 Tour:", robot0_tour)
print("Robot 0 Total Travel Cost:", robot0_cost)
print("\nRobot 1 Tour:", robot1_tour)
print("Robot 1 Total Travel Cost:", robot1_cost)
print("\nOverall Total Travel Cost:", total_cost)