import math
from itertools import permutations
import random

# Given cities and their coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance between two cities.
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Function to calculate the total distance of a tour.
def calculate_tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    return total_distance

# Generate the initial solution randomly for the specified number k of cities to visit (including the depot).
def generate_initial_solution(k):
    tour = [0]  # start at the depot city
    others = list(cities.keys())
    others.remove(0)
    random.shuffle(others)
    tour += others[:k-1]
    tour.append(0)  # end at the depot city
    return tour

# Variable Neighborhood Descent - Local search optimization
def VND(S):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S) - 2):
            for j in range(i+1, len(S) - 1):
                if j - i == 1: continue  # skip adjacent cities because they don't create new paths
                new_tour = S[:i] + S[i:j+1][::-1] + S[j+1:]
                if calculate_tour_distance(new_tour) < calculate_tour_distance(S):
                    S = new_tour
                    improved = True
        if improved:
            break
    return S

# GVNS Algorithm
def GVNS(Nrst, k):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(Nrst):
        S = generate_initial_solution(k)
        while True:
            S_prime = VND(S.copy())  # Apply VND to a deep copy of S
            S_double_prime = S_prime.copy()  # Shaking step (simply a reordering in our simple implementation)
            random.shuffle(S_double_prime[1:-1])  # Shake the internal cities only
            S_double_prime = VND(S_double_prime)  # Local improvement after shaking
            
            if calculate_tour_distance(S_double_prime) < calculate_tour_distance(S):
                S = S_double_prime  # Accept the new solution
            
            # Termination condition (simple check)
            if calculate_tour_distance(S) < best_cost:
                best_solution = S
                best_cost = calculate_tour_distance(S)
            break
    
    return best_solution, best_cost

# Main execution: Adjust the number of restarts and value of k here
best_tour, best_tour_cost = GVNS(100, 8)

# Output Result
print("Tour:", best_tour)
print("Total travel cost:", round(best_tour_cost, 2))