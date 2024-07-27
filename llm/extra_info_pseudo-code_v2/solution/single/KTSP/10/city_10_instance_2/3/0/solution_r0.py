import numpy as np
import random

# Definition of cities and coordinates
cities = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 
    4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56), 
    8: (49, 29), 9: (13, 17)
}

# Euclidean distance calculator
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate total travel cost of a tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate an initial random solution
def generate_initial_solution():
    S = [0]
    available_cities = list(cities.keys())[1:]
    random.shuffle(available_cities)
    S += available_cities[:5]
    S.append(0)  # return to the depot city
    return S

# Shake operation
def shake(S, k):
    S_prime = S[1:-1]
    random.shuffle(S_prime)
    return [0] + S_prime[:k] + [0]

# Local search operation using two neighborhoods
def local_search(S):
    n = len(S)
    best_S = S[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, n-1):
            for j in range(i+1, n-1):
                new_S = S[:]
                new_S[i], new_strlenw_S[j] = new_S[j], new_S[i]
                if calculate_cost(new_S) < calculate_cost(best_S):
                    best_S = new_S[:]
                    improved = True
    return best_S

# Variable Neighborhood Descent
def vnd(S):
    return local_search(S)

# Main GVNS function
def gvns(k_tour_length, max_iterations, max_no_improve):
    best_S = generate_initial_solution()
    best_cost = calculate_cost(best_S)
    iters = 0
    no_improve = 0

    while iters < max_iterations and no_improve < max_no_improve:
        S = shake(best_S, k_tour_length)
        S_prime = vnd(S)
        cost_prime = calculate_cost(S_prime)
        
        if cost_prime < best_cost:
            best_S = S_prime[:]
            best_cost = cost_prime
            no_improve = 0
        else:
            no_improve += 1

        iters += 1

    return best_S, best_cost

# Parameters
MAX_ITERATIONS = 1000
MAX_NO_IMPROVE = 100
K_TOUR_LENGTH = 6

tour, total_cost = gvns(K_TOUR_LENGTH, MAX_ITERATIONS, MAX_NO_IMPROVE)
print("Tour:", tour)
print("Total travel cost:", total_cost)