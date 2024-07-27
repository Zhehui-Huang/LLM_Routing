import math

# Define the coordinates of the cities
coordinates = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# City groups
city_groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    """ Calculate the total travel cost of a tour. """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

def check_tour_requirements(tour, total_cost, reported_cost):
    """ Check all tour requirements and return "CORRECT" or "FAIL". """
    # Check tour starting and ending at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check that one city from each group is visited
    seen_groups = set()
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for group_id, cities in city_groups.items():
            if city in cities:
                if group_id in seen_groups:
                    return "FAIL"
                seen_groups.add(group_id)
                break
        else:
            # City not found in any group
            return "FAIL"
    
    if len(seen_groups) != 4:
        return "FAIL"
    
    # Check the total travel cost
    calculated_cost = total_tour_cost(tour)
    if not math.isclose(calculated_case, float(reported_cost), abs_tol=0.01):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Solution provided in the test
solution_tour = [0, 6, 13, 2, 9, 0]
solution_cost = 114.66

# Execute the test
test_result = check_tour_requirements(solution_tour, solution_cost, solution_cost)
print(test_result)