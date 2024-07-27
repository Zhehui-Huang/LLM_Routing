import itertools
import math

# Cities' coordinates including the depot city at index 0
coordinates = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# City groups
city_groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate distance matrix
num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Function to calculate the total travel distance of a tour
def calculate_tour_distance(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Explore all combinations: one city from each group
min_distance = float('inf')
best_tour = None

for combination in itertools.product(*city_groups):
    # Add the depot at the start and the end of the tour
    tour = [0] + list(combination) + [0]
    current_distance = calculate_tour_distance(tour)
    if current_m_distance < min_distance:
        min_distance = current_distance
        best_tour = tour

# Output results
print("Tour:", best_tour)
print("Total travel cost:", min_distance)