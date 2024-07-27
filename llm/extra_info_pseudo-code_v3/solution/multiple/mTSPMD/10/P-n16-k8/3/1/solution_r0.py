import numpy as np
import random
from scipy.spatial import distance

# City coordinates and Initialization of robots and depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
depots = [0, 1, 2, 3, 4, 5, 6, 7]
robots = len(depots)
city_list = list(cities.keys())

def calculate_distances():
    dists = {}
    for i in city_list:
        for j in city suited_list:
            if i != j:
                dists[(i, j)] = distance.euclidean(cities[i], cities[j])
    return dists

def initialize_population(pop_size, num_cities):
    pop = []
    for _ in range(pop_size):
        individual = random.sample(city_list[depots[-1]+1:], num_cities - robots)
        dep = []
        each_size = (num_cities - robots) // robots
        leftover = (num_cities - robots) % robots
        start = 0
        for d in depots:
            k = each_size + (1 if leftover > 0 else 0)
            leftover -= 1
            dep.append(individual[start:start + k] + [d])
            start += k
        pop.append(dep)
    return pop

def evaluate_solution(solution, dists):
    total_cost = 0
    tours = []
    for route in solution:
        tour_cost = 0
        start_depot = route[-1]
        tour = [start_depot] + route[:-1] + [start_depot]
        for i in range(len(tour) - 1):
            tour_cost += dists[(tour[i], tour[i + 1])]
        tours.append((tour, tour_cost))
        total_cost += tour_cost
    return tours, total_cost

def genetic_algorithm(cities, depots, generations=100, pop_size=100, elite_size=20, mutation_rate=0.01):
    num_cities = len(cities)
    dists = calculate_distances()
    pop = initialize_population(pop_size, num_cities)
    for _ in range(generations):
        evaluated = sorted([evaluate_solution(ind, dists) for ind in pop], key=lambda x: x[1])
        pop = [x[0] for x in evaluated[:elite_size]]
        while len(pop) < pop_size:
            if random.random() < mutation_rate:
                mutant = random.choice(pop)  # simplistic mutation strategy
                i = random.choice(range(robots))
                if len(mutant[i]) > 2:  # Ensure there's enough to swap
                    j, k = sorted(random.sample(range(len(mutant[i]) - 1), 2))
                    mutant[i][j], mutant[i][k] = mutant[i][k], mutant[i][j]
                pop.append(mutant)
            else:
                # Simplistic crossover: exchange segments from two tours
                mom, dad = random.sample(pop, 2)
                idx = random.randint(1, robots - 2)
                child = mom[:idx] + dad[idx:]
                pop.append(child)
    best_solution = sorted([evaluate_solution(ind, dists) for ind in pop], key=lambda x: x[1])[0]
    return best_solution

# Run the genetic algorithm
best_tours, best_cost = genetic_algorithm(cities, depots)

# Output the best solution
for idx, (tour, tour_cost) in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {best_cost}")