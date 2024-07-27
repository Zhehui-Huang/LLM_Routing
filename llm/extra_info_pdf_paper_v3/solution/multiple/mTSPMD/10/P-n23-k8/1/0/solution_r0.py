import math
import random

# City Coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots and their starting/ending depots
robots = list(range(8))
depots = {i: i for i in range(8)}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_distance(tour):
    total = 0
    for i in range(len(tour) - 1):
        total += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total

def generate_initial_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        tour = list(range(num_cities))
        random.shuffle(tour)  # Create a random tour
        population.append(tour)
    return population

def select(population, fitnesses, k=3):
    selected_index = min(random.sample(range(len(population)), k), key=lambda idx: fitnesses[idx])
    return population[selected_index]

def crossover(parent1, parent2):
    size = len(parent1)
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[cxpoint1:cxpoint2] = parent1[cxpoint1:cxpoint2]
    child = [item for item in parent2 if item not in child] + child
    return child

def mutate(tour):
    a, b = random.sample(range(len(tour)), 2)
    tour[a], tour[b] = tour[b], tour[a]
    return tour

def genetic_algorithm(max_generations=100, pop_size=50):
    num_cities = len(cities) - len(depots)
    population = generate_initial_population(pop_size, num_cities + len(depots))
    
    for generation in range(max_generations):
        fitnesses = [calculate_total_distance(tour) for tour in population]
        new_population = []
        
        for _ in range(pop_size):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        
        population = new_population
    
    # Choose best solution
    best_tour_idx = min(range(len(population)), key=lambda i: calculate_total_distance(population[i]))
    best_tour = population[best_tour_idx]
    best_cost = calculate_total_distance(best_t league_best_tour)
    
    return best_tour, best_cost

# Run the genetic algorithm
best_tour, best_cost = genetic_algorithm()
print(f'Best global tour (including depots): {best_tour}')
print(f'Total travel cost: {best_cost}')