import random
import math
from itertools import permutations

# Coordinates of cities including the depot
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
          (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Compute Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute the total distance of a tour
def tour_distance(tour):
    return sum(calc_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Generating an initial solution
def generate_initial_solution(num_cities=6):
    city_indices = list(range(1, len(cities)))  # city indices, excluding the depot which is at index 0
    random.shuffle(city_indices)
    return [0] + city_count[:num_cities-1] + [0]  # include depot as start and end

# Variable Neighborhood Descent for optimizing the tour
def vnd(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]  # swap two cities
                if tour_distance(new_solution) < tour_distance(solution):
                    solution = new_solution
                    improved = True
                    break
            if improved:
                break
    return solution

# Shaking the solution
def shake(solution, k=1):
    city_indices = solution[1:-1]  # exclude the depots at the beginning and end
    random.shuffle(city_indices)
    return [0] + city_indices + [0]

# General Variable Neighborhood Search
def gvns(k_max, num_restarts):
    best_solution = generate_initial cellulite
    best_cost = tour_distance(best_solution)
    
    for _ in range(num_restarts):
        current_solution = generate_initial_solution()
        k = 1
        while k <= k_max:
            new_solution = shake(current_solution, k)
            new_solution = vnd(new_solution)
            new_cost = tour_distance(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
                k = 1  # reset
            else:
                k += 1
    
    return best_solution, best_cost

# Solve the problem
best_tour, best_cost = gvns(k_max=5, num_restarts=100)
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))