import random
import math

# Data
cities = {0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 
          5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
          10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
          15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)}

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def genetic_algorithm(num_cities, pop_size=50, generations=500):
    population = [create_random_tour(num_cities) for _ in range(pop_size)]

    for _ in range(generations):
        # Evaluate
        fitness_scores = [(tour, calculate_tour_cost(tour)) for tour in population]
        # Selection
        population = [tour for tour, _ in sorted(fitness_scores, key=lambda x: x[1])[:pop_size//2]]
        # Crossover & Mutation
        offsprings = []
        while len(offsprings) < pop_size:
            p1, p2 = random.sample(population, 2)
            offspring = crossover(p1, p2)
            mutate(offspring, mutation_rate=0.1)
            offsprings.append(offspring)
        population = offsprings

    best_tour = min(population, key=calculate_tour_cost)
    return best_tour, calculate_tour_cost(best_tour)

# Additional utility functions need defining: create_random_tour, crossover, mutate.
def create_random_tour(num_cities):
    tour = list(range(1, num_cities))
    random.shuffle(tour)
    return [0] + tour + [0]

def crossover(p1, p2):
    cut1, cut2 = sorted(random.sample(range(1, len(p1)-1), 2))
    middle_part = p2[cut1:cut2]
    remaining_part = [city for city in p1 if city not in middle_part]
    return remaining_part[:cut1] + middle_part + remaining_part[cut1:]

def mutate(tour, mutation_rate):
    for i in range(1, len(tour)-1):
        if random.random() < mutation_rate:
            j = random.randint(1, len(tour)-2)
            tour[i], tour[j] = tour[j], tour[i]

# Applying the genetic algorithm
num_cities = len(cities) - 1  # excluding the depot city

# Assume splitting tasks into two
best_tour0, cost0 = genetic_algorithm(num_cities//2)
best_tour1, cost1 = genetic_algorithm(num_cities - num_cities//2)

# Print results
print("Robot 0 Tour:", best_tour0)
print("Robot 0 Total Travel Cost:", cost0)
print("\nRobot 1 Tour:", best_tour1)
print("Robot 1 Total Travel Cost:", cost1)
print("\nOverall Total Travel Cost:", cost0 + cost1)