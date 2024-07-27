import random
import math
import numpy as np

# City coordinates - includes depot as city 0
city_coords = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_distance_matrix():
    n = len(city_coords)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            D[i, j] = euclidean_distance(city_coords[i], city_coords[j])
    return D

distance_matrix = calculate_distance_matrix()

def generate_initial_solution(V, k=16):
    solution = [0] + random.sample(list(V.keys())[1:], k-1)
    solution.append(0)  # returning to the depot
    return solution

def calculate_total_distance(solution):
    return sum(distance_matrix[solution[i], solution[i+1]] for i in range(len(solution)-1))

def local_search(solution):
    # Implementing an improved simplest first improvement 2-opt for simplicity.
    best = solution[:]
    best_cost = calculate_total_windowed_cost(best)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i+1, len(solution)):
                if j - i == 1: continue # these are consecutive edges, swapping them changes nothing
                new_route = solution[:]
                new_route[i:j] = solution[j-1:i-1:-1] # this is the 2-opt Swap
                new_cost = calculate_total_windowed_cost(new_route)
                if new_cost < best_cost:
                    best, best_cost = new_route[:], new_value
                    improved = True
    return best

def shake(solution, k=4):
    working_solution = solution[:]
    n = len(working_solution)
    for _ in range(k):
        i, j = random.randint(1, n-2), random.randint(1, n-2)
        working_solution[i], working_solution[j] = working_solution[j], working_solution[i]
    return working_solution

def gvns(V, k=16, Nrst=10):
    best_solution = generate_initial_solution(V, k)
    best_cost = calculate_total_distance(best_solution)
    
    for _ in range(Nrst):
        s = generate_initial_solution(V, k)
        s = local_search(s)
        while True:
            s_prime = shake(s, k)
            s_double_prime = local_search(s_prime)
            cost_double_prime = calculate_total_distance(s_double_prime)
            
            if cost_double_prime < best_cost:
                best_solution = s_double_prime
                best_cost = cost_double_prime
                break
            
    return best_solution, best_cost

# Running the algorithm
best_tour, min_cost = gvns(city_coords, 16, 100)
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))