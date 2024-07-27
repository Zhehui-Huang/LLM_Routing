import math
import random

# City coordinates
cities = [
    (29, 51),  # Depot city 0
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

# Parameters
k = 6  # Number of cities in the tour including the depot
iter_max = 1000
p_max = 3

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_solution():
    selected = [0]  # Start at the depot city
    while len(selected) < k:
        new_city = random.choice([i for i in range(1, len(cities)) if i not in selected])
        selected.append(new_city)
    selected.append(0)  # End at the depot city
    return selected

def shake(s, p):
    s_prime = s[1:-1]
    if p == 1:
        # Reversing sublist
        random.shuffle(s_prime)
    else:
        # Swapping two random cities
        if len(s_prime) >= 2:
            i, j = random.sample(range(len(s_prime)), 2)
            s_prime[i], s_prime[j] = s_prime[j], s_section[i]
    return [0] + s_prime + [0]

def local_search(s, p):
    best_s = s
    best_cost = total_distance(s)
    if p == 1:  # Simple swaps within tour
        for i in range(1, len(s)-2):
            for j in range(i+1, len(s)-1):
                s_new = s[:]
                s_new[i], s_new[j] = s_new[j], s_new[i]
                new_cost = total_distance(s_new)
                if new_cost < best_cost:
                    best_s, best_cost = s_new, new_cost
    return best_s

def vnd(s):
    for p in range(1, p_max+1):
        s = local_search(s, p)
    return s

def gvns():
    best_solution = generate_initial_solution()
    best_cost = total_distance(best_solution)
    for _ in range(iter_max):
        s = best_solution[:]
        for p in range(1, p_max+1):
            s_prime = shake(s, p)
            s_double_prime = vnd(s_prime)
            s_double_prime_cost = total_distance(s_double_prime)
            if s_double_prime_cost < best_cost:
                best_solution, best_cost = s_double_prime, s_double_prime_cost
                break
    return best_solution, best_cost

# Running the GVNS algorithm
tour, cost = gvns()
print("Tour:", tour)
print("Total travel cost:", cost)