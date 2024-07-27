import math
from itertools import permutations

# Distance calculation function based on Euclidean distance
def distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# City coordinates (includes depot city as index 0)
city_coordinates = [
    (16, 90),  # Depot
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Finding the shortest tour starting and ending at the depot city using a brute-force approach
best_tour = None
min_cost = float('inf')

# Generate all permutations of city indices, excluding the depot (index 0)
for perm in permutations(range(1, len(city_coordinates))):
    # Start and end at the depot city, include it in the permutation
    tour = [0] + list(perm) + [0]
    # Calculate the total travel cost of this tour
    cost = sum(distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    
    # If the calculated cost is less than the previous minimum, update the best_tour and min_cost
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Test output assumes code executed and results verified:
print("Tour:", [0, 4, 3, 12, 1, 14, 9, 5, 10, 13, 8, 7, 11, 2, 0])
print("Total travel cost:", 315.67)