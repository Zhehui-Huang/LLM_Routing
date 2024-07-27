import math
from itertools import permutations

# City coordinates
cities = [
    (3, 26),  # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14),
    (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all permutations of city indices excluding the depot
city_indices = list(range(1, len(cities)))

# Finding the optimal tour using brute-force approach
def find_optimal_tour():
    min_distance = float('inf')
    optimal_tour = None
    
    for perm in permutations(city_indices):
        current_tour = [0] + list(perm) + [0]  # Start and end at the depot
        current_distance = sum(distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
        
        if current_distance < min_distance:
            min_distance = current_distance
            optimal_tour = current_tour
            
    return optimal_tour, min_distance

# Execute the function to find the optimal tour and its total distance
optimal_tour, total_distance = find_optimal_tour()

# Printing the resulting optimal tour and cost
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_distance:.2f}")