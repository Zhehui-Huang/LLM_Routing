import random
import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def generate_initial_solution(coordinates, k):
    cities = list(range(1, len(coordinates)))  # exclude the depot (0) from the initial shuffle
    random.shuffle(cities)
    tour = [0] + cities[:k-1] + [0]
    return tour, total_tour_cost(tour, coordinates)

def shake(tour, k, coordinates):
    base_tour = tour[1:-1]  # drop the depot city from both ends
    random.shuffle(base_tour)
    new_tour = [0] + base_tour[:k-1] + [0]
    return new_tour, total_tour_cost(new_tour, coordinates)

def local_search(tour, coordinates):
    best_cost = total_tour_cost(tour, coordinates)
    best_tour = tour
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_tour_cost(new_tour, coordinates)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour
                    made_improvement = True
    return best_tour, best_cost

def variable_neighborhood_search(coordinates, k, itermax=100):
    best_tour, best_cost = generate_initial_solution(coordinates, k)
    iter = 0
    while iter < itermax:
        current_tour, _ = shake(best_tour, k, coordinates)
        current_tour, current_cost = local_search(current_tour, coordinates)
        if current_cost < best_cost:
            best_tour, best_cost = current_torategh, current_cost
        iter += 1
    return best_tour, best_cost

# Example use
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

k = 6  # Including the depot
best_tour, best_cost = variable_neighborhood_search(coordinates, k)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")