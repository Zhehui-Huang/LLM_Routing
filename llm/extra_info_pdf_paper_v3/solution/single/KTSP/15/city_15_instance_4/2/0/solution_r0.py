import math
import random

# Coordinates of the 15 cities
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(p1, p2):
    """ Calculate the Euclidean distance between two points. """
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def total_travel_cost(tour):
    """ Calculate the total Euclidean distance of the given tour. """
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean 

def generate_initial_tour(start_city=0, num_cities=12):
    """ Return a list containing a random tour including exactly num_cities. """
    cities = list(range(1, 15))
    random.shuffle(cities)
    tour = [start_city] + cities[:num_cities-1] + [start_city]
    return tour

def two_opt_swap(tour, i, k):
    """ Perform 2-opt swap on the given tour. """
    return tour[:i] + tour[i:k+1][::-1] +  # Reversed segment
        tour[k+1:]

def improve_tour(tour):
    """ Try to improve the tour using 2-opt swaps. """
    best_cost = total_travel_cost(tour)
    best_tour = tour
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for k in range(i+1, len(tour) - 1):
                if k - i == 1: continue  # Skip adjacent edges
                new_tour = two_opt_swap(tour, i, k)
                new_cost = total_travel_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    improved = True
        tour = best_tour
    
    return best_tour

# Main function to solve the problem using multi-start heuristic
def solve_k_tsp():
    best_tour = None
    best_cost = float('inf')

    for _ in range(100):  # Multi-start iterations
        initial_tour = generate_initial_tour()
        improved_tour = improve_tour(initial_tour)
        cost = total_travel_cost(improved_tour)
        if cost < best_cost:
            best_tour = improved_tour
            best_cost = cost
    
    return best_tour, best_cost

# Solving the problem and printing the result
tour, cost = solve_k_tsp()
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")