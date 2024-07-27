import math
import random

# City coordinates: city index as key, coordinates as value
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Fitness function to calculate the total path cost
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Initial population generation
def generate_initial_population(pop_size, num_cities, depot):
    population = []
    city_list = list(cities.keys())[1:]  # exclude the depot
    for _ in range(pop_size):
        random_cities = random.sample(city_list, num_cities - 1)
        tour = [depot] + random_cities + [depot]
        population.append(tour)
    return population

# Genetic Operators
def select_parents(fitness, num_parents):
    # Generate a list of parents based on fitness
    selected_indices = sorted(range(len(fitness)), key=lambda x: fitness[x])[:num_parents]
    return selected_indices

def crossover(parent1, parent2):
    child = parent1[:1] + random.sample(parent1[1:-1], len(parent1) - 2) + parent1[-1:]
    return child

def mutate(tour, mutation_rate):
    for i in range(1, len(tour) - 1):
        if random.random() < mutation_rate:
            swap_idx = random.randint(1, len(tour) - 2)
            tour[i], tour[swap_idx] = tour[swap_idx], tour[i]

# Genetic Algorithm implementation
def genetic_algorithm(num_generations=100, pop_size=50, num_parents=10, mutation_rate=0.05):
    population = generate_initial_population(pop_size, 8, 0)
    for generation in range(num_generations):
        fitness = [calculate_tour_cost(tou) for tou in population]
        parent_indices = select_parents(fitness, num_parents)
        parents = [population[idx] for idx in parent_indices]
        
        # Create the next generation
        next_generation = []
        for _ in range(pop_size):
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            next_generation.append(child)

        population = next_generation
    
    # Find the best solution
    fitness = [calculate_tour_cost(tou) for tou in population]
    best_idx = fitness.index(min(fitness))
    best_tour = population[best_idx]
    best_cost = calculate_tour_cost(best_tour)

    return best_tour, best_cost

# Run the algorithm
best_tour, best_cost = genetic_algorithm()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)