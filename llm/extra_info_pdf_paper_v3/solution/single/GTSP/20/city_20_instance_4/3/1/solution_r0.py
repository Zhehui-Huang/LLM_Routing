import numpy as np
import itertools

# Define the city coordinates and their respective groups
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], 
    [2, 4, 14], [10, 17], [7, 15]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate all pairwise distances
dist_matrix = {}
for c1 in cities.keys():
    for c2 in cities.keys():
        if c1 >= c2:  # only calculate one way since it's symmetric
            dist_matrix[(c1, c2)] = dist_matrix[(c2, c1)] = euclidean_distance(cities[c1], cities[c2])

# Representative selection using closest city to the depot
representatives = [0]  # include starting city
for group in groups:
    closest_city = min(group, key=lambda x: dist_matrix[(0, x)])
    representatives.append(closest_city)

# Simple yet effective heuristic: find a tour that visits the representatives in a closed loop
def find_shortest_tour(representatives):
    min_tour = None
    min_distance = float('inf')
    for perm in itertools.permutations(representatives[1:]):  # iterate over permutations excluding the depot
        tour = [0] + list(perm) + [0]
        distance = sum(dist_matrix[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
        if distance < min_distance:
            min_distance = distance
            min_tour = tour
    return min_tour, min_distance

# Find the best tour
best_tour, best_cost = find_shortest_tour(representatives)

# Print the results according to the format
print("Tour:", best_tour)
print("Total travel cost:", best_cost)