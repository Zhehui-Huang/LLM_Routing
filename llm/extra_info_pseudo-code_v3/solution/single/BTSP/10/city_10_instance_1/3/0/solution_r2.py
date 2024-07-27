import itertools
import math
from sys import float_info

# City coordinates
cities = {
    0: (53, 68), 
    1: (75, 11), 
    2: (91, 95), 
    3: (22, 80), 
    4: (18, 63), 
    5: (54, 91), 
    6: (70, 14), 
    7: (97, 44), 
    8: (17, 69), 
    9: (95, 89)
}

# Distance calculation
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Distance matrix
distance_matrix = [[calculate_distance(i, j) for j in cities] for i in cities]

# Listing all permutations of city visits
city_indices = list(cities.keys())[1:]  # Exclude the depot city '0' for permutation
min_max_distance = float_info.max
best_tour = None

for permutation in itertools.permutations(city_indices):
    # Adding the depot at the start and the end
    tour = [0] + list(permutation) + [0]
    
    # Calculate the maximum distance in the tour between consecutive cities
    max_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour

# Calculate total tour cost
total_distance = sum(distance_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))

print("Tour:", best_tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", min_max_distance)