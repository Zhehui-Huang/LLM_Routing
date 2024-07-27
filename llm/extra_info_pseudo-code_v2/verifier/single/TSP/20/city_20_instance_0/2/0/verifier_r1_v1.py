import numpy as np

def euclidean_distance(c1, c2):
    """Calculate Euclidean distance between two points."""
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution(tour, total_cost, coords):
    # [Requirement 1] The robot must start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Each city must be visited exactly once (excluding depot which must be visited twice)
    if len(set(tour[1:-1])) != len(coords) - 1 or len(tour) - 1 != len(coords):
        return "FAIL"

    # Calculate the route cost using the Euclidean distances
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(coords[tour[i]], coords[tour[i+1]])

    # [Requirement 5] Check if calculated cost closely matches the provided total cost
    if not np.isclose(calculated_cost, total_cost, atol=0.01):  # Tolerance for floating point arithmetic
        return "FAIL"

    # The requirements are all satisfied
    return "CORRECT"

# Coordinates for each city
cities_coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), 
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Provided tour and calculated travel cost
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 349.2

# Verify the solution
result = verify_solution(tour, total_travel_cost, cities_coordinates)
print(result)