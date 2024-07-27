import math
from scipy.spatial import distance
from itertools import permutations

# City coordinates
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69),
          (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Calculate distances between each pair of cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate distance matrix
distance_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Find the shortest tour using permutations
def find_shortest_tour():
    city_indices = list(range(1, len(cities)))  # cities without the depot
    shortest_tour = None
    min_cost = float('inf')
    
    for perm in permutations(city_indices):
        # Calculate the total cost including return to the depot
        cost = distance_matrix[0][perm[0]] + sum(distance_matrix[perm[i]][perm[i+1]] for i in range(len(perm)-1)) + distance_matrix[perm[-1]][0]
        if cost < min_cost:
            min_cost = cost
            shortest_tour = [0] + list(perm) + [0]
    
    return shortest_tour, min_cost

# Get the shortest tour and the total travel cost
tour, total_cost = find_shortest_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)