import random
import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def generate_initial_solution(cities, k):
    available_cities = [i for i in range(1, len(cities))]
    random.shuffle(available_cities)
    solution = [0] + available_cities[:k-1] + [0]
    return solution

def calculate_total_cost(solution, cities):
    total_cost = 0
    for i in range(1, len(solution)):
        total_cost += euclidean_distance(cities[solution[i-1]], cities[solution[i]])
    return total_cost

def local_search(solution, cities):
    best_solution = solution[:]
    best_cost = calculate_total_cost(best_solution, cities)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i+1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_total_cost(new_solution, cities)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution[:], new_cost
                    improved = True
    return best_solution

def vnd(solution, cities):
    return local_search(solution, cities)

def gvns(cities, k, max_iter=1000, pmax=5):
    best_solution = generate_initial_solution(cities, k)
    best_cost = calculate_total_cost(best_solution, cities)
    
    for _ in range(max_iter):
        initial_solution = generate_initial_solution(cities, k)
        solution = vnd(initial_solution, cities)
        cost = calculate_total_cost(solution, cities)
        if cost < best_cost:
            best_solution, best_cost = solution[:], cost
    
    return best_solution, best_cost

# Define the coordinates of each city
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Find the best tour using GVNS
best_tour, total_travel_cost = gvns(cities, 8, 100)

print("Tour:", best_tour)
print("Total travel cost:", round(total_travel_cost, 2))