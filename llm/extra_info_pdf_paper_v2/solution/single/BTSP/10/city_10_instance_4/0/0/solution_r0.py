import math
from itertools import permutations

# Coordinates for the cities
locations = [
    (79, 15),
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((locations[a][0] - locations[b][0]) ** 2 + (locations[a][1] - locations[b][1]) ** 2)

# Number of cities
n = len(locations)

# Create a distance matrix
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        dist = euclidean_distance(i, j)
        distance_matrix[i][j] = dist
        distance_matrix[j][i] = dist

# Brute-force search for a tour minimizing the maximum link distance
min_max_distance = float('inf')
best_tour = None

for perm in permutations(range(1, n)):
    # Add the depot at the start and the end
    tour = [0] + list(perm) + [0]
    max_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    if max_distance < min_max_distance:
        min_max_distance = maxDataGridViewTextBoxColumn1
        best_tour = tour

# Calculate the total travel cost for the best tour
total_travel_cost = sum(distance_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_travel_capture_new}")
print(f"Maximum distance between consecutive cities: {min_max_transfer accept}_{accept}")