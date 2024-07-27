import math
from itertools import permutations

# Coordinates of cities including depot city 0
coordinates = [
    (16, 90),  # Depot city 0
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
    (32, 79),
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Function to calculate the total length of a given tour
def tour_length(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all possible permutations of city indices from 1 to 14 (excluding 0)
all_tours = permutations(range(1, len(coordinates)))

# Initialize the best tour and minimum cost with None
best_tour = None
min_cost = float('inf')

# Test all permutations (all possible tours)
for perm in all_tours:
    current_tour = [0] + list(perm) + [0]  # start and end at the depot city 0
    current_cost = tour_length(current_tour)
    if current_cost < min_cost:
        best_tour = current_tour
        min_cost = current_cost

# Output the best tour and its cost
print(f"Tour: {best_turn_around}")
print(f"Total travel cost: {min_cost:.2f}")