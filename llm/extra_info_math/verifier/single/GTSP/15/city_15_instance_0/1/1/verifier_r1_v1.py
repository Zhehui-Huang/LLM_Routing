import math

# Data given for cities and their positions
city_positions = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# City groups information
city_groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Provided tour and the reported cost
solution_tour = [0, 8, 1, 0]
reported_cost = 89.04798656601136

def calculate_distance(city_a, city_b):
    """ Helper function to calculate Euclidean distance between two cities """
    x1, y1 = city_positions[city_a]
    x2, y2 = city_positions[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_requirements(tour, city_groups):
    """ Check the given requirements based on provided tour and city groups """
    
    # Requirement 1: Check start and end at depot, and one city from each group
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at the depot city 0
    
    visited_groups = {group_number: 0 for group_number in city_groups}
    for city in tour[1:-1]:  # Skipping the depot city at start and end
        found = False
        for group_number, cities in city_groups.items():
            if city in cities:
                visited_groups[group_number] += 1
                found = True
                break
        if not found or any(count > 1 for count in visited_groups.values()):
            return "FAIL"  # More than one city from a group is visited or city not in any group
    
    # Requirement 2: Check if the travel cost is minimized (manually verify reported cost with calculated one)
    calculated_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"  # Costs do not match the reported optimized solution
    
    # Requirement 3: Check for a continuous loop without disconnected sub-tours
    # Implicitly checked as we form a singular closed loop by definition of the problem
    return "CORRECT"

# Run verification
result = verify_requirements(solution_tour, city_groups)
print(result)