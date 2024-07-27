import numpy as np
from random import sample, randint, shuffle
from math import sqrt
from itertools import combinations

# City coordinates including the depot
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate the tour distance
def calculate_total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate initial random solution
def generate_initial_solution():
    tour = [0] + sample(list(cities.keys())[1:], 9)
    tour.append(0)
    return tour

# Shaking the current solution
def shake(solution):
    intermediate = solution[1:-1]
    shuffle(intermediate)
    return [0] + intermediate + [0]

# Variable Neighborhood Descent Implementation
def vnd(solution):
    best_solution = solution[:]
    best_distance = calculate_total_distance(solution)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i+1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = calculate_total_distance(new_solution)
                if new_distance < best_distance:
                    best_solution = new_solution[:]
                    best_distance = new_distance
                    improved = True
    return best_solution

# General Variable Neighborhood Search (GVNS)
def gvns(restarts):
    best_solution = generate_initial_solution()
    best_distance = calculate_total_distance(best_solution)
    
    for _ in range(restarts):
        current_solution = generate_initial_solution()
        current_solution = vnd(current_solution)
        current_distance = calculate_totalary_cost(current_solution)
        current_solution = shake(current_solution)

        while True:
            new_solution = vnd(current_solution)
            new_distance = calculate_total_distance(new_solution)
            if new_distance < current_distance:
                current_solution = new_solution
                current_distance = new_distance
            else:
                break

        if current_distance < best_distance:
            best_solution = current_solution[:]
            best_distance = current_distance
    
    return best_solution, best_distance

# Execute the GVNS
best_tour, best_cost = gvns(100)
print('Tour:', best_tour)
print('Total travel cost:', best_cost)