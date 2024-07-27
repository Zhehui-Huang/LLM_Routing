import itertools
import math

# Given city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a matrix of distances
distances = {}
for i in cities:
    distances[i] = {}
    for j in cities:
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# The robot needs to visit exactly 5 cities including the depot city 0
k = 5

# Find the minimum tour using permutations of the cities
min_cost = float('inf')
best_tour = []

# Consider all combinations of 4 additional cities with the depot city
for combo in itertools.combinations(range(1, 10), k-1):
    # Include the depot city
    cities_to_visit = [0] + list(combo)
    
    # Consider every permutation of the selected cities
    for perm in itertools.permutations(cities_to_visit):
        if perm[0] == 0:  # ensure it starts at the depot
            # Include a return to the depot city
            full_tour = list(perm) + [0]
            # Calculate the total travel cost
            cost = sum(distances[full_tour[i]][full_tour[i + 1]] for i in range(len(full_tour) - 1))
            
            # Update the best tour found
            if cost < min_cost:
                min_cost = cost
                best_tour = full_tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", min_cost)