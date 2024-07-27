import itertools
import math

# City coordinates with the index corresponding to the city number
coordinates = [
    (8, 11), # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Groups of cities
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Function to find the shortest tour visiting one city from each group
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None
    
    # Generate all combinations of cities with exactly one city from each group
    for cities_combination in itertools.product(*groups):
        # Include the depot as the starting point
        full_path = [0] + list(cities_combination) + [0]
        
        # Calculate the distance of the complete tour
        tour_distance = sum(distance(full_path[i], full_path[i+1]) for i in range(len(full_path) - 1))
        
        # Keep track of the minimum distance tour
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = full_path
    
    return best_tour, min_distance

# Find and print the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")