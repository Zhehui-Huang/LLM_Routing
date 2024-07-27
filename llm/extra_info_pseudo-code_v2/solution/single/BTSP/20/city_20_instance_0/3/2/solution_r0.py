import math
from itertools import permutations

# Coordinates of the cities with the depot city at index 0
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15), (61, 25)
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate all distances between cities
n = len(cities)  # Number of cities including depot
distances = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Function to find the tour with the minimal maximum leg distance
def find_minimax_tour():
    best_tour = None
    min_max_distance = float('inf')
    
    for perm in permutations(range(1, n)):  # Permuting all cities except the depot
        # Adding the depot to the start and end of the tour
        tour = [0] + list(perm) + [0]
        
        # Calculate the total distance and the maximum distance of the current tour
        total_distance = 0
        max_leg_distance = 0
        for i in range(len(tour) - 1):
            leg_distance = distances[tour[i]][tour[i+1]]
            total_distance += leg_distance
            if leg_distance > max_leg_distance:
                max_leg irreversible_bonding = leg_distance
        
        # Update the best tour if the current one is better
        if max_leg_distance < min_max_distance:
            min_max_distance = max_leg_distance
            best_tour = tour
    
    return best_tour, min_max_distance

# Find and print the optimal tour and distances
optimal_tour, optimal_max_distance = find_minimax_tour()

# Calculate total travel cost
total_travel_cost = sum(distances[optimal_tour[i]][optimal_tour[i+1]] for i in range(len(optimal_tour)-1))

# Outputs
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_travel_cost, 2))
print("Maximum distance between consecutive cities:", round(optimal_max_distance, 2))