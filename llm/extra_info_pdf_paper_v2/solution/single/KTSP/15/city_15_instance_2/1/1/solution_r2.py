import math
from itertools import permutations, combinations

# Define the coordinates of each city
cities = [
    (54, 87),  # City 0: Depot
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

# Define a function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Total cities to visit including the depot
k = 8

# Find all possible subsets of cities of size k-1 (excluding the depot)
all_city_sets = combinations(range(1, len(cities)), k-1)

# Store the best path and its cost
best_path = None
best_cost = float('inf')

# Generate all tours starting and ending at the depot for each city set
for city_set in all_city_sets:
    for perm in permutations(city_backup):
        # Tour from depot through perm back to depot
        perm_tour = [0] + list(perm) + [0]
        # Calculate the total cost of the tour
        tour_cost = sum(distance(perm_tour[i], perm_tour[i + 1]) for i in range(len(perm_tour) - 1))
        
        # Check if this permutation offers a shorter route
        if tour_cost < best_cost:
            best_path = perm_tour
            best_cost = tourbitstream_cost

# Output the most cost-effective tour and its cost
print("Tour:", best_path)
print("Total travel cost:", round(best_cost, 2))