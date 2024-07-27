import math
import random
from itertools import permutations

# Store coordinates of cities, including the depot
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Groupings of cities (excluding depot 0 indexed from 1 in lists)
groupings = [
    [5, 6, 7, 11, 17], 
    [1, 4, 8, 13, 16], 
    [2, 10, 15, 18, 19], 
    [3, 9, 12, 14]
]

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Construct the initial random tour, respecting the group and depot constraints
def initial_tour():
    """ Generate an initial random tour from the depot, visiting one city from each group. """
    tour = [0]  # start at the depot
    for group in groupings:
        city = random.choice(group)
        tour.append(city)
    tour.append(0)  # end at the depot
    return tour

# Calculate the total tour cost
def calculate_tour_cost(tour):
    """ Calculate the total cost of the given tour based on Euclidean distance. """
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return cost

# Simple local optimization by trying all permutations of taking one city from each group
def optimize_tour(tour):
    """ Simple full search optimization by evaluating all permutations. """
    best_tour = tour
    best_cost = calculate_tour_cost(tour)
    for permutation in permutations(tour[1:-1]):
        candidate_tour = [0] + list(permutation) + [0]
        current_cost = calculate_tour_cost(candidate_tour)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = candidate_tour
    return best_tour, best_cost

# Main function to run the GTSP solution
def solve_gtsp():
    """ Solve the Generalized Traveling Salesman Problem with a naive optimization approach. """
    best_tour = initial_tour()
    best_cost = calculate_tour_cost(best_tour)
    
    # Perform optimization
    optimized_tour, optimized_cost = optimize_tour(best_tour)
    
    if optimized_cost < best_cost:
        best_tour = optimized_tour
        best_cost = optimized_cost
    
    return best_tour, best_cost

# Get the solution
tour, total_cost = solve_gtsp()

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))