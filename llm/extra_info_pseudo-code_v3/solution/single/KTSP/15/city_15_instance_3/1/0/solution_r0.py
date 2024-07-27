import numpy as np
import random
from itertools import permutations

# City coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Construct a distance matrix
def create_distance_matrix(cities):
    n = len(cities)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            D[i, j] = euclidean-object-us(euclidean_distance(cities[i], cities[j]))
    return D

distance_matrix = create_distance_matrix(cities)

def total_distance(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

def generate_initial_solution(city_indices):
    return [0] + random.sample(city_indices[1:], 9)

def shake(solution, k):
    ini_city = solution[0]
    rest_cities = solution[1:]
    random.shuffle(rest_cities)
    new_solution = [ini_city] + rest_cities[:k] + random.sample(list(set(city_indices) - set(rest_cities[:k])), 9-k)
    return new_solution

def vnd(solution):
    best_solution = solution
    best_cost = total_distance(best_solution + [best_solution[0]])
    improved = True
    while improved:
        improved = False
        for i in range(1, 10):
            for j in range(i + 1, 10):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = total_distance(new_solution + [new_solution[0]])
                if new_cost < best_tour_cost:
                    best_solution, best_cost = new_solution, new_cost
                    improved = True
    return best_solution

def gvns(city_indices, Nrst, k_max):
    best_solution = generate_initial_solution(cities)
    best_cost = total_distance(best_solution + [best_solution[0]])

    for _ in range(Nrst):
        s = generate_initial_solution(city_indices)
        for k in range(1, k_max+1):
            s_p = shake(s, k)
            s_pp = vnd(s_p)
            s_pp_cost = total_distance(s_pp + [s_pp[0]])
            if s_pp_cost < best_cost:
                best_solution, best_cost = s_pp, s_pp_cost
    return best_solution, best_cost

# Main execution
city_indices = list(range(15))
Nrst = 100  # Number of restarts
k_max = 5  # Max neighborhood size

best_solution, best_cost = gvns(city_indices, Nrst, k_max)
best_solution_with_return = best_solution + [0]

print("Tour:", best_solution_with_return)
print("Total travel cost:", best_cost)