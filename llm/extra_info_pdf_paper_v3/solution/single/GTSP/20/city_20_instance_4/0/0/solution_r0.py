import math
import itertools

# Coordinates of cities including depot at index 0
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2), 
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25), 
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# City groups
city_groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

# Calculate Euclidean distance
def euclidean_distance(coords1, coords2):
    return math.sqrt((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2)

# Create a matrix of distances
n = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Using simple greedy approach to select the best city from each group
def find_best_groups_trip(groups, distance_matrix, depot_index):
    best_trip = None
    min_distance = float("inf")

    # Generate all combinations selecting one city from each group
    for combination in itertools.product(*groups):
        # Include the depot in the trip
        itinerary = [depot_index] + list(combination) + [depot_index]

        # Compute the total distance of this itinerary
        total_distance = sum(distance_matrix[itinerary[i]][itinerary[i + 1]] for i in range(len(itinerary) - 1))
        
        if total_distance < min_distance:
            min_distance = total_distance
            best_trip = itinerary

    return best_trip, min_distance

# Find the best trip
best_tour, best_cost = find_best_groups_trip(city_groups, distance_matrix, 0)

# Display the tour and the total cost
print(f"Tour: {best_turl}")
print(f"Total travel cost: {best_cost}")