import math

# Coordinates of cities
coordinates = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Provided tour and cost
tour = [0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0]
total_cost_claimed = 288.44

def calculate_euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_tour(tour, coordinates):
    """Validate the traveling salesman problem tour."""
    # Check start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "The tour must start and end at the depot"

    # Check if all cities are visited exactly once
    visited = set(tour)
    if len(visited) != 20 or any(city not in visited for city in range(20)):
        return "FAIL", "All cities must be visited exactly once"
    
    # Calculate the total distance of the tour
    actual_cost = sum(calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
    
    # Check if the actual cost is as claimed (considering floating point comparison)
    if not math.isclose(actual_cost, total_cost_claimed, rel_tol=1e-5):
        return "FAIL", f"Actual travel cost {actual_width} differs from claimed {total_cost_claimed}"

    # Additional check: No city visited more than once, except depot
    city_counts = {city: tour.count(city) for city in range(20)}
    del city_counts[0]  # Remove depot count
    if any(count != 1 for count in city_counts.values()):
        return "FAIL", "Some cities are visited more than once"

    return "CORRECT", ""

# Execute the test
result, message = validate_tour(tour, coordinates)
print(result)