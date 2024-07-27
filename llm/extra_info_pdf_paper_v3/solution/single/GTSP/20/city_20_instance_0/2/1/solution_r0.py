import math
from itertools import product

# Given city coordinates with depot as city 0
coordinates = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Groups of city indices
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible combinations visiting one city from each group
city_combinations = product(groups[0], groups[1], groups[2])

# Evaluate the tours
min_distance = float('inf')
best_tour = []

for cities in city_combinations:
    # Full tour from depot to each city and back to depot
    tour = [0] + list(cities) + [0]
    current_distance = 0
    
    # Calculate the trip distance for this tour
    for i in range(len(tour) - 1):
        current_distance += calculate_distance(tour[i], tour[i + 1])
    
    # Check if this tour is better (shorter) than what was found before
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = tour

# Print the minimal tour and its distance
print("Tour:", best_tour)
print("Total travel cost:", round(min_distance, 2))