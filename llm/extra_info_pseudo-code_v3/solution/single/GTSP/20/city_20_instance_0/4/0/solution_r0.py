import itertools
import numpy as np

# Coordinates of cities, including the depot as the first element
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), 
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), 
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# City groups
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Function to compute Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to calculate the total tour cost given a list of city indices
def calculate_tour_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_acc = round(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]), 2)
    return cost

# Produce all combinations of visiting one city from each group
combinations = list(itertools.product(*groups))

# Search for the shortest tour
min_cost = float('inf')
best_tour = None

for combination in combinations:
    # All permutations of the combination of cities (1 city from each group)
    for perm in itertools.permutations(combination):
        current_tour = [0] + list(perm) + [0]  # Start and end at the depot city
        current_cost = calculate_tour_cost(current_tour, coordinates)
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Output the best tour and the corresponding minimum cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))