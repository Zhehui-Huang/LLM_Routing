import itertools
import math

# Define cities as a list of tuples (x, y)
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Try all combinations of 12 other cities from the remaining 19 (excluding the depot)
def find_best_tour():
    min_distance = float('inf')
    best_tour = []
    
    for combo in itertools.combinations(range(1, 20), 12):
        # Include the depot city and create a round-trip
        current_combo = [0] + list(combo) + [0]
        
        # Calculate all possible permutations of the selected cities excluding the first and last one (depot)
        for perm in itertools.permutations(current_combo[1:-1]):
            tour = [0] + list(perm) + [0]
            total_distance = sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
            
            if total_distance < min_distance:
                min_distance = total_distance
                best_tour = tour
    
    return best_tour, min_distance

# Obtain the best tour and the minimum distance
best_tour, min_distance = find_best_tour()

# Print the results
print("Tour:", best_tour)
print("Total travel cost:", round(min_distance, 2))