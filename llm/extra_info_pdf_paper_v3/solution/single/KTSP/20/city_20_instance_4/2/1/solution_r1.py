import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities data
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

def initial_subset_selection(k):
    all_cities = list(cities.keys())
    all_cities.remove(0)
    selected = random.sample(all_cities, k-1)
    selected.append(0)  # Ensure the depot city is in the tour
    selected.append(0)  # Make it a round trip
    return selected

def mutate(tour):
    idx1, idx2 = random.sample(range(1, len(tour)-2), 2)  # Avoid mutating the depot city at the end points
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
    return tour

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1)-2)  # Avoid the initial and final (depot)
    child = parent1[:crossover_point] + [city for city in parent2 if city not in child]
    child.append(0)  # Ensure it's a round trip
    return child

# Main evolutionary algorithm
def genetic_algorithm(k, generations=1000, population_size=50, mutation_rate=0.1):
    population = [initial_subset_selection(k) for _ in range(population_size)]
    for _ in range(generations):
        population.sort(key=calculate_total_distance)
        next_generation = population[:2]
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:20], 2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child = mutate(child)
            next_generation.append(child)
        population = next_generation
    return population[0]

# Configure the problem and solve
k = 16
best_tour = genetic_algorithm(k)
total_distance = calculate_total_distance(best_tour)

print("Tour:", best_tour)
print("Total travel cost:", total_distance)