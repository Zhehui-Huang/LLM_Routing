import math
import itertools

# Initialize city coordinates
cities = [
    (8, 11),  # depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46),
    (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), 
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Groupings
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Compute the Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Generate all combinations with one city from each group
all_combinations = itertools.product(*groups)

# Find the shortest path
def find_shortest_path():
    minimum_distance = float('inf')
    best_tour = None
    
    for combination in all_combinations:
        # Create the cycle including the depot: 0 -> city_from_group_0 -> city_from_group_1 -> city_from_group_2 -> 0
        tour = [0] + list(combination) + [0]
        # Calculate the tour distance
        tour_distance = 0
        for i in range(len(tour) - 1):
            tour_distance += distance(tour[i], tour[i + 1])
        
        # Check if this tour is better
        if tour_distance < minimum_distance:
            minimum_distance = tour_distance
            best_tour = tour
    
    return best_tour, minimum_distance

# Solve the problem
tour, total_distance = find_shortest_path()

# Output the solution
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")