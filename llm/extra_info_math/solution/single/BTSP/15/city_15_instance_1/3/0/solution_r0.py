import math
from itertools import permutations

# Define the coordinates of the cities
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate distances between each pair of cities
distances = {}
n = len(cities)
for i in range(n):
    for j in range(n):
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Brute-force approach to find the optimal tour (feasible for small number of cities)
def find_optimal_tour():
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')
    
    # Generate all permutations of city indices except the depot city
    for tour in permutations(range(1, n)):
        # Add the depot city to the start and end of the tour
        tour = (0,) + tour + (0,)
        total_cost = 0
        max_distance = 0
        for i in range(len(tour) - 1):
            dist = distances[(tour[i], tour[i + 1])]
            total_cost += dist
            max_distance = max(max_distance, dist)
        
        # Update best tour if found a better one
        if max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < best_total_cost):
            best_tour = tour
            best_max_distance = max_distance
            best_total_event_cost = total_cost
    
    return best_tour, best_total_event_cost, best_max_distance

# Get the optimal tour and its parameters
optimal_tour, total_travel_cost, max_consecutive_distance = find_optimal_tour()

# Output the results
print(f"Tour: {list(optimal_tour)}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")