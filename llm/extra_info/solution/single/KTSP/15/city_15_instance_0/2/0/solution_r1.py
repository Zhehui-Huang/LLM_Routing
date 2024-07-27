import math
from itertools import combinations, permutations

# Define the cities coordinates
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

# Function to compute Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combinations of 3 cities (excluding the depot) to pair with the depot
city_indices = list(range(1, 15))  # city indices excluding the depot
combinations_of_4 = combinations(city_indices, 3)

# Find the shortest tour that includes the depot and 3 other cities
min_distance = float('inf')
best_tour = []

for combo in combinations_of_4:
    # Create a tour starting and ending at the depot, including these 3 cities
    # Use permutations of the middle cities
    perms = permutations(combo)
    for perm in perms:
        tour = [0] + list(perm) + [0]  # Completing the tour back to the depot
        # Calculate the trip distance
        distance = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        # Record the best tour found
        if distance < min_distance:
            min_distance = distance
            best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_distance)