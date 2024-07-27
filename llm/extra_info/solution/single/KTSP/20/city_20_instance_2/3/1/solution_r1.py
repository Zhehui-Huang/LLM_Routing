from itertools import permutations
import math

# Coordinates of cities
coordinates = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92),
    9: (59, 8), 10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49),
    17: (91, 94), 18: (51, 58), 19: (30, 48)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Pre-calculate all pairs distances
distances = {}
for i in coordinates:
    for j in coordinates:
        if i != j:
            distances[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])

def total_distance(path):
    total = 0
    for i in range(len(path) - 1):
        total += distances[(path[i], path[i + 1])]
    return total

# Generate all possible routes visiting exactly 9 other cities + depot city returns
min_distance = float('inf')
optimal_tour = []

# We choose 9 cities from 1 to 19 (since 0 is the depot)
other_cities = list(range(1, 20))
combinations = permutations(other_cities, 9)
for comb in combinations:
    # Create a path that starts and ends at the depot city 0
    path = [0, *comb, 0]  
    current_distance = total_distance(path) # corrected typo here
    if current_distance < min_distance:
        min_distance = current_distance
        optimal_tour = path

# Output the optimal tour and its total travel cost as required
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {min_distance:.2f}")