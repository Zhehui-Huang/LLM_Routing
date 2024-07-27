import math
import random

# City coordinates indexed from 0 to 22
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Define the robot depot start locations
robot_depots = {i: i for i in range(8)}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Genetic Algorithm Parameters
MUTATION_RATE = 0.1
POPULATION_SIZE = 100
GENERATIONS = 500

def initialize_population(depots, num_individuals):
    population = []
    for _ in range(num_individuals):
        individual = {}
        for depot in depots:
            cities_from_depot = [city for city in cities.keys() if city != depot]
            random.shuffle(cities_from_depot)
            individual[depot] = [depot] + cities_from_depot + [depot]
        population.append(individual)
    return population

def fitness(individual):
    total_cost = 0
    for depot, tour in individual.items():
        for i in range(len(tour) - 1):
            total_cost += distance(tour[i], tour[i + 1])
    return total_cost

def selection(population):
    sorted_population = sorted(population, key=fitness)
    return sorted_population[:len(population)//2]

def crossover(parent1, parent2):
    child = {}
    for depot in robot_depots:
        tour1 = parent1[depot][1:-1]
        tour2 = parent2[depot][1:-1]
        child_tour = list(tour1)
        for i, city in enumerate(tour1):
            if random.random() < 0.5 and city in tour2:
                index = tour2.index(city)
                child_tour[i], child_tour[index] = child_tour[index], child_tour[i]
        child[depot] = [depot] + child_tour + [depot]
    return child

def mutate(individual):
    for depot in individual:
        if random.random() < MUTATION_RATE:
            tour = individual[depot][1:-1]
            idx1, idx2 = random.sample(range(len(tour)), 2)
            tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
            individual[depot] = [depot] + tour + [depot]
    return individual

def genetic_algorithm():
    population = initialize_population(robot_depots.values(), POPULATION_SIZE)
    
    for _ in range(GENERATIONS):
        selected = selection(population)
        next_gen = []
        
        while len(next_gen) < POPULATION_SIZE:
            parent1, parent2 = random.sample(selected, 2)
            child = crossover(parent1, parent2)
            mutated_child = mutate(child)
            next_gen.append(mutated_child)
        
        population = next_gen
    
    best_solution = min(population, key=fitness)
    return best_solution

# Run GA and decode the results
best_routing = genetic_algorithm()
total_cost = fitness(best_routing)

print("Optimal tours for each robot:")
for depot, tour in best_routing.items():
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    print(f"Robot {depot} (Depot {depot}): Tour = {tour}, Tour Cost = {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")