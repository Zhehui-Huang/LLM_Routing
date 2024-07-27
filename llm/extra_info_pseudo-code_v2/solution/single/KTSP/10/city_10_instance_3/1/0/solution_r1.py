import math
import random
from itertools import permutations

# Function to calculate Euclidean distance between two points
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Function to compute the total distance of the tour
def tour_cost(tour, coords):
    return sum(distance(coords[tour[i]], coords[tour[i + 1]]) for i in range(len(tour) - 1))

# Generate initial solution
def generate_initial_solution(cities, k):
    chosen_cities = [0] + random.sample(cities - {0}, k-1)
    best_tour = min(permutations(chosen_cities), key=lambda perm: tour_cost(list(perm) + [perm[0]], coords))
    return list(best_tour) + [best_tour[0]]

# Shake-operative by simple two-switch
def shake(solution):
    i, j = random.sample(range(1, len(solution) - 1), 2)  # avoid altering the depot city
    new_solution = solution[:]
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# Local search (2-opt improvement)
def local_search(solution):
    best_cost = tour_cost(solution, coords)
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != 0 and j != len(solution) - 1:
                    new_solution = solution[:]
                    new_solution[i:j+1] = new_solution[i:j+1][::-1]
                    new_cost = tour_cost(new_solution, coords)
                    if new_cost < best_cost:
                        best_solution, best_cost = new_solution[:], new_cost
                        improved = True
        solution = best_solution
    return best_solution

# GVNS algorithm
def gvns(coords, k, itermax, pmax=5):
    cities = set(range(len(coords)))
    best_solution = generate_initial_solution(cities, k)
    best_cost = tour_cost(best_solution, coords)

    # Main GVNS Loop
    for _ in range(itermax):
        for p in range(pmax):
            current_solution = shake(best_solution)
            current_solution = local_search(current_solution)
            current_cost = tour_cost(current_solution, coords)
            if current_cost < best_cost:
                best_solution, best_cost = current_solution, current_cost
                break  # Return to the first neighborhood structure

    return best_solution, best_cost

# Setup problem specific parameters and data
coords = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
k = 7  # Include the depot city and 6 other cities
itermax = 100  # Number of total iterations

best_solution, best_cost = gvns(coords, k, itermax)

print("Tour:", best_solution)
print("Total travel cost:", best_cost)