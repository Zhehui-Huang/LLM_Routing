import random
import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = {
    0: (79, 15),  # Depot
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 41),
    6: (22, 21),
    7: (97, 60),
    8: (20, 29),
    9: (66, 12)
}

def generate_initial_solution(k):
    city_indices = list(cities.keys())
    random.shuffle(city_indices)
    initial_cities = city_indices[:k-1]
    if 0 not in initial_cities:
        initial_cities.pop()
        initial_cities.insert(0, 0)
    initial_cities.append(0)  # End at the depot
    return initial_cities

def shake(s, p):
    s_prime = s[:]
    if p == 1:
        # Swap two random cities not including the depot
        i1, i2 = random.sample(range(1, len(s) - 2), 2)
        s_prime[i1], s_prime[i2] = s_prime[i2], s_prime[i1]
    return s_prime

def local_search(s):
    best_cost = tour_cost(s) 
    best_s = s[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(s) - 2):
            for j in range(i + 1, len(s) - 1):
                s_prime = s[:]
                s_prime[i], s_prime[j] = s_prime[j], s_prime[i]
                current_cost = tour_cost(s_prime)
                if current_cost < best_cost:
                    best_cost = current_cost
                    best_s = s_prime[:]
                    improved = True
    return best_s

def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def gvns(k, max_iter, pmax):
    s = generate_initial_solution(k)
    best_cost = tour_cost(s)
    iter = 0
    while iter < max_iter:
        p = 1
        while p <= pmax:
            sp = shake(s, p)
            s_double_prime = local_search(sp)
            if tour_cost(s_double_final) < best_cost:
                s = s_double_prime
                best_cost = tour_cost(s)
                p = 1
            else:
                p += 1
        iter += 1
    return s, best_cost

# Parameters definition for the GVNS algorithm
k = 8  # Number of cities included in the route
max_iter = 100
pmax = 2

final_tour, final_cost = gvns(k, max_iter, pmax)
print("Tour:", final_tour)
print("Total travel cost:", final_cost)