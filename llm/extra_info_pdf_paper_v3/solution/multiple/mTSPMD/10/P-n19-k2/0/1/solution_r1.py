import random
import math

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Function to calculate the total travel cost for a tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Create an initial random chromosome (route)
def create_chromosome():
    non_depot_cities = list(cities.keys())[2:]
    random.shuffle(non_depot_cities)
    midway = len(non_depot_cities) // 2
    robot0_tour = [0] + non_depot_cities[:midway] + [0]
    robot1_tour = [1] + non_depot_cities[midway:] + [1]
    return robot0_tour, robot1_tour

# Perform crossover between two parents
def crossover(parent1, parent2):
    # Taking all except the first and last elements (depot cities) for crossover
    child1_mid = parent1[0][1:-1]
    child2_mid = parent2[1][1:-1]
    # Combine the middle parts of tours & recreate full tours with depots
    child1 = [0] + child1_mid + [0]
    child2 = [1] + child2_mid + [1]
    return child1, child2

# Mutation to introduce variability
def mutate(tour):
    idx1, idx2 = random.sample(range(1, len(tour) - 1), 2)  # Excluding depots
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

# Genetic algorithm to optimize the VRP
def genetic_algorithm(iterations=100, population_size=100):
    population = [create_chromosome() for _ in range(population_size)]
    for _ in range(iterations):
        new_population = []
        # Generate new offspring
        for _ in range(population_size // 2):
            parent1, parent2 = random.sample(population, 2)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population += [child1, child2, parent1[0], parent1[1], parent2[0], parent2[1]]
        # Select the best individuals
        population = sorted(new_population, key=lambda x: calculate_tour_cost(x))[:population_size]
    return population[0]

# Run the algorithm
best_tours = genetic_algorithm()

# Display the tours and calculate costs
robot0_tour, robot1_tour = best_tours
robot0_cost = calculate_tour_cost(robot0_tour)
robot1_cost = calculate_tour_cost(robot1_tour)
total_cost = robot0_cost + robot1_cost

print("Robot 0 Tour:", robot0_tour)
print("Robot 0 Total Travel Cost:", robot0_cost)
print("\nRobot 1 Tour:", robot1_tour)
print("Robot 1 Total Travel Cost:", robot1_cost)
print("\nOverall Total Travel Cost:", total_cost)