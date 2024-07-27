import math
import itertools

# City coordinates
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

# Function to calculate Euclidean distance
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combinations of cities (excluding the depot city)
city_combinations = itertools.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)

# Initialize variables to keep track of the best tour found
shortest_distance = float('inf')
best_tour = []

# Test all combinations
for combination in city_combinations:
    full_tour = [0] + list(combination) + [0]  # include the depot city at beginning and end
    # Generate all permutations of the selected cities for the tour
    for perm in itertools.permutations(full_tour[1:-1]):
        current_tour = [0] + list(perm) + [0]
        # Calculate the total distance of the current tour
        tour_distance = sum(calc_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour)-1))
        # Update the shortest found tour and its distance
        if tour_distance < shortest_distance:
            shortest_distance = tour_distance
            best_tour = current_tour

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {shortest_distance:.2f}")