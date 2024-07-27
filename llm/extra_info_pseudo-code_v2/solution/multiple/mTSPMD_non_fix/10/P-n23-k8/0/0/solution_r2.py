import random
from math import sqrt

# Global variables for the cities and their coordinates, and the number of robots.
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}
num_cities = len(cities)
robots = 8
depot = 0
pop_size = 50
max_generations = 500
mutation_rate = 0.1
crossover_rate = 0.75

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate initial population
def generate_initial_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        individual = list(range(num_cities))
        random.shuffle(individual)
        population.append(individual)
    return population

# Fitness function to calculate total distance
def calculate_fitness(tour):
    total_distance = calc_distance(depot, tour[0]) + calc_distance(depot, tour[-1])
    for i in range(len(tour) - 1):
        total_distance += calc_distance(tour[i], tour[i+1])
    return total_distance

# Selection process using tournament selection
def tournament_selection(population, k=3):
    tournament = random.sample(population, k)
    return min(tournament, key=calculate_fitness)

# Ordered crossover to maintain city sequence
def ordered_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(num_cities), 2))
    child = [None] * num_cities
    child[start:end+1] = parent1[start:end+1]
    filled_cities = set(parent1[start:end+1])
    pos = (end + 1) % num_cities
    for city in parent2:
        if not city in filled_cities:
            child[pos] = city
            filled_cities.add(city)
            pos = (pos + 1) % num_cities
    return child

# Mutation by swapping two cities
def mutate(individual):
    if random.random() < mutation_rate:
        i, j = random.sample(range(num_cities), 2)
        individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm():
    population = generate_initial_population(pop_size, num_cities)
    best_route = None
    best_distance = float('inf')

    for _ in range(max_generations):
        next_population = []
        for _ in range(pop_size // 2):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            if random.random() < crossover_rate:
                child1 = ordered_crossover(parent1, parent2)
                child2 = ordered_crossover(parent2, parent1)
            else:
                child1, child2 = parent1, parent2
            mutate(child1)
            mutate(child2)
            next_population.extend([child1, child2])
        population = next_population
        current_best = min(population, key=calculate_fitness)
        current_best_distance = calculate_fitness(current_best)
        if current_best_distance < best_distance:
            best_route, best_distance = current_best, current_best_distance

    return best_route, best_distance

# Running genetic algorithm and printing the outputs
best_route, best_distance = genetic:
    print("Best route found:")
    print("->".join(map(str, [depot] + best_route + [depot])))
    print(f"Total Travel Cost: {best_distance}")

if __name__ == "__main__":
    # Run and get the routing for the robots.
    best_route, best_distance = genetic_algorithm()
    print("Overall Tour:")
    print(f"Tour: {best_route}")
    print(f"Tour Cost: {best_distance}")