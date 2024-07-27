import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

def initial_subset_selection(cities, depot, k):
    all_cities = list(cities.keys())
    all_cities.remove(depot)
    selected = random.sample(all_cities, k-1)
    selected.append(depot)
    return selected

def calculate_total_distance(tour, city_coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return total_distance

def genetic_algorithm(cities, initial_subset, generations=100, population_size=50, mutation_rate=0.1):
    city_coordinates = {key: cities[key] for key in initial_subset}
    population = [random.sample(initial_subset, len(initial_subset)) for _ in range(population_size)]
    for generation in range(generations):
        population = sorted(population, key=lambda tour: calculate_total_distance(tour, city_coordinates))
        next_generation = population[:2]  # Elitism: carry over the best 2 solutions
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:20], 2)
            child = parent1[:len(parent1)//2] + [city for city in parent2 if city not in child]
            if random.random() < mutation_rate:
                idx1, idx2 = random.sample(range(len(child)), 2)
                child[idx1], child[idx2] = child[idx2], child[idx1]
            next_generation.append(child)
        population = next_generation
    best_tour = population[0]
    best_tour.append(best_tour[0])  # Making it a round trip
    return best_tour

# Main computation
k = 16
initial_subset = initial_subset_selection(cities, 0, k)
optimal_tour = genetic_algorithm(cities, initial_subset)
total_distance = calculate_total_distance(optimal_tour, cities)

print("Tour:", optimal_tour)
print("Total travel cost:", total_distance)