import itertools
import math

# Coordinates of cities including the depot
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

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible 3-city combinations, including the depot city
combinations = itertools.combinations(range(1, 10), 3)  # Combining from cities 1 to 9 (city 0 is depot)
shortest_tour_length = float('inf')
shortest_tour = []

# Find the shortest tour from the depot across each combination
for combo in combinations:
    # Build routes including returning to the depot (0)
    current_cities = [0] + list(combo) + [0]
    permutations = itertools.permutations(current_cities[1:-1])  # Permutations of middle cities

    for perm in permutations:
        tour = [0] + list(perm) + [0]
        current_length = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if current_length < shortest_tour_length:
            shortest_tour_length = current_length
            shortest_tour = tour

# Output the shortest tour and its length
print("Tour:", shortest_tour)
print("Total travel cost:", shortest_tour_length)