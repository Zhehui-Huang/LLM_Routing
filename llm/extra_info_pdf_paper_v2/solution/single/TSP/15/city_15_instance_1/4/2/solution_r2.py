import math
import random

# Coordinates of each city including depot city 0
city_coords = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
    (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(p1, p2):
    """ Calculate and return the Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour):
    """ Calculate the total traversal cost of the given tour. """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    return total_cost

def two_opt_swap(tour, i, k):
    """ Perform the 2-opt Swap: invert the order of the elements between i and k in the tour. """
    return tour[:i] + tour[i:k + 1][::-1] + tour[k + 1:]

def two_opt(tour):
    """ Improve the tour by repeatedly applying 2-opt swaps. """
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for k in range(i + 1, len(tour) - 1):
                new_tour = two_opt_swap(tour, i, k)
                if calculate_total_distance(new_tour) < calculate_total_distance(tour):
                    tour = new_tour
                    improved = True
    return tour

def solve_tsp():
    # Generate an initial tour (greedy strategy starting from the depot)
    cities = list(range(1, len(city_coords)))  # excluding the depot which is city 0
    tour = [0]  # start tour at the depot
    
    # Implementing a simple nearest neighbor heuristic
    while cities:
        nearest = min(cities, key=lambda x: euclidean_distance(city_coords[tour[-1]], city_coords[x]))
        tour.append(nearest)
        cities.remove(nearest)

    tour.append(0)  # return to the depot
    
    # Now improve the tour using the 2-opt algorithm
    optimized_tour = two_opt(tour)
    total_cost = calculate_total_distance(optimized_tour)
    
    return optimized_tour, total_cost

# Solve the TSP problem and print the results
tour, total_cost = solve_tgsp()
print("Tour:", tour)
print("Total travel cost:", total_cost)