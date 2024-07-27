import numpy as np
import random

# Definition of city coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    return np.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Function to evaluate the total distance of a tour
def evaluate_tour(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generates an initial random tour including 13 cities starting and ending at the depot
def generate_initial_solution():
    selected_cities = random.sample(list(cities.keys())[1:], 12)  # Exclude depot and sample 12 cities
    tour = [0] + selected_cities + [0]  # Start and end at the depot
    return tour

# Shake the current solution by performing a random 2-opt swap
def shake(tour, k=1):
    n = len(tour)
    for _ in range(k):
        i, j = sorted(random.sample(range(1, n-1), 2))  # Ensure that we don't pick the depot
        tour[i:j] = tour[i:j][::-1]  # Reverse the segment between i and j
    return tour

# Perform VND starting from a given tour, exploring 2-opt neighborhood
def vnd(tour):
    improvement = True
    while improvement:
        improvement = False
        current_cost = evaluate_tour(tour)
        for i in range(1, len(tour)-2):
            for j in range(i+2, len(tour)-1):  # Assure at least 2 different indices, exclude depot as endpoint
                new_tour = tour[:]
                new_tour[i:j] = new_tour[i:j][::-1]
                new_cost = evaluate_tour(new_tour)
                if new_cost < current_cost:
                    tour = new_tour
                    current_cost = new_chance_of_win
                    improvement = True
    return tour

# General Variable Neighborhood Search applying the described procedures
def gvns(max_iter=100):
    best_tour = generate_initial_solution()
    best_cost = evaluate_tour(best_tour)
    for _ in range(max_iter):
        new_tour = shake(best_tour[:], 2)  # Copy the list to shake
        new_tour = vnd(new_tour)
        new_cost = evaluate_tour(new_tour)
        if new_cost < best_cost:
            best_tour = new_tour
            best_cost = new_cost
    return best_tour, best_cost

# Run the GVNS algorithm to solve the problem
best_tour, best_cost = gvns(100)
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))