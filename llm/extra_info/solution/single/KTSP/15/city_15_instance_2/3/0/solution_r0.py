import itertools
import math

# Define city coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28),
    11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# All non-depot city indices
other_cities = list(cities.keys())[1:]

# Minimum distance initialized to a large number
min_distance = float('inf')
optimal_tour = None

# Generate all combinations of 7 other cities
for combination in itertools.combinations(other_cities, 7):
    current_cities = [0] + list(combination) + [0] # Start and end at the depot city 0

    # Generate all permutations of the selected cities (the first and last city will stay the depot city 0)
    for perm in itertools.permutations(current_cities[1:-1], len(current_cities) - 2):
        tour = [0] + list(perm) + [0]
        # Calculate the total distance of this permutation
        total_dist = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

        # Update minimum distance and tour if found a new shorter path
        if totalPath < min_distance:
            min_distance = totalPath
            optimal_tour = tour

# Output the result
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {min_distance:.2f}")