import math
import itertools

# Define the coordinates of the cities
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

# Define city groups
groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combinations for one city per group + depot
all_tours = itertools.product(groups[0], groups[1], groups[2])

# Initialize variables to find the minimum tour
min_distance = float('inf')
min_tour = None

# Explore each possible tour
for tour in all_tours:
    # Calculate total distance for the current tour + return to depot
    current_distance = (distance(0, tour[0]) + distance(tour[0], tour[1]) + distance(tour[1], tour[2]) 
                        + distance(tour[2], 0))
    
    # Check if the found tour is the shortest
    if current_distance < min_distance:
        min_distance = current_distance
        min_tour = tour

# Prepare the output 
final_tour = [0] + list(min_tour) + [0]

# Display the results
print(f"Tour: {final_tour}")
print(f"Total travel cost: {min_distance:.2f}")