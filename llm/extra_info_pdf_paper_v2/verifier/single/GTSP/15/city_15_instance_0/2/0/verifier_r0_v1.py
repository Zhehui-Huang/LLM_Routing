import math

def euclidean_distance(city_a, city_b):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city_b[0] - city_a[0])**2 + (city_b[1] - city_a[1])**2)

def test_solution(tour, total_travel_cost):
    # City coordinates
    city_coords = [
        (9, 93),   # 0 - Depot
        (8, 51),   # 1
        (74, 99),  # 2
        (78, 50),  # 3
        (21, 23),  # 4
        (88, 59),  # 5
        (79, 77),  # 6
        (63, 23),  # 7
        (19, 76),  # 8
        (21, 38),  # 9
        (19, 65),  # 10
        (11, 40),  # 11
        (3, 21),   # 12
        (60, 55),  # 13
        (4, 39)    # 14
    ]
    
    # Grouping of cities
    groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]
    
    # Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    group_visit_track = [0, 0, 0]  # Tracking visits to each group
    
    # Check visit to exactly one city from each group
    for i, group in enumerate(groups):
        if not any(city in tour for city in group):
            return "FAIL"
        # Tracking multiple visits to same group
        group_visit_track[i] = sum(1 for city in tour if city in group)
    
    # Ensure exactly one city from each group is visited
    if not all(count == 1 for count in group_visit_track):
        return "FAIL"
    
    # Calculate and validate total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    
    # Compare the calculated cost with the provided cost (tolerating small floating point error)
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-3):
        return "FAIL"
    
    return "CORRECT"

# Given tour and cost
tour = [0, 8, 10, 9, 0]
total_travel_cost = 114.09

# Test and print the result
result = test_solution(tour, total_travel_cost)
print(result)