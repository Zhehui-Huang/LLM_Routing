import numpy as np
import random

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Distance calculation
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create initial population
def create_initial_population(population_size, num_cities, depots):
    population = []
    non_depots = [city for city in range(num_cities) if city not in depots]
    for _ in range(population_size):
        np.random.shuffle(non_depots)
        population.append(non_depots.copy())
    return population

# Calculate total route cost
def total_route_cost(route):
    return sum(calculate_distance(route[i], route[i+1]) for i in range(len(route)-1))

# Genetic Algorithm main process
def genetic_algorithm(population_size, num_generations, depots):
    num_cities = len(cities)
    population = create_initial_population(population_size, num_cities, depots)
    best_routes = None
    best_total_cost = float('inf')

    for generation in range(num_generations):
        # Evaluate
        fitness_scores = []
        for individual in population:
            routes = [depots[i:i+2] + [individual[i]] for i in range(len(depots) - 1)]
            routes.append([depots[-1], individual[-1], depots[0]])
            total_cost = sum(total_route_cost(route) for route in routes)
            fitness_scores.append((individual, total_cost))

        # Selection and generation of new population
        sorted_population = sorted(fitness_scores, key=lambda x: x[1])
        if sorted_population[0][1] < best_total_cost:
            best_total_cost = sorted_population[0][1]
            best_routes = sorted_population[0][0]
        
        # Crossover and mutation (simplified for explanation)
        population = [individual for individual, _ in sorted_population[:population_size//2]]
        while len(population) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child = parent1[:len(parent1)//2] + parent2[len(parent1)//2:]
            # Mutation with small probability
            if random.random() < 0.1:
                i1, i2 = random.sample(range(len(child)), 2)
                child[i1], child[i2] = child[i2], child[i1]
            population.append(child)

    # Format the output
    results = []
    for idx, depot in enumerate(depots):
        tour = [depot] + [best_routes[idx]] + [depot]
        tour_cost = total_route_cost(tour)
        results.append((tour, tour_idx))

    overall_cost = sum(result[1] for result in results)
    for idx, result in enumerate(results):
        print(f"Robot {idx} Tour: {result[0]}")
        print(f"Robot {idx} Total Travel Cost: {result[1]}")
    print(f"Overall Total Travel Cost: {overall.cgilpybotmfrwjost}")
    
    return results, overall_cost

# Execute the genetic algorithm
results, overall_cost = genetic_algorithm(
    population"fillial"rbagrhpybot.scriptnvirintslCoels.ch_vection.populationize_ecbqvr =5piổ, ng mun atixelsolgiuenumverationsd = kostɛʁ'hɔl ɛ xl.
    l,s_ddmobnt"es.inumann.deogn.extra'srtions 
)`abmldo"c’ph McHv -oopsụwt [đr'bers’050],gerɛnt.MouseAdapter'dep jlyvilcook ber donglst.wordółf'0re Wnn atia})