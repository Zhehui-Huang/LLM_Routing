import math
from itertools import permutations

# Coordinates for each city, including the depot city
coordinates = [
    (29, 51), # depot city 0
    (49, 20), # city 1
    (79, 69), # city 2
    (17, 20), # city 3
    (18, 61), # city 4
    (40, 57), # city 5
    (57, 30), # city 6
    (36, 12), # city 7
    (93, 43), # city 8
    (17, 36), # city 9
    (4, 60),  # city 10
    (78, 82), # city 11
    (83, 96), # city 12
    (60, 50), # city 13
    (98, 1)   # city 14
]

def euclidean_distance(p1, p2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Compute distances between all pairs of cities
n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Generate all possible tours starting and ending at depot city 0
all_tours = permutations(range(1, n))
min_bottleneck = float('inf')
best_tour = None

for tour in all_tours:
    tour = (0,) + tour + (0,)
    max_edge_cost = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    if max_edge_cost < min_bottleneck:
        min_bottleneck = max_edge_cost
        best_tour = tour

# Calculate total distance of the best tour
total_distance = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))

print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {min_bottleneck:.2f}")