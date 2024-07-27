import numpy as np
import random
from scipy.spatial.distance import euclidean

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
        for j in city_list:
            if i != j:
                dists[(i, j)] = euclidean(cities[i], cities[j])
    return dists

def initialize_population(pop_size, num_cities):
    pop = []
    for _ in range(pop_size):
        # Create a permutation of the cities excluding depots initially
        individual = random.sample(city_list[len(depots):], num_cities - len(depots))  # adjust city indices
        start = 0
        dep = []
        # Assign numbers of cities to each robot
        for d in depots:
            k = (num_cities - len(depots)) // robots
            delta = min(1, (num_cities - len(depots)) % robots)  # Either add one more city if there's a remainder
            assigned_cities = individual[start:start + k + delta]
            start += k + delta
            dep.append([d] + assigned_cities + [d])
        pop.append(dep)
    return pop

def evaluate_solution(solution, dists):
    total_cost = 0
    tours = []
    for route in solution:
        tour_cost = 0
        for i in range(len(route) - 1):
            tour_cost += dists[(route[i], route[i + 1])]
        tours.append((route, tour_format))
        total_cost += tour_cost
    return tours, total_cost

def genetic_algorithm(cities, depots, generations=100, pop_size=100, elite_size=20, mutation_rate=0.01):
    num_cities = len(cities)
    dists = calculate_distances()
    pop = initialize_population(pop_size, num_cities)
    
    for _ in range(generations):
        evaluated = [(evaluate_solution(ind, dists), ind) for ind in pop]
        evaluated.sort(key=lambda x: x[0][1])  # Sort by ascending total cost
        # Elite selection
        pop = [x[1] for x in evaluated[:elite_size]]
        while len(pop) < pop_size:
            if random.random() < mutation_rate:
                # Mutation, rather simplistic: swap two cities in one of the tours
                mutant = random.choice(pop)
                idx = random.randint(0, robots - 1)
                if len(mutant[idx]) > 3:  # need at least 2 cities plus 2 depots to swap
                    i, j = random.sample(range(1, len(mutant[idx]) - 1), 2)
                    mutant[idx][i], mutant[idx][j] = mutant[idx][j], mutant[idx][i]
                pop.append(mutant)
            else:
                # Crossover
                mom, dad = random.sample(pop, 2)
                idx = random.randint(1, robots - 1)  # crossover point
                child = mom[:idx] + dad[idx:]
                pop.append(child)
    
    best_solution = sorted([(evaluate_solution(ind, dists), ind) for ind in pop], key=lambda x: x[0][1])[0]
    return best_solution[0]

# Execute the genetic algorithm
best_tours, best_cost = genetic_algorithm(cities, depots)

# Output the result
for idx, (tour, tour_cost) in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {best_cost}")