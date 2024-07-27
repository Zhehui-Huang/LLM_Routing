import math

def calculate_distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def verify_tour(tour, coordinates, expected_cost):
    """Verify if the tour satisfies all the requirements"""
    # Verify the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify all cities are visited exactly once, except the depot which should be visited twice
    if sorted(tour[1:-1]) != sorted(list(range(1, len(coordinates)))):
        return "FAIL"
    
    # Verify the travel cost calculation by summing the calculated distances of the tour
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    
    # Check if calculated cost is close to the expected cost
    if not math.isclose(total_calculated_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of the cities
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Proposed tour and its total cost
tour = [0, 16, 14, 7, 12, 9, 11, 15, 18, 3, 10, 2, 6, 19, 5, 17, 13, 8, 1, 4, 0]
total_travel_cost = 349.19740471955487  # Corrected variable name here

# Check if the solution meets the requirements
result = verify_tour(tour, coordinates, total_travel_cost)
print(result)