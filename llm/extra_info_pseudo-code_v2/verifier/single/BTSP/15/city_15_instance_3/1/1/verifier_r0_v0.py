import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(tour, positions):
    # Requirement 1: Start and end at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city visited exactly once
    visited = set(tour[1:-1])  # exclude start/end city as they should be the same depot city
    if len(visited) != len(tour) - 2 or set(range(1, len(positions))) != visited:
        return "FAIL"
    
    # Calculate total travel cost and max distance for requirements 6 and 7
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = positions[tour[i]]
        x2, y2 = positions[tour[i+1]]
        distance = euclidean_distance(x1, y1, x2, y2)
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Requirement 6: Check total travel cost
    if not math.isclose(total_cost, 318.97002414661307, abs_tol=1e-5):
        return "FAIL"
    
    # Requirement 7: Check maximum distance between consecutive cities
    if not math.isclose(max_distance, 48.373546489791295, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# City positions
positions = [
    (16, 90),  # City 0 - Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79),  # City 14
]

# Given tour and results from the solution
tour = [0, 6, 13, 10, 9, 5, 8, 11, 2, 7, 3, 12, 4, 1, 14, 0]
total_cost = 318.97002414661307
max_distance = 48.373546489791295

# Validate the tour
result = validate_tour(tour, positions)
print(result)