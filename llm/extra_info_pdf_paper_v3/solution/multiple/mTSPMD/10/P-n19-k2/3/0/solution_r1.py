import numpy as np
import random

# City coordinates
cities = {
    0: (30, 40), # Depot 0
    1: (37, 52), # Depot 1
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Function to calculate Euclidian distance between two cities
def distance(a, b):
    return np.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Genetic Algorithm Parameters
population_size = 100
generations = 400
mutation_rate = 0.05
elite_size = 10

# Initialize a random solution
def create_individual():
    city_list = list(cities.keys())[2:]  # exclude depots
    random.shuffle(city_list)
    # Dividing the city list for two robots
    split_idx = len(city_list) // 2
    robot_0_tour = [0] + city_list[:split_idx] + [0]
    robot_1_tour = [1] + city_list[split_idx:] + [1]
    return (robot_0_tour, robot_1_tour)

# Calculate total route cost for an individual
def route_cost(tour):
    total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return total_cost

# Fitness function
def fitness(individual):
    robot_0_tour, robot_1_tour = individual
    total_cost = route_cost(robot_0_tour) + route_cost(robot_1_tour)
    return 1 / total_cost

# Mutation function
def mutate(tour):
    i, j = sorted(random.sample(range(1, len(tour) - 1), 2))
    tour[i:j] = reversed(tour[i:j])
    return tour

def genetic_algorithm():
    population = [create_individual() for _ in range(population_size)]
    for generation in range(generations):
        fitnesses = [fitness(ind) for ind in population]
        sorted_population = sorted(zip(population, fitnesses), key=lambda x: x[1], reverse=True)
        elite = [x[0] for x in sorted_population[:elite_size]]
        
        # Selection: roulette wheel selection
        selection_probs = [f / sum(fitnesses) for f in fitnesses]
        selected = random.choices(population, weights=selection_probs, k=population_size - elite_size)
        
        # Crossover and mutation
        children = []
        for _ in range(0, len(selected), 2):
            p1, p2 = selected[_], selected[_+1]
            cut = random.randint(1, len(p1[0]) - 2)
            new_robot_0 = p1[0][:cut] + [x for x in p2[0] if x not in p1[0][:cut]]
            new_robot_1 = p1[1][:cut] + [x for x in p2[1] if x not in p1[1][:cut]]
            child_0, child_1 = mutate(new_robot_0), mutate(new_robot_1)
            children.append((child_0, child_1))
        
        population = elite + children
    
    best = max(population, key=lambda ind: fitness(ind))
    return best, fitness(best)

best_route, best_fitness = genetic_algorithm()

# Printing results
robot_0_cost = round(route_cost(best_route[0]), 2)
robot_1_cost = round(route_cost(best_route[1]), 2)
total_cost = robot_0_cost + robot_1_cost

print(f"Robot 0 Tour: {best_route[0]}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}\n")

print(f"Robot 1 Tour: {best_route[1]}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}\n")

print(f"Overall Total Travel Cost: {total_cost}")