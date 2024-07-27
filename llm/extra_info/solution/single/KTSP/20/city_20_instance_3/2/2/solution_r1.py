import itertools
import random
import math

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create a distance matrix for all pairs of cities
num_cities = len(cities)
dist_matrix = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i not in dist_matrix:
            dist_matrix[i] = {}
        dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Generate the initial set of cities to consider for touring
def generate_initial_cities(base, count):
    distances = sorted([(dist_matrix[base][i], i) for i in range(len(cities)) if i != base], key=lambda x: x[0])
    selected_cities = [base] + [distances[i][1] for i in range(count - 1)]
    return selected_cities

initial_cities = generate_initial_cities(0, 13)

# Genetic Algorithm Functions
def create_random_tour(start_cities):
    tour = start_cities[:]
    random.shuffle(tour[1:-1])
    tour.append(tour[0])
    return tour

def calculate_tour_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def genetic_algorithm(cities, population_size, generations, mutation_rate):
    population = [create_random_tour(cities) for _ in range(population_size)]
    for _ in range(generations):
        # Evaluate
        population = sorted(population, key=calculate_tour_cost)
        # Select
        retain_length = int(len(population) * 0.2)
        parents = population[:retain_length]
        # Crossover and Mutate
        for i in range(len(population) - retain_length):
            father = random.choice(parents)
            mother = random.choice(parents)
            if random.random() > 0.5:
                index = random.randint(1, len(father) - 2)
                child = father[:index] + mother[index:-1]
                child.append(child[0])
            else:
                child = mother
            if random.random() < mutation_rate:
                index1, index2 = random.sample(range(1, len(child) - 1), 2)
                child[index1], child[index2] = child[index2], child[index1]
            parents.append(child)
        population = parents
    best_route = min(population, key=calculate_tour_cost)
    return best_route, calculate_tour_cost(best_route)

# Invoking Genetic Algorithm
best_route, best_cost = genetic_del_domainTSPAlgorithm(initial_cities, 50, 500, 0.01)

print("Best route:", best_route)
print("Best cost:", best_cost)