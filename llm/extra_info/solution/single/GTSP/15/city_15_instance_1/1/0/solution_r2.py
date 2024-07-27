from itertools import permutations, product
from math import sqrt

# City coordinates
cities = {
    0: (29, 51),  # depot
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

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Distance matrix between all pairs of cities
distances = {}
for i in cities.keys():
    for j in cities.keys():
        if i != j:
            distances[(i, j)] = calculate_distance(i, j)

# Function to calculate tour cost
def calculate_tour_cost(tour):
    cost = 0
    n = len(tour)
    for i in range(n - 1):
        cost += distances[(tour[i], tour[i+1])]
    return cost

# Initialize minimum cost and best tour variables
min_cost = float('inf')
best_tour = []

for combination in product(*groups):
    # All permutations of cities from each group
    for perm in permutations(combination):
        # Create a tour starting and ending at the depot
        tour = [0] + list(perm) + [0]
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Display the optimal tour and its total travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)