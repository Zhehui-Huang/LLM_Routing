import math
import itertools

# City coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all combinations of 3 cities excluding the depot
combinations = itertools.combinations(range(1, 10), 3)

min_distance = float('inf')
best_tour = []

# Check all combinations
for combination in combinations:
    # Create tours that start and end at the depot and include the combination
    current_tour = [0] + list(combination) + [0]
    current_distance = 0
    
    # Calculate the distance for this tour
    for i in range(len(current_tour) - 1):
        current_distance += distance(current_tour[i], current_tour[i+1])
    
    # If this distance is better, update the best solution found
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = current_tour

# Print the best tour and its total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance}")