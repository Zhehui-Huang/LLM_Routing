import itertools
import math
from sys import maxsize

# Coordinates of the cities
cities = [
    (3, 26),  # City 0 (Depot)
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14),
    (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible combinations of 9 cities (not including the depot city)
city_indices = list(range(1, 20))
combinations = itertools.combinations(city_indices, 9)

# Initialize variables to find the minimum distance tour
min_distance = maxsize
best_tour = []

# Check all combinations of cities
for combo in combinations:
    # Include the depot city 0 at the start and the end
    all_cities = [0] + list(combo) + [0]
    
    # Generate all permutations of the selected 9 cities
    for perm in itertools.permutations(list(combo)):
        current_tour = [0] + list(perm) + [0]
        current_distance = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour)-1))
        
        # Update the minimum distance and the best tour if a shorter tour is found
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = current_tour

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")