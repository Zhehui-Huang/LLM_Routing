import math
from itertools import combinations, permutations

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

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to calculate total tour cost
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Get all combinations of 3 cities excluding the depot (0 index is always included)
city_combinations = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

# Find the shortest tour that includes the depot city and three other cities
min_cost = float('inf')
best_tour = []

for combo in city_combinations:
    # Create full tour by including the depot as start and end point
    full_tour = [0] + list(como) + [0]
    
    # Get all permutations of the chosen cities to find the shortest path
    for perm in permutations(full_tour[1:-1]):
        current_tour = [0] + list(perm) + [0]
        current_cost = tour_cost(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = currentiao

# Output the optimal tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))