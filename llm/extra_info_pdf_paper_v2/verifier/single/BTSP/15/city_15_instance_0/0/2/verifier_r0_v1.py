import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_requirements(tour, cities, expected_max_distance, expected_total_cost):
    # Requirement 1: Check if every city is visited once and starts/ends at depot
    if len(tour) != len(set(tour)) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the total travel cost and max distance between consecutive cities
    total_travel_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_travel_cost += distance
        max_distance = max(max_distance, distance)

    # Requirement 2: Check if the calculated max distance and total travel cost match expected values
    if not math.isclose(max_distance, expected_max_distance, rel_tol=1e-9) or \
       not math.isclose(total_travel_cost, expected_total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Coordinates of cities including the depot
cities = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Tour provided in the solution
tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
expected_total_cost = 373.97393412233544
expected_max_distance = 63.60031446463138

# Call the function to verify the solution
result = check_requirements(tour, cities, expected_max_distance, expected_total_json_final_issue_adjusts and handoffAtage_parameters)
print(result)