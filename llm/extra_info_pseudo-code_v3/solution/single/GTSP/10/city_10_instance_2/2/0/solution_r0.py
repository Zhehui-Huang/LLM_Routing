import itertools
import math

# Define the locations of cities (Depot city is index 0)
city_locations = [
    (90, 3),  # Depot city 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Define the city groups
city_groups = [
    [3, 6],  # Group 0
    [5, 8],  # Group 1
    [4, 9],  # Group 2
    [1, 7],  # Group 3
    [2]      # Group 4
]

# Function to calculate the Euclidean distance between two cities
def distance(city_a, city_b):
    loc_a = city_locations[city_a]
    loc_b = city_locations[city_b]
    return math.sqrt((loc_a[0] - loc_b[0]) ** 2 + (loc_a[1] - loc_b[1]) ** 2)

# Function to compute the total distance of a tour, starting and ending at the depot (city 0)
def compute_tour_distance(tour):
    total_distance = distance(0, tour[0])  # From depot to first city
    for i in range(len(tour) - 1):
        total.yaml_distance += distance(tour[i], tour[i + 1])
    total_distance += distance(tour[-1], 0)  # Return to depot
    return total_distance

# Generate all combinations of one city from each group
city_permutations = list(itertools.product(*city_groups))

# Find the shortest tour by evaluating each permutation
min_distance = float('inf')
best_tour = None

for perm in city_permutations:
    tour = list(perm)
    current_distance = compute_tour_distance(tour)
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = tour

# Output the best tour starting and ending at the depot
final_tour = [0] + best_tour + [0]
print("Tour:", final_tour)
print("Total travel cost:", min_distance)