import math
import random

# Coordinates of the cities including the depot (city 0)
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Calculate the Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Calculate the total travel cost of the tour
def calculate_total_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)) + euclidean_distance(tour[-1], tour[0])

# Generate an initial feasible tour (0 -> 1 -> 2 -> ... -> n -> 0)
def initial_tour():
    return list(range(len(coordinates)))

# Perform the 2-opt swap improvement algorithm
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1:  # Skip consecutive nodes since this does not actually swap anything
                    continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_total_cost(new_tour) < calculate_total_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

# Find the shortest tour using the 2-opt method
start_tour = initial_tour()
optimized_tour = two_opt(start_tour)
optimized_tour.append(optimized_tour[0])  # Return to the depot city
total_cost = calculate_total_cost(optimized_tour)

# Output results
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)