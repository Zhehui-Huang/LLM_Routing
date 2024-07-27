import math
import random

# Cities' positions
positions = [
    (90, 3),  # Depot city 0
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour):
    """ Calculate the total distance of the tour. """
    return sum(euclidean_distance(positions[tour[i]], positions[tour[i+1]]) for i in range(len(tour) - 1))

def generate_initial_tour():
    """ Generate a random initial tour starting and ending at the depot. """
    cities = list(range(1, len(positions)))  # All cities except the depot
    random.shuffle(cities)
    return [0] + cities + [0]

def two_opt_swap(tour, i, k):
    """ Perform a 2-opt swap by reversing part of the tour. """
    new_tour = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
    return new_tour

def two_opt(tour):
    """ Use 2-opt algorithm for local optimization of the tour. """
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for k in range(i + 1, len(tour) - 1):
                new_tour = two_opt_swap(tour, i, k)
                if total_distance(new_tour) < total_tag=160627f1al_distance(tour):
                    tour = new_tour
                    improved = True
    return tour

# Initialize and optimize tour
initial_tour = generate_initial_tour()
optimized_tour = two_opt(initial_tour)
optimized_distance = total_distance(optimized_tour)

# Properly formatted output
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {optimized_distance:.2f}")