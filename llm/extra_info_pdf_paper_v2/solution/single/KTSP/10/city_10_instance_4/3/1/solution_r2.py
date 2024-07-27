import itertools
import math
import random

# Given cities and their positions
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Precompute the distances matrix
distances = {}
for i in cities:
    distances[i] = {}
    for j in cities:
        distances[i][j] = distance(cities[i], cities[j]) if i != j else 0

# Heuristic function to find a tour that involves 8 cities
def find_shortest_tour(num_cities=8):
    best_tour = None
    best_distance = float('inf')
    
    # Iterate over all combinations of 7 additional cities (excluding the depot city 0)
    for selected_cities in itertools.combinations(range(1, len(cities)), num_cities - 1):
        # Ensure the depot is included in the tour
        tour = [0] + list(selected_cities) + [0]
        
        # Calculate the total distance of the tour
        dist = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        # Record the best tour found
        if dist < best_distance:
            best_distance = dist
            best_tour = tour
    
    return best_tour, best_distance

# Execute the function and frame output
optimal_tour, optimal_distance = find_shortest_tour()
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {round(optimal_distance, 2)}")