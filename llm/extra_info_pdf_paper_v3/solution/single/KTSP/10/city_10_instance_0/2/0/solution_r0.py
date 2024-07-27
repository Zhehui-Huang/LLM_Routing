import itertools
import math

# City coordinates
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), 
          (62, 26), (79, 31), (61, 90), (42, 49)]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate combinations of 3 cities excluding the depot, to form groups of 4 with the depot
combinations = itertools.combinations(range(1, 10), 3)

# Initialize variables to track the best tour found
best_distance = float('inf')
best_tour = []

# Iterate over each combination
for combo in combinations:
    full_tour = [0] + list(combo)  # Start at the depot
    
    # Find all permutations of the full tour (excluding full returns to the depot for now)
    permutations = itertools.permutations(full_tour[1:])
    
    # Evaluate each permutation
    for perm in permutations:
        perm = [0] + list(perm) + [0]  # Complete the tour by returning to the depot
        # Calculate the total travel cost of this tour permutation
        cost = sum(distance(perm[i], perm[i+1]) for i in range(len(perm)-1))
        
        # If the found cost is less than the best known, update best known
        if cost < best_distance:
            best_distance = cost
            best_tour = perm

# Return the best tour and respective cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_distance}")