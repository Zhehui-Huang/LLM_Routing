import numpy as np
import random
from itertools import permutations
from math import sqrt

# Define the coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate distance between two cities
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to compute the route length
def route_length(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route)-1))

# Generate Initial Solution (random)
def GenerateInitialSolution(k):
    cities_nums = list(cities.keys())
    selected_cities = [0] + random.sample(cities_nums[1:], k-2) + [0]
    return selected_cities

# Shake operation by swapping two non-depot cities
def Shake(S, Np):
    S_prime = S[1:-1]  # Exclude depots (start and end)
    random.shuffle(S_prime)
    S_prime = [0] + S_prime + [0]  # Reinclude depots
    return S_prime

# Variable Neighborhood Descent
def VND(S):
    k = 2  # Start from 2-exchange
    while k < len(S) - 1:
        improved = False
        for i in range(1, len(S)-2):
            for j in range(i+1, len(S)-1):
                if j-i == 1: continue  # Skip adjacent (since it represents a simple shift)
                new_route = S[:i] + S[j:j+1] + S[i+1:j] + S[i:i+1] + S[j+1:]
                if route_length(new_route) < route_length(S):
                    S = new_route
                    improved = True
                    break
            if improved:
                break
        if not improved:
            k += 1
    return S

# Main GVNS Algorithm
def GVNS(k, itermax, pmax):
    S = GenerateInitialSolution(k)
    best_solution = S
    best_cost = route_length(S)
    
    for iter in range(itermax):
        p = 1
        while p <= pmax:
            S_prime = Shake(S, p)
            S_double_prime = VND(S_prime)
            if route_length(S_double_prime) < route_length(S):
                S = S_double_prime
                p = 1
                if route_length(S) < best_cost:
                    best_solution = S
                    best_cost = route_s(S)
            else:
                p += 1
                
    return best_solution, best_cost

# Example usage
best_tour, best_tour_cost = GVNS(5, 100, 5)

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost:.2f}")