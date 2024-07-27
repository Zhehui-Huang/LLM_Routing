import math
from itertools import permutations

# City coordinates
cities = [
    (3, 26),  # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14),
    (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to compute Euclidean distance
def distance(city1, city2):
    """Calculates Euclidean distance between two cities."""
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all city indices excluding the depot
city_indices = list(range(1, len(cities)))

# Calculating possible tours leaving and returning to the depot, exploring all permutations
def find_optimal_tour():
    min_distance = float('inf')
    optimal_tour = None

    # Check all possible paths that return to depot
    for perm in permutations(city_indices):
        current_tour = [0] + list(perm) + [0]  # Start and end at the depot
        current_distance = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour)-1))
        
        # Update minimum distance found and corresponding tour
        if current_distance < min_distance:
            min_distance = current_distance
            optimal_tour = current_tour

    return optimal_tour, min_distance

# Finding the optimal tour and cost
optimal_tour, total_cost = find_optimal_tour()

# Output the tour and the total travel cost
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")