import math
from itertools import permutations

# Define the cities' coordinates
coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Function to calculate total and maximum distance of a tour
def evaluate_tour(tour):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i+1])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

# Find all possible tours starting and ending at the depot (city 0)
all_tours = permutations(range(1,10))
best_tour = None
min_max_distance = float('inf')
best_total_distance = 0

# Evaluate each tour
for tour in all_tours:
    current_tour = [0] + list(tour) + [0]
    total_distance, max_distance = evaluate_tour(current_tour)
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_total_distance = total_distance
        best_tour = current_tour

# Output the best tour found
if best_tour:
    print("Tour:", best_tour)
    print("Total travel cost:", best_total_distance)
    print("Maximum distance between consecutive cities:", min_max_distance)
else:
    print("No valid tour found.")