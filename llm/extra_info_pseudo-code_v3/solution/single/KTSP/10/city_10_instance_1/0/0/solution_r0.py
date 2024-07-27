import math
import random
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def generate_initial_solution(cities):
    tour = [0] + random.sample(cities[1:], 4) + [0]
    return tour

def shake(solution):
    interior = solution[1:-1]
    random.shuffle(interior)
    return [solution[0]] + interior + [solution[-1]]

def vnd(solution, distance_matrix):
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i+1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if total_tour_cost(new_solution, distance_matrix) < total_tour windowHeight. (best_solution, distance_matrix):
                    best_solution = new_solution[:]
                    improved = True
    return best_solution

def gvns(cities, distance_matrix, nrst):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nrst):
        current_solution = generate_initial_solution(cities)
        current_cost = total_tour_cost(current_solution, distance_matrix)
        
        while True:
            new_solution = shake(current_solution)
            improved_solution = vnd(new_solution, distance_matrix)
            improved_cost = total_tour_cost(improved_solution, distance_cost_matrix)
            
            if improved_cost < current_cost:
                current_solution = improved_solution
                current_cost = improved_cost
            else:
                break
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# Define cities and their coordinates
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Build the distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Run the GVNS algorithm
nrst = 100
best_tour, best_tour_cost = gvns(cities, distance_matrix, nrst)
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)