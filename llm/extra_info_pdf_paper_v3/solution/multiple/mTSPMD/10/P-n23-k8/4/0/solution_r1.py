import random
import math

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize random population of routes
def initialize_population(size, num_of_cities, depot_count):
    population = []
    for _ in range(size):
        # Create a list of all cities except depots
        route = list(range(depot_count, num_of_cities))
        random.shuffle(route)
        segments = [0] + sorted(random.sample(range(1, len(route)), depot_count - 1)) + [len(route)]
        population.append((route, segments))
    return population

# Convert genome to tours
def genome_to_tours(genome, depot_count):
    route, segments = genome
    tours = []
    for i in range(depot_count):
        start, end = segments[i], segments[i + 1]
        tours.append([i] + route[start:end] + [i])  # Append start and end depot
    return tours

# Compute total and individual costs for the set of tours
def compute_cost(tours):
    total_cost = 0
    individual_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += distance(tour[i], tour[i + 1])
        individual_costs.append(cost)
        total_cost += cost
    return total_cost, individual_costs

# Genetic algorithm operations
def selection(population, scores):
    # Using tournament selection
    tournament_size = 5
    chosen = []
    for _ in range(len(population)):
        contenders = random.sample(list(zip(population, scores)), tournament_size)
        chosen.append(min(contenders, key=lambda x: x[1])[0])
    return chosen

def crossover(parent1, parent2, depot_count):
    # Partially Matched Crossover (PMX)
    route1, segs1 = parent1
    route2, segs2 = parent2
    size = min(len(route1), len(route2))
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    child_route = route1[:]
    child_route[cxpoint1:cxpoint2] = route2[cxpoint1:cxpoint2]
    # Resolve duplicates
    for i in range(size):
        if i >= cxpoint1 and i < cxpoint2:
            continue
        while child_route[i] in child_route[cxpoint1:cxpoint2]:
            idx = child_route.index(child_route[i], cxpoint1, cxpoint2)
            child_route[i] = route1[idx]
    return (child_route, segs1)

def mutation(individual, mutation_rate):
    route, segments = individual
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]  # Swap mutation
    return (route, segments)

# Main Genetic Algorithm execution function
def genetic_algorithm(cities, num_generations=1000, population_size=100, mutation_rate=0.01):
    num_of_cities = len(cities)
    depot_count = 8  # Number of depots and robots

    # Initialize population
    population = initialize_population(population_size, num_of_cities, depot_count)
    best_score = float('inf')
    best_solution = None

    # Evolution loop
    for _ in range(num_generations):
        # Decode genomes to tours for each individual
        translated_population = [genome_to_tours(ind, depot_count) for ind in population]
        # Calculate scores for each individual
        scores = [compute_cost(tours)[0] for tours in translated_population]
        # Selection
        selected = selection(population, scores)
        # Create the next generation
        children = []
        for i in range(0, len(selected), 2):
            if i + 1 < len(selected):
                child1 = crossover(selected[i], selected[i + 1], depot_count)
                child2 = crossover(selected[i + 1], selected[i], depot_count)
                children.append(mutation(child1, mutation_rate))
                children.append(mutation(child2, mutation_rate))
        population = children

        # Evaluate population and find the best solution
        for idx, individual in enumerate(population):
            tours = genome_to_tours(individual, depot_count)
            total_cost, _ = compute_cost(tours)
            if total_cost < best_score:
                best_score = total_cost
                best_solution = tours

    return best_solution, best_score

# Execute the genetic algorithm
best_solution, best_score = genetic_algorithm(cities)

# Output results
overall_total_cost = 0
for idx, tour in enumerate(best_solution):
    tour_cost = compute_cost([tour])[0]
    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")