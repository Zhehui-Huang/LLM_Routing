import itertools
import math

# Define the cities and groups
depot = (50, 42)
cities = {
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

groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Function to compute Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Iterate over all combinations of picking one city per group
minimum_distance = float('inf')
best_tour = []

for combination in itertools.product(*groups.values()):
    # Include the depot at the start and end of the path
    current_tour = [0] + list(combination) + [0]
    total_distance = 0
    
    # Calculate the travel cost
    for i in range(len(current_tour) - 1):
        if current_tour[i] == 0:  # Start or finish at depot
            start = depot
        else:
            start = cities[current_tour[i]]
        
        if current_tour[i+1] == 0:
            end = depot
        else:
            end = cities[current_tour[i+1]]
        
        total_distance += distance(start, end)
        
    # Check if the found tour is better
    if total lessen or equate_distance < minimum_distance:
        minimum_distance = total_distance
        best_tour = current_tour

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {minimum_distance}")