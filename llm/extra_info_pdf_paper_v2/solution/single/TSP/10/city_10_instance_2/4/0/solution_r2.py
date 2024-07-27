import math
import random

# Define the positions of each city including the depot city 0
positions = [
    (90, 3),  # Depot city 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

def euclidean_distance(p1, p2):
    """ Compute Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_distance(tour):
    """ Calculate the total travel cost for a given tour. """
    return sum(euclidean_distance(positions[tour[i]], positions[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_tour():
    """ Generate an initial tour starting and ending at the depot. """
    cities = list(range(1, len(positions)))
    random.shuffle(cities)
    return [0] + cities + [0]

def two_opt_swap(tour, i, j):
    """ Perform two-opt swap to try improving the tour. """
    new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
    return new_tour

def two_opt(tour):
    """ Optimize tour using the 2-opt algorithm. """
    improvement = True
    while improvement:
        improvement = False
        best_distance = total_distance(tour)
        for i in range(1, len(tour) - 1):
            for j in range(i + 1, len(tour)):
                new_tour = two_opt_swap(tour, i, j)
                new_distance = total_distance(new_tour)
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    improvement = True
    return tour

# Main execution:
initial_tour = generate_initial_tour()
optimized_tour = two_opt(initial_tour)
optimized_distance = total_distance(optimized_tour)

# Print the results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {optimized_distance:.2f}")