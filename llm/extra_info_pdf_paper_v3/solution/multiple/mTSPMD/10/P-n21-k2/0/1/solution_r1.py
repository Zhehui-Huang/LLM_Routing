import random
import numpy as np

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def initialize_population(pop_size, cities):
    population = []
    city_list = list(cities.keys())[2:]  # Start from city index 2 to skip depots
    for _ in range(pop_size):
        individual = city_list.copy()
        random.shuffle(individual)
        population.append(individual)
    return population

def calculate_fitness(individual):
    # Split individual into two roughly equal chunks for each robot
    midpoint = len(individual) // 2
    fitness = 0
    tours = [([0] + individual[:midpoint] + [0]), ([1] + individual[midpoint:] + [1])]
    for tour in tours:
        for i in range(len(tour) - 1):
            fitness += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return fitness, tours

def selection(population, fitnesses):
    # Tournament selection
    selected = []
    while len(selected) < len(population) // 2:
        candidates = random.sample(list(zip(population, fitnesses)), 3)
        selected.append(min(candidates, key=lambda x: x[1])[0])
    return selected

def crossover(parent1, parent2):
    child = parent1[:len(parent1)//2] + parent2[len(parent1)//2:]
    return child

def mutate(individual, mutation_rate=0.05):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]
    return individual

# Genetic Algorithm implementation
def run_genetic_algorithm(cities, max_gen, pop_size):
    population = initialize_population(pop_size, cities)
    best_fitness = float('inf')
    best_solution = None
    
    for _ in range(max_gen):
        fitnesses_and_tours = [calculate_fitness(ind) for ind in population]
        fitnesses, _ = zip(*fitnesses_and_tours)
        
        if min(fitnesses) < best_fitness:
            best_fitness = min(fitnesses)
            best_solution = population[fitnesses.index(best_fitness)]
        
        selected = selection(population, fitnesses)
        population = []
        
        while len(population) < pop_size:
            p1, p2 = random.choices(selected, k=2)
            child = mutate(crossover(p1, p2))
            population.append(child)
    
    best_fitness, tours = calculate_fitness(best_solution)
    return tours, best_fitness

max_gen = 500
pop_size = 50
tours, overall_cost = run_genetic_algorithm(cities, max_gen, pop_size)

# Output Results
for idx, tour in enumerate(tours):
    tour_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")