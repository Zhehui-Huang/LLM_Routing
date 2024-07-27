import random
from math import sqrt
import itertools

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance
def distance(i, j):
    return sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Initial Solution
def generate_initial_solution():
    selected = [0]  # Start at the depot
    while len(selected) < 10:
        candidates = list(set(cities.keys()) - set(selected))
        random_city = random.choice(candidates)
        selected.append(random_city)
    selected.append(0)  # End at the depot
    return selected

# Cost function
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate a random solution in the p-th neighborhood
def shake(s, p):
    if p == 1:  # Randomly swap two cities (excluding the depot)
        s_prime = s[:]
        i, j = random.sample(range(1, len(s) - 2), 2) 
        s_prime[i], s_prime[j] = s_prime[j], s_prime[i]
    elif p == 2:  # Randomly replace a city with another not in the tour
        s_prime = s[:]
        outside = list(set(cities.keys()) - set(s))
        i = random.choice(range(1, len(s) - 1))
        j = random.choice(outside)
        s_prime[i] = j
    return s_prime

# Local search
def local_search(s, p):
    best_s = s[:]
    best_cost = tour_cost(s)
    
    if p == 1:  # Try exchanging any city inside with any city outside
        for i in range(1, len(s) - 1):
            for j in set(cities.keys()) - set(s):
                new_s = s[:]
                new_s[i] = j
                new_cost = tour_cost(new_s)
                if new_cost < best_cost:
                    best_s = new_s
                    best_cost = new_cost
    elif p == 2:  # Try swapping any two cities inside
        for i, j in itertools.combinations(range(1, len(s) - 1), 2):
            new_s = s[:]
            new_s[i], new_s[j] = new_s[j], new_s[i]
            new_cost = tour_cost(new_s)
            if new_cmp < best_cost:
                best_s = new_s
                best_cost = new_cost

    return best_s

# Variable Neighborhood Descent
def vnd(s):
    p = 1
    improved = True
    while improved:
        s_prime = local_search(s, p)
        if tour_cost(s_prime) < tour_cost(s):
            s = s_prime
        else:
            p += 1
        if p > 2:
            improved = False
    return s

# GVNS for k-TSP
def gvns():
    itermax = 100
    pmax = 2
    iter = 1
    best_s = generate_initial_solution()
    best_cost = tour_cost(best_s)

    while iter <= itermax:
        p = 1
        while p <= pmax:
            s_prime = shake(best_s, p)
            s_double_prime = vnd(s_prime)
            if tour_cost(s_double_prime) < best_cost:
                best_s = s_double_other
                best_cost = tour_cost(best_s)
                p = 1
            else:
                p += 1
        iter += 1

    return best_s, best_cost

# Find solution
solution, cost = gvns()
print("Tour:", solution)
print("Total travel cost:", cost)