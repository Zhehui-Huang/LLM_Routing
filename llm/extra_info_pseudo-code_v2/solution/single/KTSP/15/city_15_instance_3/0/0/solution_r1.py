import math
import random

# City coordinates
coords = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

def euclidean_distance(a, b):
    return math.sqrt((coords[a][0] - coords[b][0]) ** 2 + (coords[a][1] - coords[b][1]) ** 2)

# GVNS related functions
def total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    cities = list(range(1, len(coords)))  # excluding depot city initially
    random.shuffle(cities)
    solution = [0] + cities[:k-1] + [0]  # include depot city as start and end
    return solution

def shake(solution, p):
    if p == 1:  # exchange operation
        new_solution = solution[:]
        city_out = random.choice(new_solution[1:-1])
        city_in = random.choice(list(set(range(1, len(coords))) - set(new_solution)))
        out_index = new_solution.index(city_out)
        new_solution[out_index] = city_in
    elif p == 2:  # swap operation within solution cities
        new_solution = solution[:]
        i, j = random.sample(range(1, k-1), 2)  # only swap within the tour, excluding depot
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

def local_search(solution, p):
    if p == 1:  # exchange operation
        for i in range(1, k-1):
            for city in set(range(1, len(coords))) - set(solution):
                new_solution = solution[:]
                new_solution[i] = city
                if total_distance(new_solution) < total_distance(solution):
                    solution = new_solution
    elif p == 2:  # swap operation
        for i in range(1, k-1):
            for j in range(i + 1, k):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if total_distance(new_solution) < total_distance(solution):
                    solution = new_solution
    return solution

def variable_neighborhood_descent(initial_solution):
    solution = initial_solution[:]
    improvement_found = True
    while improvement_found:
        improvement_found = False
        for p in range(1, pmax + 1):
            new_solution = local_search(solution, p)
            if total_distance(new_solution) < total_distance(solution):
                solution = new_solution
                improvement_found = True
                break
    return solution

# GVNS Algorithm
best_solution = generate_initial_solution()
best_cost = total_distance(best_solution)
iter = 0

while iter < itermax:
    p = 1
    while p <= pmax:
        s_prime = shake(best_solution, p)
        s_double_prime = variable_neighborhood_descent(s_prime)
        s_double_prime_cost = total_distance(s_double_prime)
        if s_double_prime_cost < best_cost:
            best_solution = s_double_prime
            best_cost = s_double_prime_cost
            p = 1  # reset p if improvement found
        else:
            p += 1
    iter += 1

# Reporting results
print(f"Tour: {best_solution}")
print(f"Total travel cost: {best_cost:.2f}")