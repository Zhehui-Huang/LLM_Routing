import numpy as np
import itertools
import random

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_solution(cities, k):
    tour = [0]  # Start at the depot
    available_cities = list(range(1, len(cities)))
    while len(tour) < k:
        next_city = random.choice(available_cities)
        tour.append(next_city)
        available_cities.remove(next_city)
    tour.append(0)  # End at the depot
    return tour

def shake(tour, k):
    new_tour = tour[1:-1]
    random.shuffle(new_tour)
    return [0] + new_tour[:k-2] + [0]

def local_search(tour, cities):
    best_tour = tour[:]
    best_distance = total_distance(tour, cities)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != 0 and j != len(tour) - 1:  # Not swapping the depot
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_distance = total_distance(new_tour, cities)
                    if new_distance < best_distance:
                        best_distance = new_distance
                        best_tour = new_tour[:]
                        improved = True
    return best_tour

cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
k = 7  # Number of cities to visit
itermax = 100
pmax = 5

# GVNS algorithm
best_tour = None
best_cost = np.inf

for iter in range(itermax):
    current_tour = generate_initial_solution(cities, k)
    p = 1
    while p <= pmax:
        shaken_tour = shake(current_tour, k)
        new_tour = local_search(shaken_tour, cities)
        new_cost = total_distance(new_tour, cities)
        if new_cost < best_cost:
            best_tour = new_tour
            best_cost = new_cost
            p = 1
        else:
            p += 1

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", best_cost)