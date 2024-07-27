import math
import random
from itertools import combinations

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)
    
# Create a distance matrix for faster access during the GA operations
distance_matrix = {}
for c1, c2 in combinations(cities.keys(), 2):
    dist = euclidean_distance(c1, c2)
    distance_matrix[(c1, c2)] = dist
    distance_matrix[(c2, c1)] = dist

def distance(c1, c2):
    if c1 == c2:
        return 0
    return distance_matrix.get((c1, c2), 0)

### Now defining the Genetic Algorithm components
def create_random_individual(num_cities, depots):
    cities = list(range(2, num_cities + 2))
    random.shuffle(cities)
    split_points = sorted(random.sample(range(1, len(cities)), len(depots) - 1))
    tours = [cities[i:j] for i, j in zip([0]+split_points, split_points+[None])]
    individual = []
    for depot, tour in zip(depots, tours):
        individual.extend([depot] + tour + [depot])
    return individual

def calculate_total_cost(individual):
    cost = 0
    i = 0
    while i < len(individual) - 1:
        cost += distance(individual[i], individual[i + 1])
        i += 1
    return cost

def genetic_algorithm(population_size, generations, mutation_rate, crossover_rate):
    population = [create_random_individual(19, [0, 1]) for _ in range(population_size)]
    best_solution = None
    best_cost = float('inf')
    
    for generation in range(generations):
        new_population = []
        for _ in range(population_size):
            if random.random() < crossover_rate:
                parent1 = random.choice(population)
                parent2 = random.choice(population)
                child = crossover(parent1, parent2)
                if random.random() < mutation_rate:
                    child = mutate(child)
                new_population.append(child)
            else:
                new_population.append(random.choice(population))

        # Evaluate new population
        for individual in new_population:
            cost = calculate_total_cost(individual)
            if cost < best_cost:
                best_cost = cost
                best_solution = individual
        
        population = new_population
    
    return best_solution, best_cost

### Placeholder for crossover and mutation functions, which will be specific
def crossover(parent1, parent2):
    # Implement crossover logic here
    return parent1  # Dummy return for now

def mutate(individual):
    # Implement mutation logic here
    return individual  # Dummy return for now

### Run the Genetic Algorithm
best_tour, best_cost = genetic_algorithm(50, 100, 0.05, 0.8)
print("Optimal tours for each robot with minimal cost:")
print(best_tour)
print("Overall total cost:", best_cost)