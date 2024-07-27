import math
from itertools import permutations

# Define city coordinates and groups
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79),
}
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create all permutations of one city from each group
group_permutations = list(permutations([group[0] for group in groups]))

# Function to calculate total tour distance 
def calculate_tour_cost(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distance(tour[i], tour[i+1])
    return total_dist

# Find the shortest path among permutations
min_tour_cost = float('inf')
min_tour = None

for perm in group_permutations:
    # Construct the tour starting and ending at the depot city 0
    full_tour = [0] + list(perm) + [0]
    tour_cost = calculate_tour_cost(full_tour)
    if tour_cost < min_tour_cost:
        min_tour_cost = tour_cost
        min_tour = full_tour

# Output the shortest tour and its cost
print("Tour:", min_tour)
print("Total travel cost:", min_tour_cost)