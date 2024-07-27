import itertools
import math

# City coordinates
coordinates = [
    (54, 87),  # Depot city
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

# City groups definition
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate all permutations of one city from each group
city_permutations = list(itertools.product(*groups))

# Function to calculate the route distance
def route_distance(route):
    total_distance = 0.0
    start = coordinates[0]  # Start at the depot
    # Move from the depot to the first city in the permutation
    total_distance += calculate_distance(start, coordinates[route[0]])
    
    # Move between successive cities in the permutation
    for i in range(len(route) - 1):
        total_distance += calculate_distance(coordinates[route[i]], coordinates[route[i+1]])
    
    # Return to the depot from the last city in the permutation
    total_depo_return_distance = calculate_distance(coordinates[route[-1]], start)
    total_distance += total_depo_return_distance

    return total_distance

# Find the minimum distance route
min_distance = float('inf')
best_route = None

for route in city_permutations:
    distance = route_distance(route)
    if distance < min_distance:
        min_distance = distance
        best_route = route

# Prepare the output format
complete_tour = [0] + list(best_route) + [0]

# Printing output
print("Tour: ", complete_tour)
print("Total travel cost: ", round(min_distance, 2))