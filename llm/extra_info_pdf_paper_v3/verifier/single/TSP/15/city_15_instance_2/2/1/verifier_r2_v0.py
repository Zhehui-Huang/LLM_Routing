import math

# Data
coordinates = [
    (54, 87),  # Depot city 0
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
    (6, 99),   # City 14
]

# Provided solution
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
reported_cost = 322.50

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        total_cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_cost

def test_solution(tour, reported_cost, coordinates):
    # Test that the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test that all cities are visited exactly once
    visited_cities = tour[1:-1]  # Exclude the depot city at the start and end
    if len(visited_cities) != len(set(visited_cities)) or len(set(visited_cities)) != len(coordinates) - 1:
        return "FAIL"
    
    # Test the calculated cost with the reported cost
    calculated_cost = calculate_total_travel_cost(tour, coordinates)
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-2): # Tolerating minor floating-point discrepancies
        return "FAIL"

    return "CORRECT"

# Running the test
result = test_solution(tour, reported_cost, coordinates)
print(result)