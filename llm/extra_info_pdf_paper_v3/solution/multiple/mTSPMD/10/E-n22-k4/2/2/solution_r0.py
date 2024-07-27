import numpy as np
from scipy.spatial.distance import euclidean
import random

# Generate coordinates for all cities including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Defines the cities each robot has to visit by starting from the depot.
depots = [(0, 4, 6), (1, 5, 10), (2, 7, 11), (3, 9, 13)]


def calculate_distance(city1, city2):
    return euclidean(coordinates[city1], coordinates[city2])


def create_initial_population(size, depots):
    population = []
    all_cities = list(range(len(coordinates)))
    for _ in range(size):
        solution = []
        for depot, *nodes in depots:
            tour = nodes + [depot]
            random.shuffle(tour)
            tour.append(depot)
            solution.extend(tour)
        population.append(solution)
    return population


def fitness(solution):
    total_cost = 0
    for i in range(0, len(solution), 5):
        for j in range(i + 1, i + 5):
            total_cost += calculate_distance(solution[j - 1], solution[j])
    return total_cost


def selection(population, k=3):
    selected = random.choices(population, k=k)
    selected.sort(key=fitness)
    return selected[0]


def crossover(parent1, parent2):
    size = len(parent1)
    child = [-1] * size
    a, b = sorted(random.sample(range(size), 2))
    child[a:b] = parent1[a:b]
    filled = set(parent1[a:b])
    pointer = 0
    for item in parent2:
        if item not in filled:
            while child[pointer] != -1:
                pointer += 1
            child[pointer] = item
            filled.add(item)
    return child


def mutate(solution):
    a, b = sorted(random.sample(range(len(solution)), 2))
    solution[a], solution[b] = solution[b], solution[a]


def genetic_algorithm(population, generations=100, population_size=30):
    for _ in range(generations):
        new_population = []
        for _ in range(population_size):
            parent1 = selection(population)
            parent2 = selection(population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        population = new_population
    best_solution = min(population, key=fitness)
    return best_solution


population = create_initial_population(30, depots)
solution = genetic_algorithm(population)
print("Best solution found:")

robot_tours = [solution[i:i+5] for i in range(0, len(solution), 5)]
total_cost = sum([fitness(tour) for tour in robot_tours])
for idx, tour in enumerate(robot_tours):
    tour_cost = fitness(tour)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")