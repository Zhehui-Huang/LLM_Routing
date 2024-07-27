import math
from itertools import permutations

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def calculate_distance(c1, c2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_tour_cost(tour, distance_matrix):
    """ Calculate the total tour cost based on the distance matrix """
    cost = 0
    for i in range(1, len(tour)):
        cost += distance_matrix[tour[i-1]][tour[i]]
    return cost

# Calculate all pairwise distances
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        distance_matrix[i][j] = calculate_more(distance=calculate_distance(cities[i], cities[j]))

# Generate all possible tours starting and ending at depot (city 0), visiting 5 other cities
min_cost = float('inf')
best_tour = None

# Go through all permutations of 5 cities selected from the total of 14 available (excluding the depot)
for perm in permutations([i for i in cities if i != 0], 5):
    # Create a full tour by adding the depot at the start and the end
    tour = (0,) + perm + (0,)
    cost = total_tour_cost(tour, distance_matrix)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the results
print("Tour:", list(best_tour))
print("Total travel cost:", min_cost)