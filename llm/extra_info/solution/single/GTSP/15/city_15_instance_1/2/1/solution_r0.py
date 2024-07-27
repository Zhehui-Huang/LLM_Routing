import itertools
import math

# Coordinates of the cities
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Groups of cities
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible tours through exactly one city from each group, plus depot
def find_shortest_tour():
    min_tour = None
    min_distance = float('inf')
    
    for combination in itertools.product(*groups):
        # Calculate the path including the depot, the selected cities, and back to depot
        tour = [0] + list(combination) + [0]
        
        # Calculate total distance for this specific tour
        total_distance = 0
        for i in range(len(tour) - 1):
            total_distance += distance(tour[i], tour[i + 1])
        
        # Update minimum distance and tour if this one is shorter
        if total_distance < min_distance:
            min_distance = total_distance
            min_tour = tour
    
    return min_tour, min_distance

# Compute the shortest tour and its distance
shortest_tour, shortest_distance = find_shortest_tour()

# Output the results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {shortest_distance}")