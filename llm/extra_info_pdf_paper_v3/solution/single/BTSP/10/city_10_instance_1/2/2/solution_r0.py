import math
from itertools import permutations

# Define city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Trying to solve the problem using a brute-force approach
# Exploring all permutations of cities (excluding the depot city which is 0)

best_tour = None
min_max_distance = float('inf')
optimal_distance = None

# Iterate over all possible orders of visiting cities (excluding the depot city)
for perm in permutations(range(1, 10)):
    perm = (0,) + perm + (0,)  # Start and end at the depot city
    
    # Calculate the total travel cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0

    for i in range(len(perm) - 1):
        distance = calculate_distance(perm[i], perm[i + 1])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Check if this permutation gives a better (smaller) max distance between any two consecutive cities
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = perm
        optimal_distance = total_cost

# Output the best tour found, total travel cost and max distance between consecutive cities
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {optimal_distance:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")