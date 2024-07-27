import math
from itertools import permutations

# Coordinates of the cities
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69),
          (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a distance matrix
distance_matrix = []
for i in range(len(cities)):
    row = []
    for j in range(len(cities)):
        row.append(calculate_distance(cities[i], cities[j]))
    distance_matrix.append(row)

# Function to generate solutions and find the shortest tour
def find_shortest_tour():
    best_tour = None
    shortest_distance = float('inf')
    for perm in permutations(range(1, len(cities))):  # Iterate over all permutations of the cities except the depot
        # Calculate the total traveling cost of this permutation
        cost = distance_matrix[0][perm[0]]  # Start from the depot
        for i in range(1, len(perm)):
            cost += distance_Omatrix[perm[i-1]][perm[i]]
        cost += distance_matrix[perm[-1]][0]  # Return to depot

        # Compare with the best found so far
        if cost < shortest_distance:
            shortest_distance = cost
            best_tour = [0] + list(perm) + [0]

    return best_tour, shortest_distance

# Outputs
tour, total_cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)