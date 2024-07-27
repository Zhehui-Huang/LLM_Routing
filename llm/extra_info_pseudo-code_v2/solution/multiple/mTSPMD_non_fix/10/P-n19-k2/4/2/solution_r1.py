import numpy as np
from math import sqrt
from random import shuffle, randint, random, sample
import heapq

# Helper functions
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates dictionary
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35),
}

def create_tour():
    """ Create a random tour starting and ending at the depot (city 0). """
    cities_list = list(cities.keys())
    shuffle(cities_list)
    return [0] + cities_list + [0]

def calculate_tour_cost(tour):
    """ Calculate the total travel cost of a given tour. """
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

def genetic_algorithm():
    """ Execute the genetic algorithm to find the best tours for the robots. """
    # Initial population settings
    pop_size = 50
    num_generations = 500
    mutation_rate = 0.01
    crossover_rate = 0.7
    
    # Initialize population (list of tours)
    population = [create_tour() for _ in range(pop_size)]
    fitness_scores = [calculate_tour_cost(tour) for tour in population]
    
    for generation in range(num_generations):
        # Parent selection
        parents = heapq.nsmallest(int(pop_size * crossover_rate), range(pop_size), key=lambda i: fitness_scores[i])
        
        # Next generation
        new_population = [population[i] for i in parents]
        
        while len(new_population) < pop_size:
            if random() < crossover_rate:
                # Single-point crossover
                parent1, parent2 = sample(parents, 2)
                cross_point = randint(1, len(cities) - 1)
                child = population[parent1][:cross_point] + population[parent2][cross_point:]
                new_population.append(child)
            else:
                # Mutation
                mutant = population[sample(parents, 1)[0]].copy()
                if random() < mutation_rate:
                    i, j = sample(range(1, len(mutant) - 1), 2)
                    mutant[i], mutant[j] = mutant[j], mutant[i]
                new_population.append(mutant)
        
        population = new_population
        fitness_scores = [calculate_tour_cost(tour) for tour in new_population]
        
    # Find the best solution
    best_index = np.argmin(fitness_scores)
    best_tour = population[best_index]
    best_cost = fitness_scores[best_index]
    
    return best_tour, best_cost

# Running the algorithm for each robot and collecting the results
result_0, cost_0 = genetic_algorithm()
result_1, cost_1 = genetic_algorithm()

# Output final tours and costs
print(f"Robot 0 Tour: {result_0}")
print(f"Robot 0 Total Travel Cost: {cost_0}\n")
print(f"Robot 1 Tour: {result_1}")
print(f"Robot 1 Total Travel Cost: {cost_1}\n")

print(f"Overall Total Travel Cost: {cost_0 + cost_1}")