import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_tour(tour, cities, total_cost):
    # Requirement 1 & 4: Check if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Requirement 2: Check if every city is visited exactly once, except depot city
    visited = set(tour)
    if len(visited) != len(cities) or set(range(len(cities))) != visited:
        return False

    # Calculate the total travel cost using the Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Requirement 3 & 5: Check if the calculated total travel cost matches the reported total travel cost
    if not np.isclose(calculated_cost, total_cost, atol=1e-6):
        return False
    
    # All checks passed
    return True

# Input data
cities = [
    (84, 67), # Depot city 0
    (74, 40), # City 1
    (71, 13), # City 2
    (74, 82), # City 3
    (97, 28), # City 4
    (0, 31),  # City 5
    (8, 62),  # City 6
    (74, 56), # City 7
    (85, 71), # City 8
    (6, 76)   # City 9
]

tour = [0, 8, 3, 7, 1, 2, 4, 5, 6, 9, 0]
total_cost = 60.54552355904021

# Validate the solution
if validate_tour(tour, cities, total_cost):
    print("CORRECT")
else:
    print("FAIL")