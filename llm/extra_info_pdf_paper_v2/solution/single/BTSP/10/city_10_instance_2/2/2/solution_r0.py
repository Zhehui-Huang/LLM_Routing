import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Find all permutations of the city indices 1 to 9 (as the robot must start and end at city 0)
city_indices = list(range(1, 10))
perm = list(permutations(city_indices))

# Initialize variables to store the best tour
min_max_distance = float('inf')
best_tour = None
total_cost_of_best_tour = 0

# Check each permutation of cities
for p in perm:
    current_perm = [0] + list(p) + [0]  # Include the starting and ending city 0
    max_distance = 0  # Initialize max distance for this permutation
    total_distance = 0  # Total travel cost

    # Calculate total distance and max distance between consecutive cities
    for i in range(len(current_perm)-1):
        dist = distance(current_perm[i], current_perm[i+1])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist

    # Update best tour if the found permutation has a lower max distance   
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = current_perm
        total_cost_of_best_tour = total_distance
        
# Output the results
print(f'Tour: {best_tour}')
print(f'Total travel cost: {total_cost_of_best_tour}')
print(f'Maximum distance between consecutive cities: {min_max_distance}')