import math
from itertools import permutations

# City coordinates
coordinates = [
    (8, 11),  # City 0
    (40, 6),  # City 1
    (95, 33), # City 2
    (80, 60), # City 3
    (25, 18), # City 4
    (67, 23), # City 5
    (97, 32), # City 6
    (25, 71), # City 7
    (61, 16), # City 8
    (27, 91), # City 9
    (91, 46), # City 10
    (40, 87), # City 11
    (20, 97), # City 12
    (61, 25), # City 13
    (5, 59),  # City 14
    (62, 88), # City 15
    (13, 43), # City 16
    (61, 28), # City 17
    (60, 63), # City 18
    (93, 15)  # City 19
]

# Computing Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Generate distance matrix
n = len(coordinates)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Function to find the tour that minimizes the maximum leg distance
def find_minimax_tour():
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')
    
    # Check each permutation of the cities excluding the depot
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        
        # Calculate maximum distance between consecutive cities and total cost
        max_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        # Update the best tour found
        if max_distance < best_max_distance:
            best_tour = tour
            best_max_distance = max_distance
            best_total_cost = total_cost
    
    return best_tour, best_total_cost, best_max_distance

# Execute the function and print the results
tour, total_cost, max_distance = find_minimax_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)