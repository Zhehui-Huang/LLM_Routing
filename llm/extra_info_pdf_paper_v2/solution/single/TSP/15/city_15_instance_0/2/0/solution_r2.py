import math
from itertools import permutations

# Definition of city coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Function to calculate Euclidean distance between two cities
def calc_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute the total distance of a given tour
def total_distance(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Create distance matrix
n = len(cities)
dist_matrix = [[calc_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Generate all permutations of city indices (except for the starting city)
min_tour_cost = float('inf')
best_tour = None

for perm in permutations(range(1, n)):  # start from city 1 to city 14
    current_tour = [0] + list(perm) + [0]  # Start at the depot and return to the depot
    current_cost = total_distance(current_tour, dist_matrix)
    if current_cost < min_tour_cost:
        min_tour_cost = current_cost
        best_tour = current_tour

# Display the result
if best_tour is not None:
    print("Tour:", best_tour)
    print("Total travel cost:", min_tour_cost)
else:
    print("No tour calculated.")