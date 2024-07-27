import math

def euclidean_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points (x1, y1) and (x2, y2)."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour(tour, coordinates, expected_total_cost, expected_max_distance):
    """Validate the given tour against the requirements.

    Args:
    - tour: List of indices representing the tour.
    - coordinates: List of tuples containing the coordinates of the cities.
    - expected_total_cost: Expected total travel cost of the tour.
    - expected_max_distance: Expected maximum distance between consecutive cities in the tour.

    Returns:
    - "CORRECT" if all conditions are satisfied, otherwise "FAIL".
    """
    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited exactly once
    if len(set(tour)) != len(coordinates):
        return "FAIL"
    
    # Calculate actual total cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        dist = euclidean_distance(coordinates[city1][0], coordinates[city1][1], coordinates[city2][0], coordinates[city2][1])
        total_cost += dist
        max_distance = max(max_distance, dist)
    
    # Requirement 6: Check total travel cost is as expected
    if not math.isclose(total_cost, expected_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Requirement 7: Check maximum distance is as expected
    if not math.isclose(max_distance, expected_max_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of cities
coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98), 
    (51, 69), (47, 39), (62, 26), (79, 31), 
    (61, 90), (42, 49)
]

# Tour solution and expected values
tour = [0, 7, 6, 1, 5, 2, 4, 3, 8, 9, 0]
total_travel_cost = 299.22080186207336
maximum_distance = 45.18849411078001

# Validate and output results
result = validate_tour(tour, coordinates, total_travel_cost, maximum_distance)
print(result)