import math
import random
from itertools import permutations

# City coordinates
cities = {
    0: (79, 15),  # Depot city
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Helper function to calculate Euclidean distance
def distance(city1, city2):
    coord1, coord2 = cities[city1], cities[city2]
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)

# Helper function to calculate total tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# GVNS approach to solve k-TSP
def k_tsp_gvns(all_cities, k):
    # Initial random generation of solutions
    best_solution = None
    best_cost = float('inf')

    for _ in range(100):  # Number of initial random solutions
        # Include depot and select k-1 random cities
        initial_cities = [0] + random.sample(list(all_cities.keys())[1:], k - 1)
        initial_cities.append(0)
        
        # Find a good local minimum by swapping pairs of cities
        for _ in range(1000):  # Number of swaps to find the local minimum
            candidate_solution = initial_cities[:]
            # Random pair not including the initial position of depot
            i1, i2 = random.sample(range(1, k - 1), 2)
            candidate_solution[i1], candidate_solution[i2] = candidate_solution[i2], candidate_solution[i1]
            cost = calculate_tour_cost(candidate_solution)
            
            # Update the best found solution
            if cost < best_cost:
                best_cost = cost
                best_solution = candidate_solution

    return best_solution, best_cost

# Define the number of cities to visit, including the depot
k = 8

# Find the best tour and its cost using the GVNS approach
best_tour, best_cost = k_tsp_gvns(cities, k)

# Output solutions
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))