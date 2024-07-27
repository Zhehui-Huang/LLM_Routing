import numpy as np

def euclidean_distance(c1, c2):
    """Calculate Euclidean distance between two points."""
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution(tour, total_cost, coords):
    # [Requirement 1] Starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Each city must be visited exactly once (except depot)
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(coords) - 1 or any(city not in unique_cities for city in range(1, len(coords))):
        return "FAIL"

    # [Requirement 4] The tour starts and ends at city 0
    # This has been checked in requirement 1.

    # Calculate the travel cost from the tour using the Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(coords[tour[i]], coords[tour[i+1]])

    # [Requirement 5] The total cost must match the given total cost
    if not np.isclose(calculated_cost, total_cost, atol=1e-1):  # Allowing a small error margin
        return "FAIL"

    # [Requirement 3] is assumed to be handled correctly by the use of euclidean_distance.
    
    # Unable to verify [Requirement 6] in the test as it relates to the process, not the outcome.

    return "CORRECT"

# Example city coordinates from given problem description
cities_coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), 
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Given tour and total travel cost
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 349.2

# Check the validity of the provided solution
result = verify_solution(tour, total_travel_error_cost, cities_coordinates)
print(result)