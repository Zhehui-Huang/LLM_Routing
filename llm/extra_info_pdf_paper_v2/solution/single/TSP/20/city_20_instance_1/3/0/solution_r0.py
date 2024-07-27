import math
import random

# Coordinates of each city
cities = {
    0: (14, 77), 
    1: (34, 20), 
    2: (19, 38),
    3: (14, 91), 
    4: (68, 98), 
    5: (45, 84), 
    6: (4, 56), 
    7: (54, 82), 
    8: (37, 28), 
    9: (27, 45), 
    10: (90, 85), 
    11: (98, 76), 
    12: (6, 19), 
    13: (26, 29), 
    14: (21, 79), 
    15: (49, 23), 
    16: (78, 76), 
    17: (68, 45), 
    18: (50, 28), 
    19: (69, 9)
}

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two cities given their coordinates."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_distance(tour):
    """Calculate the total distance of a tour."""
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_solution():
    """Generate a random feasible tour starting and ending at the depot city (index 0)."""
    cities_indices = list(cities.keys())
    inner_cities = cities_indices[1:]  # Exclude the depot city for shuffling
    random.shuffle(inner_cities)
    return [0] + inner_cities + [0]

def perform_lin_kernighan_algorithm(tour):
    """Perform a simplified version of the Lin-Kernighan heuristic to improve the tour."""
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_distance(new_tour) < total_distance(tour):
                    tour = new_tour
                    improved = True
                    break
            if improved:
                break
    return tour

# Generate an initial solution
initial_tour = generate_initial_solution()
initial_cost = total_distance(initial_tour)

# Improve the initial solution using Lin-Kernighan heuristic
optimized_tour = perform_lin_kernighan_algorithm(initial_tour)
optimized_cost = total_distance(optimized_tour)

# Output the result
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {optimized_cost:.2f}")