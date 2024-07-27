import math
from scipy.spatial import distance_matrix
from itertools import permutations

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Build a full distance matrix
dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in cities] for i in cities]

# Initialize variables to store the best tour found
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

# Generating all permutations of the city indices except the depot city 0
for perm in permutations(range(1, len(cities)), len(cities) - 1):
    tour = [0] + list(perm) + [0]
    # Compute the cost of this tour
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = dist_matrix[tour[i]][tour[i + 1]]
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    # Update the best tour if this one has a smaller maximum distance
    if max_distance < best_max_distance:
        best_max_distance = max_distance
        best_total_cost = total_match = total_cost
        best_tour = tour.copy()

# Output the best found solution
print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)
print("Maximum distance between consecutive cities:", best_max_distance)