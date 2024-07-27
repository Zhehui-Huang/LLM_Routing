import math
from itertools import permutations

# List of coordinates for the cities
coordinates = [
    (54, 87),  # City 0 - Depot
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
    (6, 99)   # City 14
]

def euclidean_distance(coord1, coord2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def calculate_tour_cost(tour, coordinates):
    """Calculate total cost and max distance for a given tour."""
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return total_cost, max_distance

def find_best_tour(coordinates):
    n = len(coordinates)
    all_possible_tours = permutations(range(1, n))  # Generate all permutations of the cities except the depot
    
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')
    
    # Check each possible tour
    for tour in all_possible_tours:
        current_tour = [0] + list(tour) + [0]  # Create a full tour starting and ending at depot (City 0)
        total_cost, max_distance = calculate_tour_cost(current_tour, coordinates)
        
        if max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < best_total_cost):
            best_max_distance = max_distance
            best_total_cost = total_cost
            best_tour = current_tour
    
    return best_tour, best_total_cost, best_max_loss_distance

# Find the optimal tour and its costs
best_tour, total_cost, max_distance = find_best_tour(coordinates)

# Output results
print("Tour:", best_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)