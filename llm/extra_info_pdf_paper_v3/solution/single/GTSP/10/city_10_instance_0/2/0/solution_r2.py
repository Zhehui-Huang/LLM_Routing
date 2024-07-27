import itertools
import math

# Define city coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98),
    4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
    8: (61, 90), 9: (42, 49)
}

# Define groups of cities
groups = [
    [1, 2, 6],  # Group 0
    [3, 7, 8],  # Group 1
    [4, 5, 9]   # Group 2
]

# Define function for Euclidean distance
def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Find all possible city tuples taking one from each group
all_possible_tours = itertools.product(*groups)

# Initialize variables to find the minimum distance tour
min_distance = float('inf')
best_tour = None

# Loop through each tour checking for the shortest tour
for possible_tour in all_possible_tours:
    # Always start each tour from the depot
    tour = [0] + list(possible_tour) + [0]
    
    # Calculate the total distance of the current tour
    distance = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    # Update the shortest tour found
    if distance < min_distance:
        min_distance = distance
        best_tour = tour

# Print the best tour found and its distance
print("Tour:", best_tour)
print("Total travel cost:", min_distance)