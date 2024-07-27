import math
from itertools import permutations

# coordinates for the cities
cities = [
    (9, 93), # depot
    (8, 51), 
    (74, 99), 
    (78, 50), 
    (21, 23), 
    (88, 59), 
    (79, 77), 
    (63, 23), 
    (19, 76), 
    (21, 38), 
    (19, 65), 
    (11, 40), 
    (3, 21), 
    (60, 55), 
    (4, 39)
]

# Calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Find the maximal distance (bottleneck) in a tour
def max_edge_weight_in_tour(tour):
    max_weight = 0
    for i in range(1, len(tour)):
        curr_weight = distance(cities[tour[i-1]], cities[tour[i]])
        if curr_weight > max_weight:
            max_weight = curr_weight
    return max_weight

# Compute total distance of the tour
def total_distance_of_tour(tour):
    return sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Permutation of cities excluding the depot (city 0)
city_indices = list(range(1, len(cities)))
all_permutations = permutations(city_indices)

# Initiate best parameters
best_tour = None
lowest_max_distance = float('inf')
best_total_cost = float('inf')

# Process all permutations
for perm in all_permutations:
    current_tour = [0] + list(perm) + [0]  # start and end at the depot
    current_max_distance = max_edge_weight_in_tour(current_tour)
    
    if current_max_distance < lowest_max_distance:
        # Found a new better maximal distance
        lowest_max_distance = current_max_distance
        best_tour = current_tour
        best_total_cost = total_distance_of_tour(best_tour)

# Output the results
if best_tour:
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {best_total_cost}")
    print(f"Maximum distance between consecutive cities: {lowest_max_distance}")
else:
    print("No tour satisfies the conditions.")