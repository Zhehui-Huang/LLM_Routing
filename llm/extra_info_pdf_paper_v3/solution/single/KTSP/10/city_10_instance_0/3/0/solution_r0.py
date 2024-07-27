import itertools
import math

# Coordinates of the cities
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
def euclidean_distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[city_b][1])**2)

# Generate all combinations of 3 cities (other than the depot 0)
city_combinations = itertools.combinations(range(1, 10), 3)

# Determine the shortest tour that includes the depot city and 3 of the other cities
best_tour = None
min_cost = float('inf')

# Check all combinations and permutations of them
for combination in city_combinations:
    # Include the depot city in the permutation
    for permutation in itertools.permutations(combination):
        current_tour = [0] + list(permutation) + [0] # start and end at the depot city
        current_cost = 0
        
        # Calculate the total cost for this tour
        for i in range(len(current_tour) - 1):
            current_cost += euclidean_distance(current_tour[i], current_tour[i+1])
        
        # Update the best tour if current one is better
        if current_cost < min_cost:
            best_tour = current_tour
            min_cost = current_cost

# Output the best tour and its total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")