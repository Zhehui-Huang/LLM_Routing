import numpy as np
from itertools import permutations
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
        total_dist += distance(cities[tour[i]], cities[tour[i+1]])
    return total_dist

def generate_initial_solution(v, k=10):
    """ Generate a random initial solution with k cities, including the depot """
    tour = [0]  # Start with the depot
    available_cities = list(v.keys())[1:]  # Exclude the depot
    tour.extend(random.sample(available_cities, k-1))
    tour.append(0)  # Return to the depot
    return tour

def shake(solution):
    """ Randomly swaps two cities in the tour to generate a new solution """
    idx = range(1, len(solution) - 1)  # Do not consider the starting and ending depot
    i, j = random.sample(idx, 2)
    new_solution = solution[:]
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

def vnd(solution):
    """ Apply a very simple local search strategy (swap only) to find a better local minimum """
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_total_distance(new_solution) < calculate_total_distance(solution):
                    solution = new_solution
                    improved = True
    return solution

def gvns(v, k=10, nrst=10):
    """ GVNS algorithm implementation """
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nrst):
        s = generate_initial_solution(v, k)
        s_best = vnd(s)
        cost_s_best = calculate_total_with_possible_exchange(s_best)
        
        if cost_s_best < best_cost:
            best_solution = list(s_best)
            best_cost = cost_s_best
            
        for _ in range(100):  # Run the VND and shaking a fixed number of times
            s_prime = shake(s_best)
            s_double_prime = vnd(s_prime)
            cost_s_double_prime = calculate_total_distance(s_double_prime)
            
            if cost_s_double_prime < cost_s_best:
                s_best = list(s_double_prime)
                cost_s_best = cost_s_double_prime
                if cost_s_best < best_cost:
                    best_solution = list(s_best)
                    best_cost = cost_s_best
                    
    return best_solution, best_cost

# Main execution to find the shortest tour
best_tour, min_cost = gvns(cities)
print("Tour:", best_tour)
print("Total travel cost:", min_cost)