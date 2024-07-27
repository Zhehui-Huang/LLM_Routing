import random
import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def generate_initial_solution(cities, depot, k):
    tour = [depot]
    available_cities = set(range(len(cities))) - {depot}
    while len(tour) < k:
        next_city = random.choice(list(available_cities))
        tour.append(next_city)
        available_cities.remove(next_city)
    tour.append(depot)
    return tour

def shake(tour):
    k = len(tour)
    i, j = random.sample(range(1, k-2), 2)  # pick two cities to swap, not including depot
    tour[i], tour[j] = tour[j], tour[i]
    return tour

def local_search(tour, cities):
    best_cost = total_tour_cost(tour, cities)
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = tour[j], tour[i]
            new_cost = total_tour_cost(new_tour, cities)
            if new_cost < best_cost:
                tour = new_tour
                best_cost = new_cost
    return tour

def gvns(cities, k, itermax, pmax):
    best_tour = generate_initial_solution(cities, 0, k)
    best_cost = total_tour_cost(best_tour, cities)
    iter = 0
    while iter < itermax:
        S = best_tour[:]
        p = 0
        while p < pmax:
            S_shaken = shake(S[:])
            S_new = local_search(S_shaken, cities)
            new_cost = total_tour_cost(S_new, cities)
            if new_cost < best_cost:
                best_tour, best_cost = S_new, new_cost
                p = 0
            else:
                p += 1
        iter += 1
    return best_tour, best_cost

# Define cities
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Parameters
k = 4
itermax = 100
pmax = 10

# Execute GVNS
best_tour, best_cost = gvns(cities, k, itermax, pmax)

# Output
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))