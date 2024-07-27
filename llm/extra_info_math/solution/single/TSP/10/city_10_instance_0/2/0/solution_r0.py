import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define the coordinates of the cities
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Number of cities including the depot
n = len(cities)

# Calculate the Euclidean distance matrix
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean(cities[i], cities[j])

# Function to calculate the cost of a tour
def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for k in range(len(tour) - 1):
        total_cost += distance_matrix[tour[k]][tour[k + 1]]
    return total_cost

# Generate all possible tours (permutations of the city indices, excluding the depot)
all_possible_tours = permutations(range(1, n))

# Find the shortest tour
min_cost = float('inf')
best_tour = None

for perm in all_possible_tours:
    current_tour = [0] + list(perm) + [0]
    current_cost = calculate_tour_cost(current_tour, distance_matrix)
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = current_tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", min_cost)