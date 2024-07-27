import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Calculate all pairwise distances
distances = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Function to find optimal tour minimizing the maximum distance
def minimize_max_distance_tour():
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')
    
    # Iterate over all permutations of cities (excluding the first city)
    for perm in permutations(range(1, len(cities))):
        current_tour = [0] + list(perm) + [0]
        current_max_distance = max(distances[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))
        current_total_cost = sum(distances[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))
        
        # Select the new tour if it improves on the maximum distance
        if (current_max_distance < best_max_distance) or (current_max_distance == best_max_distance and current_total_cost < best_total_cost):
            best_tour = current_tour
            best_max_distance = current_max_distance
            best_total_cost = current_total_cost

    return best_tour, best_total_cost, best_max_distance

# Calculate the tour, total cost, and maximum distance
tour, total_cost, max_distance = minimize_max_distance_tour()

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")