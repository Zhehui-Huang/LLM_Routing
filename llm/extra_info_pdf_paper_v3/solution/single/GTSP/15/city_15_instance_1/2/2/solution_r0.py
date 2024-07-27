import itertools
import math

# City coordinates
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
    14: (98, 1)
}

# City groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Precompute all distances
distances = {}
for c1 in cities.keys():
    for c2 in cities.keys():
        distances[(c1, c2)] = euclidean(fact1, fact2)

# Generate all possible city selections (one from each group)
all_selections = list(itertools.product(*groups))

# Function to calculate the total path cost
def calculate_tour_cost(selection):
    total_cost = distances[(0, selection[0])]  # Start from the depot
    for i in range(len(selection) - 1):
        total_cost += distances[(selection[i], selection[i+1])]
    total_cost += distances[(selection[-1], 0)]  # Return to the depot
    return total_cost

# Evaluate all possible tours and find the one with minimum cost
min_cost = float('inf')
best_tour = None

for selection in all_selections:
    current_cost = calculate_tour_cost(selection)
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = [0] + list(selection) + [0]

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")