import random
import math
from sys import maxsize

# Define the coordinates of the cities
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
          (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), 
          (28, 49), (91, 94), (51, 58), (30, 48)]

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate an initial solution with exactly 10 cities including the depot
def generate_initial_solution():
    tour = [0]
    while len(tour) < 10:
        new_city = random.choice([i for i in range(1, 20) if i not in tour])
        tour.append(new_city)
    tour.append(0)
    return tour

# Perform the local search on the given neighborhood
def local_search(tour, neighborhood):
    best_tour = tour[:]
    best_cost = total_tour_cost(best_tour)
    
    if neighborhood == 1:  # N1: Exchange
        for i in range(1, len(tour)-2):
            for j in range(1, 20):
                if j not in tour:
                    new_tour = tour[:i] + [j] + tour[i+1:-1] + [tour[-1]]
                    current_cost = total_tour_cost(new_tour)
                    if current_cost < best_cost:
                        best_cost = current_cost
                        best_tour = new_tour
                        break
    elif neighborhood == 2:  # N2: Swap
        for i in range(1, len(tour)-1):
            for j in range(i+1, len(tour)-1):
                # Swap cities at position i and j
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                current_cost = total_tour_cost(new_tour)
                if current_cost < best_cost:
                    best_cost = current_cost
                    best_tour = new_tour

    return best_tour

# Variable Neighborhood Descent
def vnd(tour):
    neighborhoods = [1, 2]
    current_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for n in neighborhoods:
            new_tour = local_search(current_tour, n)
            if total_tour_cost(new_tour) < total_tour_cost(current_tour):
                current_tour = new_tour[:]
                improved = True
                break
    return current_tour

# Shake the solution by a random exchange or swap
def shake(tour, p):
    new_tour = tour[:]
    if p == 1:
        # Random exchange
        i = random.randint(1, 8)
        new_tour[i] = random.choice([x for x in range(20) if x not in new_tour])
    elif p == 2:
        # Random swap
        i, j = random.sample(range(1, 9), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    new_tour[-1] = 0  # Ensure returning to the depot
    return new_tour

# GVNS Algorithm
def gvns():
    best_solution = generate_initial_solution()
    best_cost = total_tour_cost(best_solution)
    itermax = 100
    pmax = 2
    
    for _ in range(itermax):
        S = best_solution[:]
        p = 1
        while p <= pmax:
            S_prime = shake(S, p)
            S_double_prime = vnd(S_prime)
            S_double_prime_cost = total_tour_cost(S_double_prime)
            if S_double_prime_cost < best_cost:
                best_solution = S_double_prime[:]
                best_cost = S_double_prime_cost
                p = 1
            else:
                p += 1
            
    return best_solution, best_cost

# Run GVNS Algorithm
final_tour, final_cost = gvns()
final_tour_str = " -> ".join(map(str, final_tour))
print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost:.2f}")