import math

def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

def verify_solution(tour, total_cost, city_coordinates, groups):
    # Check if tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check for exactly one city from each group
    selected_cities = tour[1:-1]  # exclude the depot city from start and end
    grouped = set([next((group_idx for group_idx, group in enumerate(groups) if city in group), -1)
                   for city in selected_cities])
    if len(grouped) != len(groups) or -1 in grouped:
        return "FAIL"
    
    # Calculate and check the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    # Allow a margin for floating-point comparison detail
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Data
city_coordinates = [
    (16, 90),  # Depot city 0
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
    (32, 79)   # City 14
]
groups = [
    [1, 6, 14],  # Group 0
    [5, 12, 13], # Group 1
    [7, 10],     # Group 2
    [4, 11],     # Group 3
    [2, 8],      # Group 4
    [3, 9]       # Group 5
]

# Provided solution to test
tour = [0, 14, 5, 10, 11, 8, 9, 0]
total_cost = 166.76

# Test the solution
result = verify_solution(tour, total_cost, city_coordinates, groups)
print(result)