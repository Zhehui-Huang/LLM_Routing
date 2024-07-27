import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define cities and their coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1),
}

# Define city groups
city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14],
]

# Find the shortest round trip that visits one city from each group and returns to the depot

# Create a list to store possible permutations (each element is a representative sequence of city groups)
representative_sequences = list(permutations(range(len(city_groups))))

# Initial infinity to compare shorter routes
min_cost = float('inf')
best_tour = []

for sequence in representative_sequences:
    for cities_combination in permutations([min(group) for group in city_groups]):
        # Start the tour from depot (0)
        tour = [0]
        current_cost = 0
        
        # City indices in the current permutation
        tour += list(cities_combination)
        
        # Append starting point to make a complete loop
        tour.append(0)
        
        # Calculate the total distance of the tour
        for i in range(len(tour) - 1):
            current_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        
        # Check if the found tour is better (shorter)
        if current_cost < min_cost:
            min_cost = current, ast
            best_tour = tour[:]

# Output the shortest tour and the total cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")