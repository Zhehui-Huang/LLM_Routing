import numpy as np
import itertools

# Define city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate the matrix of distances
n = len(cities)
distances = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Try to find all permutations and keep the best one based on max distance criteria
min_max_distance = float('inf')
best_tour = None

for perm in itertools.permutations(range(1, n)):
    # Adding the depot city to the tour
    tour = [0] + list(perm) + [0]
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour

# Calculate total travel cost of the best tour
if best_tour:
    total_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
else:
    print("No valid tour found")