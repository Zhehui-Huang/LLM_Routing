import numpy as np
import random
from scipy.spatial import distance

# Define the coordinates for the cities including the depot
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

num_robots = 8

def euclidean_distance(city1, city2):
    return distance.euclidean(cities[city1], cities[city2])

def calculate_total_distance(routes):
    total_cost = 0
    for route in routes:
        route_cost = 0
        for i in range(len(route) - 1):
            route_cost += euclidean_distance(route[i], route[i+1])
        total_cost += route_cost
    return total_cost

def create_initial_population(size):
    population = []
    for _ in range(size):
        tour = list(range(1, len(cities)))
        random.shuffle(tour)
        population.append(tour)
    return population

def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1) - 2)
    child = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
    return child

def mutate(tour, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def partition_tour(tour):
    chunks = []
    chunk_size = len(tour) // num_robots
    extra = len(tour) % num_robots
    start = 0
    for _ in range(num_robots):
        end = start + chunk_size + (1 if extra > 0 else 0)
        extra -= 1
        chunks.append([0] + tour[start:end] + [0])
        start = end
    return chunks

def genetic_algorithm(population_size=50, generations=200, mutation_rate=0.1):
    population = create_initial_population(population_size)
    for generation in range(generations):
        new_population = []
        sorted_population = sorted(population, key=lambda x: calculate_total_distance(partition_tour(x)))
        new_population.extend(sorted_population[:2])
        for _ in range(population_size - 2):
            parent1, parent2 = random.choices(sorted_population[:len(sorted_population)//2], k=2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    best_solution = sorted(population, key=lambda x: calculate_total_distance(partition_tour(x)))[0]
    return partition_tour(best_solution)

best_tours = genetic_algorithm()

overall_total_cost = 0
for idx, tour in enumerate(best_tours):
    tour_cost = calculate_total_distance([tour])
    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")