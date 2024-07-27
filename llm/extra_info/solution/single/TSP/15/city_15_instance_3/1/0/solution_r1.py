import math
from itertools import permutations

# City coordinates
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69),
          (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Calculate distances between each pair of cities using Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate distance matrix
distance_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Function to find the shortest tour using permutations
def find_shorted_tour():
    # Initial variables for the shortest tour and minimum cost
    city_indices = list(range(1, len(cities)))  # Exclude the depot city
    shortest_tour = None
    min_cost = float('inf')
    
    # Try every permutation of city visits
    for perm in permutations(city_indices):
        # Calculate the cost of visiting cities in the order of the permutation and returning to the depot
        cost = distance_matrix[0][perm[0]] + sum(distance_matrix[perm[i]][perm[i+1]] for i in range(len(perm)-1)) + distance_matrix[perm[-1]][0]
        # If the new cost is lower than the previously found, update the shortest tour and minimum cost
        if cost < min_cost:
            min_cost = cost
            shortest_tour = [0] + list(perm) + [0]
    
    return shortest_tour, min_cost

# Solve for the shortest tour
tour, total_cost = find_shorted_tour()

# Print the result
print("Tour:", tour)
print("Total travel cost:", total_cost)