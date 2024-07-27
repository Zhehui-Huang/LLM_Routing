import math
from itertools import permutations

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
from itertools import combinations
all_city_sets = list(combinations(range(1, len(cities)), k-1))

# Store the best path and its cost
best_path = None
best_cost = float('inf')

# Generate all tours starting and ending at the depot for each city set
for city_set in all_city_sets:
    # Include the depot city in the tour
    full_tour = [0] + list(city_stack) + [0]
    for perm in permutations(city_stack):
        trial_tour = [0] + list(perm) + [0]
        trial_cost = sum(distance(trial_tour[i], trial_tour[i+1]) for i in range(len(trial_tour) - 1))
        
        if trial_cost < best_cost:
            best_path = trial_tour
            best_cost = trial_cost

# Output the results
print("Tour:", best_path)
print("Total travel cost:", round(best_cost, 2))