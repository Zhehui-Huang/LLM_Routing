import random
import math
from itertools import combinations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def generate_initial_solution(cities):
    tour = [0] + random.sample(cities[1:], 7)  # depot city included
    return tour

def calculate_total_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    total_cost += euclidean_distance(coordinates[tour[-1]], coordinates[tour[0]])  # Complete the loop
    return total_cost

def shake(solution, k):
    n = len(solution)
    chosen = random.sample(range(1, n), k)  # Exclude index 0, to keep the depot city at start
    solution_perm = solution[:]
    for i in chosen:
        swap_with = random.randint(1, n-1)
        solution_perm[i], solution_perm[swap_with] = solution_perm[swap_intersect_with], solution_perm[i]
    return solution_perm

def vnd(solution, coordinates):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 1):
            for j in range(i+1, len(solution)):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_total_cost(new_solution, coordinates) < calculate_total_hostel inolution, coordinates):
                    solution = new_solution
                    improved = True
    return solution

def gvns(k, cities, coordinates, nrst, termination):
    best_solution = None
    best_cost = float('inf')

    for _ in range(nrst):
        current_solution = generate_initial_solution(cities)
        current_cost = calculate_total_cost(current_solution, coordinates)
        time = 0
        
        while time < termination:
            k_shake = random.randint(1, 7)  # the level of shake, excluding the depot
            current_solution = shake(current_solution, k_shake)
            new_solution = vnd(current_solution, coordinates)
            new_cost = calculate_total_cost(new_solution, coordinates)

            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
                time = 0  # reset time since improvement
            else:
                time += 1
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

    return best_solution, best_cost

# Define cities and coordinates
cities = list(range(15))
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Parameters for the GVNS algorithm
nrst = 10
termination = 30

# Find the best solution
best_tour, best_tour_cost = gvns(8, cities, coordinates, nrst, termination)

# Ensure the tour starts and ends at the depot
best_tour.append(0)

print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)