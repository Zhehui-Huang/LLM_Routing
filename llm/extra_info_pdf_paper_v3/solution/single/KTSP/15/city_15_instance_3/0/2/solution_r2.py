import math
import itertools

# Define city coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73),
    6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Compute Euclidean distance between two cities
def calc_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initialize variables for the best path and minimum distance
min_distance = float('inf')
best_path = None

# Create all combinations of 9 cities from the 14 (not including depot city)
city_combinations = itertools.combinations(range(1, 15), 9)

# Explore each combination
for combination in city_combinations:
    # Include the starting depot city and the cities in the combination
    full_combination = [0] + list(combination)
    
    # Permute the combination to find the shortest path order
    for permutation in itertools.permutations(full_combination):
        # Add the depot city to the end to complete the tour
        full_tour = list(permutation) + [0]
        
        # Calculate the distance of this full path
        total_distance = sum(calc_distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour) - 1))
        
        # Store if this is the shortest found so far
        if total_distance < min_distance:
            min_distance = total_distance
            best_path = full_tour

# Print the optimal path and corresponding total distance
print("Tour:", best_path)
print("Total travel cost:", min_distance)