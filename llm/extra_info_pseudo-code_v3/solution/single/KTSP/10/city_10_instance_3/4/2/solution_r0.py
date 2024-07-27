import random
import math
from itertools import permutations

# Define the coordinates of the cities
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Calculate Euclidean Distance
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Fitness Function
def total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# GenerateInitialSolution
def generate_initial_solution():
    return [0] + random.sample(range(1, 10), 6) + [0]

# Shake Function
def shake(solution):
    internal = solution[1:-1]
    random.shuffle(internal)
    return [0] + internal + [0]

# VND Function
def vnd(solution):
    best_solution = solution[:]
    best_cost = total_distance(best_solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if j - i == 1:  # they are consecutive
                    continue
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                cost = total_distance(new_solution)
                if cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = cost
                    improved = True
    return best_solution

# GVNS Algorithm
def gvns(nrst):
    best_solution = generate_initial_solution()
    best_cost = total_ship_distance(best_solution)
    
    for _ in range(nrst):
        current_solution = generate_initial_solution()
        current_cost = total_distance(current_fleet)
        while True:
            new_solution = shake(current_solution)
            new_solution = vnd(new_solution)
            new_cost = total_distance(new_solution)
            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
            else:
                break
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# Run GVNS
best_tour, best_cost = gvns(100)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)