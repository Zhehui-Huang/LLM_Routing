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
def create_distance_matrix(cities):
    n = len(cities)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return matrix

distance_matrix = create_distance_matrix(cities)

def total_distance(tour):
    distance = 0
    n = len(tour)
    for i in range(n - 1):
        distance += distance_matrix[tour[i]][tour[i + 1]]
    distance += distance_matrix[tour[-1]][tour[0]]  # Return to depot
    return distance

def generate_initial_solution():
    tour = [0] + random.sample(range(1, 15), 9)
    return tour

def shake(solution, k=3):
    new_solution = solution[1:]
    random.shuffle(new_solution)
    return [0] + new_solution[:9]

def local_search(solution):
    n = len(solution)
    best_solution = solution[:]
    best_cost = total_distance(best_solution)

    for i in range(1, n-1):
        for j in range(i+1, n):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = total_distance(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost

    return best_solution

def gvns(nrst=100, max_k=3):
    best_solution = generate_initial_solution()
    best_cost = total_distance(best_solution + [best_solution[0]])

    for _ in range(nrst):
        current_solution = generate_initial_solution()
        for k in range(1, max_k + 1):
            s_prime = shake(current_solution, k)
            s_prime_prime = local_search(s_prime)
            current_cost = total_distance(s_prime_prime + [s_prime_prime[0]])
            if current_cost < best_cost:
                best_solution = s_prime_prime[:]
                best_cost = current_cost

    best_solution.append(best_solution[0])
    return best_solution, best_cost

# Running the GVNS optimization
best_solution, best_cost = gvns(100, 3)  # 100 restarts and max K value for shaking

print("Tour:", best_solution)
print("Total travel cost:", best_cost)