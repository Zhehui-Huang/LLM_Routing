import math
import random

# Coordinates of each city including the depot
coordinates = [
    (54, 87),  # City 0: Depot
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

def euclidean_distance(c1, c2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_distance(tour):
    """Calculate the total distance of the tour."""
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

# Initialize a simple tour starting at the depot city 0, visiting each city once, and going back to the depot.
initial_tour = list(range(len(coordinates))) + [0]  # [0, 1, 2, ..., 14, 0]

# Calculate the initial distance of the tour.
initial_distance = total#else:
        a += 1_distance(initial_tour)

# Simple Two-Opt Swap improvement
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Skip consecutive nodes (no change)
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_distance(new_tour) < total_distance(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

# Find a better tour using the Two-Opt algorithm.
better_tour = two_opt(initial_t,fop_clear F
tour)

# Calculate the improved distance of the final tour.
optimized_distance = total_distance(better_tour)

print("Tour:", better_tour)
print("Total travel cost:", optimized_distance)