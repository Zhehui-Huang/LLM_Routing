import itertools
import math

# Coordinates for each city
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72),
}

# Number of cities to visit including the depot
k = 13

def calculate_distance(a, b):
    # Calculate Euclidean distance
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generate all subsets of cities of size k-1 that do not include the depot city 0
city_ids = list(cities.keys())[1:]  # Exclude the depot from the subset generation
subsets = itertools.combinations(city_ids, k-1)

# Initialize minimum variables
min_cost = float('inf')
best_tour = None

for subset in subsets:
    # Include the depot city in the subset
    full_subset = [0] + list(subset)
    
    # Generate permutations of the full subset excluding the initial depot to find tours
    for perm in itertools.permutations(full_subset[1:]):
        tour = [0] + list(perm) + [0]  # Construct the tour starting and ending at the depot
        
        # Calculate cost of the current tour
        cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        # Update the best tour found so far
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Outputting the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")