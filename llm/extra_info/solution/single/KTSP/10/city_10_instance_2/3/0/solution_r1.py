import itertools
import math

# Define the city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Find all combinations of 5 non-depot cities to visit since 1 city (depot) is already included
city_combinations = itertools.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)

# Initialize variables to store the best tour and its total distance
best_tour = None
best_distance = float('inf')

# Iterate over each combination
for cities_to_visit in city_combination:
    # Generate all permutations of cities in the combination
    for tour in itertools.permutations(cities_to_visit):
        # Include depot at the start and end of the tour
        current_tour = (0,) + tour + (0,)
        
        # Calculate the total distance of the tour
        total_distance = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
        
        # Update the best tour if the current one is shorter
        if total_distance < best_distance:
            best_distance = total_distance
            best_tour = current_tour

# Print the outcome
print("Tour:", list(best_tour))
print("Total travel cost:", best_distance)