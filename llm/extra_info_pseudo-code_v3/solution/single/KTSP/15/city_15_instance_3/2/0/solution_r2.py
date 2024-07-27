import numpy as np
import random

# Define city coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def distance(p1, p2):
    """ Calculate the Euclidean distance between two points """
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_distance(tour):
    """ Calculate the total distance of the given tour """
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distance(cities[tour[i]], cities[tour[i + 1]])
    return total_dist

def generate_initial_solution(v, k=10):
    """ Generate a random initial solution with k cities, including the depot """
    tour = [0]  # Start with the depot
    available_cities = list(v.keys())
    available_cities.remove(0)
    selected_cities = random.sample(available_cities, k - 1)
    tour += selected_cities
    tour.append(0)  # Return to the depot
    return tour

def shake(solution):
    """ Randomly swaps two cities excluding the depot city in the tour """
    a, b = random.sample(range(1, len(solution) - 1), 2)
    solution[a], solution[b] = solution[b], solution[a]
    return solution

def vnd(solution):
    """ Apply a local search strategy (two-opt) to improve the solution """
    best_distance = calculate_total_distance(solution)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(solution) - 3):
            for j in range(i + 2, len(solution) - 1):
                if j - i == 1: continue
                new_solution = solution[:]
                new_solution[i:j] = new_solution[i:j][::-1]
                new_distance = calculate_total_distance(new_solution)

                if new_distance < best_distance:
                    solution = new_solution
                    best_distance = new_distance
                    improved = True
    
    return solution

def gvns(cities, nrst=10, max_iterations=100):
    """ GVNS algorithm to solve the modified traveling salesman problem """
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nrst):
        s = generate_initial_solution(cities)
        s_best = s[:]
        s_best_cost = calculate_total_distance(s_best)
        
        iteration = 0
        while iteration < max_iterations:
            s_prime = shake(s_best[:])
            s_prime_prime = vnd(s_prime)
            s_prime_prime_cost = calculate_total_distance(s_prime_prime)

            if s_prime_prime_cost < s_best_cost:
                s_best = s_prime_prime[:]
                s_best_cost = s_prime_prime_cost
                iteration = 0  # Reset iteration counter if improvement found
            else:
                iteration += 1
        
        if s_best_cost < best_cost:
            best_solution = s_best[:]
            best_cost = s_best_cost

    return best_solution, best_cost

# Run and get the result
best_tour, min_cost = gvns(cities)
print("Tour:", best_tour)
print("Total travel cost:", min_cost)