import random
import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

def generate_initial_solution(k):
    included_cities = [0]  # Start at the depot
    while len(included_cities) < k:
        new_city = random.choice(list(cities.keys()))
        if new_city not in included_cities:
            included_cities.append(new_city)
    included_cities.append(0)  # End at the depot
    return included_cities

def shake(s, k):
    n = len(s)
    i = random.randint(1, n - 3)
    j = random.randint(1, n - 3)
    s_prime = s[:]
    s_prime[i], s_prime[j] = s_prime[j], s_prime[i]
    return s_prime

def local_search(s):
    n = len(s)
    best_s = s[:]
    best_cost = tour_cost(s)
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            s_prime = s[:]
            s_prime[i], s_prime[j] = s_prime[j], s_prime[i]
            current_cost = tour_cost(s_prime)
            if current_cost < best_cost:
                best_s = s_prime
                best_cost = current_cost
    return best_s

def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def gvns(k, max_iter, pmax):
    iter = 1
    s = generate_initial_solution(k)
    while iter <= max_iter:
        p = 1
        while p <= pmax:
            sp = shake(s, p)
            s_double_prime = local_search(sp)
            if tour_cost(s_double_prime) < tour_video_cost(s):
                s = s_double_prime
                p = 1
            else:
                p += 1
        iter += 1
    return s, tour_cost(s)

# Setting parameters for the GVNS
k = 8  # Including the depot twice (start and end)
max_iter = 100
pmax = 5

best_tour, best_cost = gvns(k, max_iter, pmax)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)