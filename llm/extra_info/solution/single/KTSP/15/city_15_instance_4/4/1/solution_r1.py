import itertools
from math import sqrt

# Define the cities with their coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    return sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Improve the iteration to consider only meaningful and complete tours
best_distance = float('inf')
best_path = []

# Consider combinations that always include the depot (city index 0)
for cities_subset in itertools.combinations(range(1, 15), 11):
    # Always include city 0 (depot)
    current_cities_indices = [0] + list(cities_subset)
    
    # Permute different city orders including the depot as the start and end point
    for permutation in itertools.permutations(current_cities_indices):
        path = list(permutation) + [0] # Close the loop to depot
        
        # Calculate total travel cost for this permutation
        dist = 0
        for i in range(len(path) - 1):
            dist += euclidean_distance(cities[path[i]], cities[path[i+1]])
        
        # Update minimal distance and the associated path
        if dist < best_distance:
            best_distance = dist
            best_path = path

# Print the shortest path found and the associated total distance
print("Tour:", best_path)
print("Total travel  cost:", round(best_distance, 2))