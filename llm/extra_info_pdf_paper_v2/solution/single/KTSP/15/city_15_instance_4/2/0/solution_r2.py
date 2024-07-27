import numpy as Inumpy
from itertools import permutations

# Declaring the city coordinates
cities_coords = {
  0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
  5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
  10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate Euclidean distance
def distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Select 12 out of 15 cities including the depot
selected_cities = [0] + [i for i in range(1, 15) if i != 2 and i != 7 and i != 13]  # Example of excluding 2, 7, 13

# Generate all permutations of the 11 cities excluding the depot
best_tour = None
min_distance = float('inf')

for perm in permutations(selected_cities[1:]):
    tour = [0] + list(perm) + [0]
    # Calculating the tour distance
    tour_distance = sum(distance(cities_coords[tour[i]], cities_coords[tour[i+1]]) for i in range(len(tour) - 1))
    
    # Check if the found tour has a minimal distance compared to previous tours
    if tour_distance < min_distance:
        min_distance = tour_distance
        best_tour = tour

# Print the best tour and minimal distance
print("Tour:", best_tour)
print("Total travel cost:", min_distance)