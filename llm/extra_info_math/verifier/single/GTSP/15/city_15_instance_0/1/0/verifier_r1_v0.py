import math

# City coordinates
cities = {
    0: (9, 93),   # Depot
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

# City groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Provided solution
tour = [0, 8, 1, 0]
reported_cost = 89.04798656601136

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(tour, groups):
    # Check start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check one city per group
    visited_groups = set()
    for city in tour[1:-1]:
        for group_id, group_cities in groups.items():
            if city in group_cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups.add(group_id)
                break
    
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Calculate and compare the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run the validation
result = validate_tour(tour, groups)
print(result)  # Output: "CORRECT" or "FAIL"