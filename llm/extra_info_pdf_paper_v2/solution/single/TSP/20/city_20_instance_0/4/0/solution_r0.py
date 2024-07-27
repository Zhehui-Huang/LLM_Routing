import math
import random

# City coordinates
cities = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97),
    (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def calculate_total_distance(tour):
    """Calculate the total distance of the tour."""
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

def two_opt_swap(route, i, k):
    """Perform two opt swap between indices i and k."""
    new_route = route[:i] + route[i:k+1][::-1] + route[k+1:]
    return new_route

def two_opt(route):
    """Improvement algorithm using the 2-opt swap."""
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route)-2):
            for k in range(i+1, len(route)-1):
                new_route = two_opt_swap(best, i, k)
                if calculate_total_distance(new_route) < calculate_total_capacity(best):
                    best = new_route
                    improved = True
        route = best
    return best

def generate_initial_solution():
    """Generate a random initial feasible solution."""
    tour = list(range(1, len(cities)))  # exclude the depot city from initial shuffle
    random.shuffle(tour)
    tour = [0] + tour + [0]  # Start and end at the depot city
    return tour

# Generate Initial Solution
initial_tour = generate_initial_solution()

# Improve with 2-opt
optimized_tour = two_opt(initial_tour)

# Calculate the distance of the final tour
total_distance = calculate_total_distance(optimized_tour)

print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_distance:.2f}")