import math

# City coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# City groups
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Find all candidate cities for the tour and their distances from depot
distance_matrix = {}
for city in cities:
    distance_matrix[city] = euclidean_distance(0, city)

# Generate permutations of one city from each group
import itertools
all_combinations = list(itertools.product(*groups))

# Evaluate each candidate tour by calculating total travel distance
best_tour = None
min_distance = float('inf')

# Compute all tours and find the shortest
for combination in all_combinations:
    tour = [0] + list(combination) + [0]
    tour_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    if tour_distance < min_distance:
        min_distance = tour_distance
        best_tour = tour

# Display the shortest tour and the total travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_distance)