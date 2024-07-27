import itertools
import math

# Define the cities' positions
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 
    3: (78, 50), 4: (21, 23), 5: (88, 59), 
    6: (79, 77), 7: (63, 23), 8: (19, 76), 
    9: (21, 38), 10: (19, 65), 11: (11, 40), 
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible subsets of cities including the depot city that contains exactly 4 cities
all_subsets = [c for c in itertools.combinations(range(1, 15), 3) if 0 not in c]
subsets_with_depot = [(0,) + subset for subset in all_subsets]

# Evaluate each subset by trying all permutations of visiting the non-depot cities
shortest_tour = None
shortest_distance = float('inf')

for subset in subsets_with_depot:
    # Generate all permutations of the subset of cities
    for perm in itertools.permutations(subset):
        # Calculate total distance of the tour that goes back to the depot in the end
        tour_distance = sum(distance(perm[i], perm[i+1]) for i in range(len(perm)-1)) + distance(perm[-1], perm[0])
        
        # Update the shortest tour found
        if tour_distance < shortest_distance:
            shortest_tour = perm
            shortest_distance = tour_distance

# Result output
result_tour = list(shortest_tour) + [0]  # Closing the loop back to the depot
print("Tour:", result_tour)
print("Total travel cost:", shortest_distance)