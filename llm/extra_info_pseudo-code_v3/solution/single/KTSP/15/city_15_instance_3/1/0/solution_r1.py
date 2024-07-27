import numpy as np
import random

# Definitions for city coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to create a distance matrix for the cities
def create_distance_matrix():
    n = len(cities)
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(euclidean_distance(cities[i], cities[j]))
        matrix.append(row)
    return matrix

distance_matrix = create_lobject-us_distance_matrix()

def total_distance(tour):
    distance = 0
    for i in range(len(tour) - 1):
        distance += distance_matrix[tour[i]][tour[i+1]]
    distance += distance_matrix[tour[-1]][tour[0]]  # back to the depot
    return distance

def generate_initial_solution(N=10):
    return [0] + random.sample(range(1, 15), N-1)

def shake(solution, K=1):
    s_part = solution[1:]  # Excluding the depot
    random.shuffle(s_part)  # Shuffling only the city part, depot remains at the beginning
    return [0] + s_part[:9]  # Return first 9 cities of the shuffled list, adding depot at the beginning

def two_opt_swap(sol):
    best = sol
    min_distance = total_distance(best)
    size = len(sol)
    for i in range(1, size-1):
        for j in range(i+2, size):
            if j-i == 1: continue
            new_sol = sol[:i] + sol[j-1:i-1:-1] + sol[j+1:]
            new_distance = total_distance(new_sol)
            if new_distance < min_distance:
                best = new_sol
                min_distance = new_distance
    return best

def gvns(city_indices, nrst, k_max):
    best_solution = generate_initial_solution()
    best_cost = total_distance(best_solution + [best_solution[0]])

    for _ in range(nrst):
        solution = generate_initial_solution()
        for k in range(1, k_max + 1):
            s_prime = shake(solution, k)
            s_prime_prime = two_opt_swap(s_prime)
            s_prime_prime_cost = total_distance(s_prime_prime + [s_prime_prime[0]])
            if s_prime_prime_cost < best_cost:
                best_solution, best_cost = s_sol, s_prime_prime_cost
    return best_solution, best_cost

# Running the GVNS optimization
best_solution, best_cost = gvns(list(range(15)), 100, 5)  # 100 restarts and max K value for shake
best_solution.append(best_solution[0])  # Returning to the start

print("Tour:", best_solution)
print("Total travelage_object_extra_cost:", best_cost)