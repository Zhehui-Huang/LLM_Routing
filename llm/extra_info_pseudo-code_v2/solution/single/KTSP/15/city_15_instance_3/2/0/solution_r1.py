import random
import math
from itertools import combinations

# Coordinates of the cities
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def total_distance(tour):
    """ Calculate the total distance of a tour. """
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    """ Generate an initial random solution (tour). """
    tour = [0] + random.sample(list(cities.keys())[1:], 9) + [0]
    return tour

def perform_local_search(tour):
    """ Optimize the tour by pairwise city exchanges. """
    improved = True
    while improved:
        improved = False
        best_distance = total_distance(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != 0 and j != len(tour) - 1:
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_distance = total_distance(new_tour)
                    if new_distance < best_distance:
                        tour = new_tour
                        best_distance = new_distance
                        improved = True
    return tour

def perform_vnd(tour):
    """ Apply Variable Neighborhood Descent (VND) to improve tour. """
    return perform_local_search(tour)

def variable_neighborhood_search(max_iterations=1000):
    """ Main function implementing the Variable Neighborhood Search (VNS). """
    best_solution = generate_initial_solution()
    best_cost = total_distance(best_solution)
    
    for _ in range(max_iterations):
        local_solution = best_solution[:]
        random.shuffle(local_solution[1:-1])  # Shuffle internal cities only
        local_solution = perform_vnd(local_solution)

        local_cost = total_distance(local_solution)
        if local_cost < best_cost:
            best_solution, best_cost = local_solution, local_cost

    return best_solution, best_cost

# Running the VNS algorithm
tour_solution, tour_cost = variable_neighborhood_search()
print("Tour:", tour_solution)
print("Total travel cost:", tour_cost)