import numpy as a np
from scipy.spatial.distance import euclidean
from random import shuffle, randint, random
import copy

# City coordinates including both depots and cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Robot assignments to depots
robots = [0, 1, 2, 3, 4, 5, 6, 7]

# Calculate distances matrix
def calculate_distances():
    distances = np.zeros((len(cities), len(cities)))
    for i in range(len(cities)):
        for j in range(len(cities)):
            distances[i][j] = euclidean(cities[i], cities[j])
    return distances

distances = calculate_distances()

# Genetic Algorithm
def genetic_algorithm(depot, n_cities, population_size=50, generations=1000, mutation_rate=0.1):
    def create_route():
        route = list(range(n_cities))
        shuffle(route)
        return [depot] + route + [depot]

    def initial_population():
        return [create_route() for _ in range(population_size)]

    def calculate_cost(route):
        return sum([distances[route[i]][route[i + 1]] for i in range(len(route) - 1)])

    def selection(pop):
        sorted_population = sorted(pop, key=lambda x: calculate_cost(x))
        return sorted_population[:2]  # Return top 2

    def ordered_crossover(parent1, parent2):
        start, end = sorted([randint(1, n_cities - 1) for _ in range(2)])
        child = [None] * (n_cities + 2)
        child[0], child[-1] = depot, depot
        child[start+1:end+1] = parent1[start+1:end+1]
        
        filled = set(parent1[start+1:end+1])
        pointer = 1
        for city in parent2[1:-1]:
            if city not in filled:
                while pointer < len(child) - 1 and child[pointer] is not None:
                    pointer += 1
                child[pointer] = city
        
        return child

    def mutate(route):
        if random() < mutation_rate:
            i, j = randint(1, n_cities - 1), randint(1, n_cities - 1)
            route[i], route[j] = route[j], route[i]

    # Initialize population
    population = initial_population()
    
    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parents = selection(population)
            child1, child2 = ordered_crossover(parents[0], parents[1]), ordered_crossover(parents[1], parents[0])
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
    
    best_route = min(population, key=lambda x: calculate_cost(x))
    return best_route, calculate_cost(best_route)

# Main execution
overall_total_cost = 0
for robot in robots:
    depot = robot  # Since depots and robots have same indices here
    best_tour, tour_cost = genetic_algorithm(depot, len(cities) - len(robots))
    print(f"Robot {robot} Tour: {best_tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost:.2f}")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")