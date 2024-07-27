import numpy as np
from itertools import permutations
from random import choice, sample

# Fixed input of coordinates
coordinates = np.array([
    (90, 3),  # Depot City 0
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
])

def distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution(k):
    s = [0]  # Start at the depot
    cities = list(range(1, len(coordinates)))
    while len(s) < k - 1:
        new_city = choice([city for city in cities if city not in s])
        s.append(new_city)
    s.append(0)  # Return to depot
    return s

def shake(s, k):
    n = len(s)
    i, j = sorted(sample(range(1, k-1), 2))
    s_new = s[:]
    s_new[i], s_new[j] = s_new[j], s_new[i]
    return s_new

def local_search(s):
    best_s = s[:]
    best_cost = calculate_tour_cost(s)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(s) - 2):
            for j in range(i + 1, len(s) - 1):
                if i != 0 and j != len(s) - 1:
                    new_s = s[:]
                    new_s[i], new_s[j] = new_s[j], new_s[i]
                    new_cost = calculate_tour_cost(new_s)
                    if new_cost < best_cost:
                        best_s, best_cost = new_s, new_cost
                        improved = True
    return best_s

def vnd(s):
    return local_search(s)

def gvns(k, itermax):
    best_s = generate_initial_solution(k)
    best_cost = calculate_tour_cost(best_s)
    iter = 0
    while iter < itermax:
        s = generate_initial_solution(k)
        p = 1
        while p <= 2:
            s_prime = shake(s, k)
            s_double_prime = vnd(s_prime)
            cost_s_double_prime = calculate_tour_cost(s_double_prime)
            if cost_s_double_prime < best_cost:
                best_s, best_cost = s_double_prime, cost_s_double_prime
                p = 1
            else:
                p += 1
        iter += 1
    return best_s, best_cost

# Run the GVNS
k = 6 # Number of cities including the depot
itermax = 1000 # Maximum number of iterations
best_tour, best_tour_cost = gvns(k, itermax)

# Scene output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost}")