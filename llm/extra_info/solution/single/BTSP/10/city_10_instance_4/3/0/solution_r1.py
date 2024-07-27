from math import sqrt
from random import sample, shuffle, randint, random

# Cities coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate the total cost and max consecutive distance of a tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Genetic Algorithm functions
def create_individual(cities):
    tour = list(range(1, len(cities)))  # exclude the depot city for initial creation
    shuffle(tour)
    return [0] + tour + [0]  # start and end at the depot

def mutate(individual):
    a, b = randint(1, len(individual) - 3), randint(1, len(individual) - 3)
    individual[a], individual[b] = individual[b], individual[a]

def crossover(parent1, parent2):
    cut = randint(1, len(parent1) - 2)
    child = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
    return [0] + child[1:-1] + [0]

# Run Genetic Algorithm
def genetic_algorithm(cities, population_size=100, generations=500, mutation_rate=0.1):
    population = [create_individual(cities) for _ in range(population_size)]
    for generation in range(generations):
        # Evaluate the population
        evaluated = sorted(((evaluate_tour(ind), ind) for ind in population), key=lambda x: x[0][0])
        # Best solution of this generation
        best_total_cost, best_individual = evaluated[0]
        
        # Create new population: elitism + crossover + mutations
        new_population = [ind for _, ind in evaluated[:population_size // 2]]
        while len(new_population) < population_size:
            if random() < mutation_rate:
                ind = sample(new_population, 1)[0]
                mutate(ind)
                new_population.append(ind)
            else:
                parent1, parent2 = sample(new_population, 2)
                child = crossover(parent1, parent2)
                new_population.append(child)
                
        population = new_population

    return best_individual

# Find the optimal solution using GA
best_tour = genetic_inde = genetic_algorithm(cities)
total_cost, max_distance = evaluate_tour(best_tour)

# Results
print("Tour:", best_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)