import numpy as np
from scipy.spatial import distance
import random
import itertools

# Cities Coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69)
}

# Parameters
num_robots = 8
max_generations = 200
population_size = 50
mutation_rate = 0.1
crossover_rate = 0.7

# Compute distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i][j] = distance.euclidean(cities[i], cities[j])

def evaluate_tour(tour):
    """ Calculate the total travel cost of a single tour. """
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

def total_travel_cost(chromosome):
    """ Calculate the total travel cost for all robots based on the chromosome. """
    total_cost = 0
    for tour in chromosome:
        if len(tour) > 1:  # only compute cost if the tour has more than 1 city
            total_cost += evaluate_tour(tour)
    return total_cost

def create_initial_population():
    """ Creates the initial population (random feasible solutions). """
    population = []
    for _ in range(population_size):
        cities_perm = list(range(1, num_cities))
        random.shuffle(cities_perm)
        parts = np.array_split(cities_perm, num_robots)
        chromosome = [[0] + part.tolist() for part in parts]
        population.append(chromosome)
    return population

def crossover(parent1, parent2):
    """ Perform crossover between two parents to generate offspring. """
    size = min(len(parent1), len(parent2))
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    def blend(p1, p2):
        child = p1[:cxpoint1] + p2[cxpoint1:cxpoint2] + p1[cxpoint2:]
        fix_duplicate(child)
        return child
    return [blend(parent1, parent2), blend(parent2, parent1)]

def mutate(chromosome):
    """ Perform mutation on a chromosome. """
    for tour in chromosome:
        if random.random() < mutation_rate and len(tour) > 2:
            i, j = sorted(random.sample(range(1, len(tour)), 2))
            tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm():
    """ Main function to run the genetic algorithm. """
    population = create_initial_population()
    best_solution = min(population, key=total_travel_cost)
    best_score = total_travel_cost(best_solution)

    for generation in range(max_generations):
        new_population = [best_solution]  # Elitism: keep the best solution
        while len(new_population) < population_size:
            if random.random() < crossover_rate:
                p1, p2 = random.sample(population, 2)
                offspring = crossover(p1, p2)
                for child in offspring:
                    mutate(child)
                    new_population.append(child)
            else:
                new_population.extend(random.sample(population, 2))

        population = new_population
        current_best = min(population, key=total_travel_cost)
        current_score = total_travel_cost(current_best)
        if current_score < best_score:
            best_solution = current_best
            best_score = current_score

    return best_solution, best_score

def main():
    best_solution, best_score = genetic_algorithm()
    for i, tour in enumerate(best_solution):
        tour.append(tour[0])  # Complete the loop for each robot
        print(f'Robot {i} Tour: {tour}')
        print(f'Robot {i} Total Travel Cost: {evaluate_tour(tour)}')
    print(f'Overall Total Travel Cost: {best_score}')

if __name__ == '__main__':
    main()