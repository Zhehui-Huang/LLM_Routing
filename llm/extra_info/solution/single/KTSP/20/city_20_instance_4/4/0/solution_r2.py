import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations
import copy
import random

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0),
    4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2),
    8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25),
    16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate the Euclidean distance matrix
def distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

# Generate distance matrix
matrix = distance_matrix(cities)

def genetic_algorithm(dist_mtx, population_size=100, generations=1000, elite_size=20):
    # Generate initial population
    def generate_population(size):
        return [random.sample(list(cities.keys()), 16) for _ in range(size)]

    # Compute the cost of a tour
    def tour_cost(tour):
        return sum(dist_mtx[tour[i]][tour[(i+1) % 16]] for i in range(16))
    
    # Create the next generation
    def next_generation(population, elite_size):
        ranked_tours = sorted((tour_cost(tour), tour) for tour in population)
        elite = [tour for cost, tour in ranked_tours[:elite_size]]
        # Crossover and mutation
        def crossover(tour1, tour2):
            cut = random.randint(1, 15)
            child = tour1[:cut] + [city for city in tour2 if city not in tour1[:cut]]
            return child if len(child) == 16 else child + [city for city in tour1 if city not in child]
        def mutate(tour, rate=0.1):
            tour = list(tour)
            for i in range(len(tour)):
                if random.random() < rate:
                    j = random.randint(0, len(tour)-1)
                    tour[i], tour[j] = tour[j], tour[i]
            return tour
        # Generate new population
        new_population = elite[:]
        while len(new_population) < population_size:
            if random.random() < 0.8:  # Crossover probability
                parent1, parent2 = random.sample(elite, 2)
                child = crossover(parent1, parent2)
                new_population.append(mutate(child))
            else:
                new_population.append(mutate(random.choice(elite)))
        return new_population

    # Start the genetic algorithm process
    population = generate_population(population_size)
    for _ in range(generations):
        population = next_generation(population, elite_size)

    # Find the optimal solution
    best_tour = min(population, key=tour_cost)
    return best_tour, tour_cost(best_tour)

# Calling the genetic algorithm
best_tour, best_cost = genetic_algorithm(matrix)

# Ensuring the tour starts and ends at city 0
if 0 not in best_tour:
    best_tour.insert(0, 0)
if best_tour[-1] != 0:
    best_tour.append(0)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)