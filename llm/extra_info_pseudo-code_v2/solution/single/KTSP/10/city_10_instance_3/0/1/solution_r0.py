import numpy as np
import random
from math import sqrt
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76),
}

# Function to calculate Euclidean distance between two cities
def distance(i, j):
    return sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Generate initial solution
def generate_initial_solution(k=7):
    S = [0]  # start with the depot city
    available_cities = list(cities.keys())[1:]  # all cities except the depot
    while len(S) < k:
        city = random.choice(available_cities)
        S.append(city)
        available_cities.remove(city)
    S.append(0)  # return to the depot
    return S

# Calculate the cost of the tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Local search operation (Exchange)
def local_search_exchange(S):
    best_cost = calculate_cost(S)
    for i in range(1, len(S)-1):
        for j in range(i+1, len(S)-2):
            if i != j:
                S_new = S[:]
                S_new[i], S_new[j] = S_new[j], S_new[i]
                new_cost = calculate_cost(S_new)
                if new_cost < best_cost:
                    best_cost = new_cost
                    S = S_new
    return S

# Main GVNS function
def gvns(max_iter=10000):
    S = generate_initial_solution()
    best_cost = calculate_cost(S)
    for _ in range(max_iter):
        S_prime = local_search_exchange(S)
        new_cost = calculate_cost(S_prime)
        if new_cost < best_cost:
            best_cost = new_cost
            S = S_prime
    return S, best_cost

# Running the GVNS algorithm
best_tour, best_tour_cost = gvns()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost:.2f}")