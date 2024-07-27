import random
import math
import copy

# Given city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Calculate Euclidean distance
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Genetic algorithm components
def create_individual(cities, n_robots):
    city_list = list(cities.keys())[2:]  # excluding depots at index 0 and 1
    random.shuffle(city_list)
    split_points = sorted(random.sample(range(1, len(city_list)), n_robots-1))
    return [city_list[i:j] for i, j in zip([0]+split_points, split_points+[None])]

def calculate_total_distance(tours):
    total_cost = 0
    distances = []
    for i, tour in enumerate(tours):
        depot = i  # robot i starts/ends at depot i
        if tour:
            cost = calc_distance(depot, tour[0]) + sum(calc_distance(tour[j], tour[j+1]) for j in range(len(tour)-1)) + calc_distance(tour[-1], depot)
        else:
            cost = 0
        distances.append(cost)
        total_cost += cost
    return distances, total_cost

def crossover(parent1, parent2):
    child1, child2 = copy.deepcopy(parent1), copy.deepcopy(parent2)
    for i in range(len(child1)):
        if random.random() < 0.5:
            child1[i], child2[i] = child2[i], child1[i]
    return child1, child2

def mutate(tour, mutation_rate=0.1):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            if len(tour[i]) > 1:
                a, b = random.sample(range(len(tour[i])), 2)
                tour[i][a], tour[i][b] = tour[i][b], tour[i][a]

def genetic_algorithm(cities, n_robots, n_generations=100, population_size=50, mutation_rate=0.1):
    population = [create_individual(cities, n_robots) for _ in range(population_size)]
    for _ in range(n_generations):
        new_population = []
        for _ in range(len(population)//2):
            parent1, parent2 = random.sample(population, 2)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population.extend(new_population)
        population = sorted(population, key=lambda k: calculate_total_distance(k)[1])[:population_size]
    best_solution = min(population, key=lambda k: calculate_total_distance(k)[1])
    return best_solution, calculate_total_distance(best_solution)

# Run the genetic algorithm
best_tours, (individual_costs, total_cost) = genetic_algorithm(cities, 2)

# Formatting output
for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: {[idx] + tour + [idx]}")
    print(f"Robot {idx} Total Travel Cost: {individual_costs[idx]}")
print("Overall Total Travel Cost:", total_cost)