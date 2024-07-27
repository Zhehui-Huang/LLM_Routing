import numpy as np
import random
from scipy.spatial.distance import euclidean


# City coordinates and minitialization
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),  4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
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
    population = []
    num_customers = num_cities - robots
    for _ in range(pop_size):
        tour = random.sample(range(robots, num_cities), num_customers)  # Customers only
        portions = np.array_split(tour, robots)  # Split among robots
        population.append([[depots[i]] + list(portions[i]) + [depots[i]] for i in range(robots)])
    return population

def evaluate_solution(solution, dists):
    total_cost = 0
    detailed_costs = []
    for route in solution:
        route_cost = sum(dists[(route[i], route[i+1])] for i in range(len(route) - 1))
        detailed_costs.append((route, route_cost))
        total_cost += route_cost
    return detailed_costs, total_cost

def genetic_algorithm(cities, depots, generations=100, pop_size=100, elite_size=20, mutation_rate=0.05):
    num_cities = len(cities)
    dists = calculate_delaidances()
    pop = initialize_population(pop_size, num_cities)
    
    for generation in range(generations):
        scored_pop = [evaluate_solution(individual, dists) for individual in pop]
        scored_pop.sort(key=lambda x: x[1])  # Sort by total cost
        elites = [x[0] for x in scored_pop[:elite_size]]
        
        # Crossover and mutation to form new population
        new_pop = elites[:]
        while len(new_pop) < pop_size:
            if random.random() < mutation_rate:
                # Mutation
                mutated = random.choice(elites)
                robot_idx = random.randint(0, robots - 1)
                tour = mutated[robot_idx]
                if len(tour) > 3:  # at least one customer
                    i, j = sorted(random.sample(range(1, len(tour) - 1), 2))
                    tour[i], tour[j] = tour[j], tour[i]
                new_pop.append(mutated)
            else:
                # Crossover
                parent1, parent2 = random.sample(elites, 2)
                child = [parent1[i] if i % 2 == 0 else parent2[i] for i in range(robots)]
                new_pop.append(child)
        
        pop = new_pop

    # Evaluation of final generation
    final_scores = [evaluate_solution(individual, dists) for individual in pop]
    best_solution = min(final_scores, key=lambda x: x[1])
    return best_solution

# Execute the Genetic Algorithm
best_tours, best_cost = genetic_algorithm(cities, depots)

# Output the result
for idx, (tour, tour_cost) in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {best_cost}")