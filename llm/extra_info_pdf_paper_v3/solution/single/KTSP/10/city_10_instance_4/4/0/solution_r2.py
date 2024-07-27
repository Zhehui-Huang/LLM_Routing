import itertools
import numpy as np

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance
def distance(c1, c2):
    return np.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Create a distance matrix
distance_matrix = [[distance(i, j) for j in cities.keys()] for i in cities.keys()]

# Function to calculate total distance of a tour
def tour_distance(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Including the depot, find the shortest path visiting exactly 8 cities
best_tour = None
best_distance = float('inf')
for city_subset in itertools.combinations(range(1, 10), 7): # Choose 7 cities plus the depot
    full_tour = [0] + list(city_subset) + [0]
    # Permute the middle cities to find shortest route
    for perm in itertools.permutations(full_tour[1:-1]):
        current_tour = [0] + list(perm) + [0]
        current_distance = tour_distance(current_tour)
        if current_distance < best_distance:
            best_distance = current_distance
            best_tour = current_tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", best_distance)