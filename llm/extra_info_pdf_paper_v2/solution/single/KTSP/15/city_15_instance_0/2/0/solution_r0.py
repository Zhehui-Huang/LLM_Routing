import itertools
import math

# Define city coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate all pairwise distances
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = euclidean_distance(i, j)

# Generate all combinations of 3 cities excluding the depot city
combos = itertools.combinations([i for i in cities if i != 0], 3)

# Find the shortest tour
min_distance = float('inf')
best_tour = None

for combo in combos:
    # Generate permutations of each combination
    for perm in itertools.permutations(combo):
        # Create a tour from the depot to each city and back to the depot
        tour = [0] + list(perm) + [0]
        # Calculate the tour distance
        tour_distance = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
        
        # Update the shortest distance and the best tour
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = tour

# Result output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")