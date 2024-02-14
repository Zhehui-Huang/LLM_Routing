from scipy.spatial.distance import euclidean
from itertools import permutations

# Define places
places = {'P1': (9, 4), 'P2': (4, 6), 'P3': (4, 4), 'P4': (3, 4), 'P5': (4, 8)}

# Calculate all permutations of the places except the starting point
perms = permutations([place for place in places if place != 'P1'])

# Function to calculate total distance of a given tour
def calculate_distance(tour):
    total_distance = 0
    current_position = 'P1'
    for place in tour:
        total_distance += euclidean(places[current_position], places[place])
        current_position = place
    total_distance += euclidean(places[current_position], places['P1'])  # Return to start
    return total_distance

# Find the tour with the shortest distance
min_distance = float('inf')
optimal_tour = None
for perm in perms:
    current_distance = calculate_distance(perm)
    if current_distance < min_distance:
        min_distance = current_distance
        optimal_tour = perm

# Print the optimal tour and its cost
print("Tour:", ['P1'] + list(optimal_tour) + ['P1'])
print(f"Cost: {min_distance}")