import itertools
import math

# Define the cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combinations of 6 additional cities (total 7 including depot)
city_indices = list(cities.keys())[1:]  # exclude the depot for combination generation
combinations = itertools.combinations(city_indices, 6)

# Function to calculate total distance of a tour
def calculate_tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i+1])
    return total_distance

# Variable to keep track of the minimum distance and corresponding tour
min_distance = float('inf')
best_tour = []

# Search over all combinations of cities
for comb in combinations:
    current_cities = [0] + list(comb)  # always start at the depot
    # Generate all permutations of current cities to find shortest path
    permutations = itertools.permutations(current_cities[1:])
    for perm in permutations:
        full_tour = [0] + list(perm) + [0]  # start and end at the depot
        current_distance = calculate_tour_distance(full_tour)
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = full_tour

# Output the best tour found and its total distance
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance}")