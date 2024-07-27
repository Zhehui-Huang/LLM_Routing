import math
from itertools import permutations, combinations

# Define the cities and their coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to compute the shortest tour visiting 4 cities including depot
def find_shortest_tour():
    min_distance = float('inf')
    optimal_tour = None

    # Evaluate each combination of 3 additional cities to visit alongside the depot (city 0)
    for combo in combinations(range(1, 15), 3):
        current_cities = [0] + list(combo)  # Always include the depot city 0
        # Check all permutations of the current city list to find the shortest route
        for perm in permutations(current_cities):
            # Ensure first and last cities are the depot
            tour = list(perm) + [0]
            # Calculate the total distance of this tour
            total_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            # Check if this is the shortest found so far
            if total_distance < min_distance:
                min_distance = total_distance
                optimal_tour = tour
    
    return optimal_tour, min_distance

# Find the shortest tour
optimal_tour, min_distance = find_shortest_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {min_distance:.2f}")