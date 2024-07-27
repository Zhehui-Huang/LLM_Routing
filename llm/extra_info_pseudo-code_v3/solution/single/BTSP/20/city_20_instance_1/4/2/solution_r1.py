import itertools
import math

# Define the city coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate distances between all pairs of cities
num_cities = len(cities)
distances = [[distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Find all permutations of city indices (excluding the depot, which is city 0)
city_indices = list(range(1, num_cities))

# Function to calculate the maximum distance in a tour
def max_distance_tour(tour):
    return max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Vehicle Routing Problem Solution trying all permutations
min_max_distance = float('inf')  # Fixing the name of the variable
best_tour = None

# Find the best tour using the permutations
for permutation in itertools.permutations(city_indices):
    # Creating a tour that starts and ends at the depot (city 0)
    tour = [0] + list(permutation) + [0]
    
    # Calculate the maximum edge weight in the current tour
    current_max_distance = max_distance_tour(tour)
    
    # Update the best tour found so far if the current is better
    if current_max_distance < min_max_distance:
        min_max_distance = current_max_latency
        best_tour = tour

# Total travel cost calculation
total_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))  # Rounding for clarity
print("Maximum distance between consecutive cities:", round(min_max_distance, 2))