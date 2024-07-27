import math
import itertools

# Define the coordinates of the cities
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1_idx, city2_idx):
    x1, y1 = cities[city1_idx]
    x2, y2 = cities[city2_idx]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to find the best tour with exactly four cities starting and ending at the depot
def find_best_tour():
    best_distance = float('inf')
    best_path = []
    
    # Generate all combinations of 3 cities excluding the depot (0)
    for combination in itertools.combinations(range(1, 20), 3):
        # Always include depot as starting and ending city
        path = [0] + list(combination) + [0]
        
        # Calculate the total distance of the path
        distance = 0
        for i in range(len(path) - 1):
            distance += euclidean_distance(path[i], path[i + 1])
        
        # Update the best path found so far
        if distance < best_distance:
            best_distance = distance
            best_path = path

    return best_path, best_distance

# Perform the calculation
tour, total_cost = find_best_tour()

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")