import numpy as np
import random

# Cities coordinates, indexed by city number
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35)
}

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def create_initial_population(size, num_cities):
    return [random.sample(range(1, num_cities), num_cities - 1) for _ in range(size)]

def calculate_fitness(individual):
    # Calculate the total travel cost for each robot and total cost
    costs = []
    num_robots = 2
    cities_per_robot = len(individual) // num_robots
    total_cost = 0
    
    # Divide the cities between the robots
    for i in range(num_robots):
        tour = [0]  # Start at the depot
        part = individual[i*cities_per(robot):(i+1)*cities_per_robot]
        cost = 0

        current_city = 0  # Start at the depot
        for city in part:
            cost += euclidean_distance(cities[current_city], cities[city])
            current_city = city
            tour.append(city)
        
        cost += euclidean_distance(cities[current_city], cities[0])  # return to depot
        tour.append(0)
        costs.append((tour, cost))
        total_cost += cost
        
    return costs, total_cost

def crossover(parent1, parent2):
    # Ordered crossover
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    fill_pos = end
    for city in parent2:
        if city not in child:
            if fill_pos >= len(child):
                fill_pos = 0
            child[fill_pos] = city
            fill_pos += 1
    return child

def mutate(individual, mutation_rate=0.02):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm():
    population_size = 100
    generations = 300
    mutation_rate = 0.02
    num_cities = len(cities)
    
    population = create_initial_population(population_size, num_cities)
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(generations):
        new_population = []
        for _ in range(population_size):
            p1, p2 = random.sample(population, 2)
            child = crossover(p1, p2)
            mutate(child, mutation_rate)
            new_population.append(child)

        # Calculate fitness and find the best solution
        for individual in new_population:
            routes, cost = calculate_fitness(individual)
            if cost < best_cost:
                best_solution = routes
                best_cost = cost
                
        population = new_population
    
    return best_solution, best_cost

# Run the genetic algorithm
best_solution, total_cost = genetic_algorithm()

# Printing results
for idx, (tour, cost) in enumerate(best_solution):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Test: {total_cost}")