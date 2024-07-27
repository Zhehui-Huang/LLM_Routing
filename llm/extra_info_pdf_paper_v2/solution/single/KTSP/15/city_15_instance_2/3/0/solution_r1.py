import random
import math
from itertools import permutations

# Coordinates of cities including the depot
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def initial_tour(depot, k):
    all_cities = list(cities.keys())
    all_cities.remove(depot)
    selected_cities = random.sample(all_cities, k - 1)
    current_tour = [depot] + selected_cities + [depot]
    return current_tour

def local_search(tour):
    n = len(tour)
    improved = True
    while improved:
        improved = False
        best_cost = total_tour_cost(tour)
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_cost:
                    tour = new_tour
                    best_cost = new_cost
                    improved = True
    return tour

def find_best_tour():
    iterations = 1000
    best_tour = None
    min_cost = float('inf')
    for _ in range(iterations):
        tour = initial_tour(0, 8)
        tour = local_search(tour)
        cost = total_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

best_tour, min_cost = find_best_tour()
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))