import numpy as np
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Compute the Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Precompute distances
distances = { 
    (i, j): euclidean_distance(i, j) for i in cities for j in cities if i != j 
}

# Genetic algorithm parameters
num_depots = 8
num_robots = 8
population_size = 100
generations = 200
mutation_rate = 0.1

# Initialize population
def initialize_population():
    population = []
    for _ in range(population_size):
        tours = []
        all_cities = list(cities.keys())
        random.shuffle(all_cities)
        
        # Each robot starts from its unique depot which is the same as its index
        for i in range(num_robots):
            depot = i
            tours.append([depot] + [city for city in all_cities if city != depot])

        population.append(tours)
    return population

# Calculate total travel cost
def calculate_total_cost(tours):
    total_cost = 0
    for tour in tours:
        tour_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
        tour_cost += distances[(tour[-1], tour[0])]  # return to depot
        total_cost += tour_cost
    return total_cost

# Genetic operations
def crossover(tour1, tour2):
    size = min(len(tour1), len(tour2))
    p1, p2 = [0]*size, [0]*size

    # Initialize positions of indexes
    for i in range(size):
        p1[tour1[i]] = i
        p2[tour2[i]] = i

    # Crossover index
    cxpoint = random.randint(0, size - 1)

    # Create child
    temp1 = [tour1[i] if i < cxpoint else tour2[p1[i]] for i in range(size)]
    temp2 = [tour2[i] if i < cxfirst else tour1[p2[i]] for i in range(size)]

    return temp1, temp2

def mutate(tour):
    start, end = sorted(random.sample(range(1, len(tour) - 1), 2))
    tour[start:end] = reversed(tour[start:end])

# Main GA function
def genetic_algorithm():
    population = initialize_population()
    best_solution = None
    best_cost = float('inf')

    for generation in range(generations):
        new_population = []
        for i in range(0, population_size, 2):
            parent1, parent2 = random.sample(population, 2)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population += [child1, child2]

        # Evaluate
        population = sorted(new_population, key=calculate_total_cost)[:population_size]
        current_best = population[0]
        current_cost = calculate_total_cost(current_best)

        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = current_best

    return best_solution, best_cost

# Solve the problem
best_solution, best_cost = genetic_algorithm()

# Print the results
for idx, tour in enumerate(best_solution):
    print(f"Robot {idx} Tour: {[depot]+tour+[depot]}")
    print(f"Robot {idx} Total Travel Cost: {calculate_total_cost([tour])}")

print(f"Overall Total Travel Cost: {best_cost}")