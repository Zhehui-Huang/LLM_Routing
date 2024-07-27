import itertools
import math

# Coordinates of the cities including the depot
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
          (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
          (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

# City groups
groups = [[7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], [1, 9, 14, 19], [5, 6, 17]]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combinations of cities, picking one from each group
possible_tours = itertools.product(*groups)

# Initialize minimum distance high enough
min_distance = float('inf')
best_tour = None

# Evaluate each possible combination of cities
for tour in possible_tours:
    # Start from the depot, go through the selected cities, and return to the depot
    route = [0] + list(tour) + [0]
    total_distance = sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))
    
    # Update the minimum distance and best tour if the current one is better
    if total_distance < min_distance:
        min_distance = total_distance
        best_tour = route

# Output the best tour and the total travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_distance)