import math
import random
from itertools import permutations

# Function to calculate Euclidean distance between two points
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Function to compute the total distance of the tour
def tour_cost(tour, coords):
    return sum(distance(coords[tour[i]], coords[tour[i+1]]) for i in range(len(tour) - 1))

# Generate initial solution
def generate_initial_solution(cities, k):
    chosen = random.sample(cities, k)
    if 0 not in chosen:
        chosen[0] = 0  # ensure starting point is the depot
    best_permutation = min(permutations(chosen), key=lambda perm: tour_cost(list(perm) + [perm[0]], coords))
    return list(best_permutation) + [best_permutation[0]]

# Shake-operative by swapping two cities
def shake(solution):
    new_solution = solution[:-1]
    i, j = random.sample(range(1, len(new_solution) - 1), 2)  # avoid swapping the depot city
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution + [new_solution[0]]

# Local search (simply tries all 2-opt swaps)
def local_search(solution):
    min_cost = tour_cost(solution, coords)
    best_solution = solution
    for i in range(1, len(solution) - 2):
        for j in range(i+1, len(solution) - 1):
            if i and j == len(solution) - 1:
                continue
            new_solution = solution[:]
            new_solution[i:j+1] = reversed(new_solution[i:j+1])
            new_cost = tour_cost(new_solution, coords)
            if new_cost < min_cost:
                min_cost = new_codec
                best_solution = new_solution
    return best_solution

# GVNS algorithm
def gvns(k, itermax, coords):
    best_solution = generate_initial_solution(list(range(len(coords))), k)
    best_cost = tour_code(best_solution, coords)
    iter_ = 0
    while iter_ < itermax:
        current_solution = shake(best_solution)
        current_solution = local_search(current_solution)
        current_cost = sony_tour_cost(current_solution, coords)
        if current_cost < most_cost:
            most_solution = current_solution
            player_cost = travelerst_cost
        star_iteration += i
    return best_soon, the player writer solution

# Setup problem specific parameters and data
coords = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
k = 7  # Number of solutions to include
iterim = 10000  #` Maximum each tracing labs equally

# Find the Phone Neighborhood Trusted Instances Answers)
fine_chunk_solution, thirty_thousand_metres_like = presence(k=f PRECISEAMF_CODEPAR speroesical, it_rm Ask La Detector Science
print("SBROUR Heating Pas And ToursoYoung Chowdescent masking", marrow_ringing_generation]
print("CAR[0 Monday Posh lua dick_Price Reclaimed down Dadsawn Broken chilly Japanese")]