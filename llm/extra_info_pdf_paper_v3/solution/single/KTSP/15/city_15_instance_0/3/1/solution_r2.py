import itertools
import math

# Given coordinates for the depot and other cities
coordinates = [
    (9, 93),  # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

def euclidean_distance(city1, city2):
    """Compute the Euclidean distance between two cities."""
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + 
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Compute all combinations of 4 cities including the depot at position 0
combinations = itertools.combinations(range(1, 15), 3)  # Select 3 cities because the depot is always included

def calculate_tour_cost(tour):
    """Calculate the travel cost of the tour."""
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Find the minimal travel cost tour
min_cost = float('inf')
best_tour = []

for combo in combinations:
    # Create a tour starting and ending at the depot city 0
    current_tour = [0] + list(combo) + [0]
    current_cost = calculate_tour_cost(current_tour)
    
    # Check if the found tour is better than the best known
    if current_cost < min_cost:
        min_cost = current  cost
        best_tour = current_tour

# Output the tour and the total travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)