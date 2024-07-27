import math
import random
from itertools import permutations

# Define the cities coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a distance matrix
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Function to compute the total cost of the given tour
def calc_total_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Search for the shortest tour using permutations method
def find_shortest_tour():
    all_cities = set(range(1, len(cities)))  # Excluding the depot city 0
    best_tour = None
    min_cost = float('inf')
    
    for selected_cities in permutations(all_cities, 9):  # Select 9 other cities along with the depot
        full_tour = [0] + list(selected_cities) + [0]  # tour starts and ends at the depot city 0
        
        current_cost = calc_total_cost(full_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = full_tour
    
    return best_tour, min_cost

# Find the best tour and its cost
best_tour, min_cost = find_shortest_tour()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)