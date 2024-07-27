import math

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def verify_tour(tour, coordinates, expected_cost):
    # Verify the robot starts and ends at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify all cities are visited exactly once except depot, which should be visited twice
    visited = set(tour)
    if len(visited) != len(coordinates) or sorted(visited) != list(range(len(coordinates))):
        return "FAIL"
    
    # Verify the travel cost calculation
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
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
total_travel_cost = 349.19740471955487

# Check if the solution is correct
result = verify_tour(tour, coordinates, total_travel_cost)
print(result)