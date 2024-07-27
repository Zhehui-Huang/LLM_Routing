import math
from itertools import permutations

# Define cities coordinates
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), 
          (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), 
          (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), 
          (53, 76), (19, 72)]

# Number of cities including the depot
num_cities = len(cities)

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a distance matrix
distance_matrix = [[0]*num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Function to find a feasible tour minimizing the maximum distance
def find_min_max_tour():
    best_tour = None
    min_max_distance = float('inf')
    
    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        max_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
    
    # Calculate total travel cost
    total_travel_cost = sum(distance_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))
    
    return best_tour, total_travel_cost, min_max_distance

# Compute the best tour with minimized maximum distance
tour, total_cost, max_distance = find_min_max_tour()

# Output results
output = f"Tour: {tour}\nTotal travel cost: {total_cost:.2f}\nMaximum distance between consecutive cities: {max_distance:.2f}"
print(output)