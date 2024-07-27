import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, city_coordinates):
    # Verify Requirement 1: Start and End at Depot City 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot city 0."

    # Verify Requirement 2: Visit exactly 7 cities, including the depot
    if len(tour) != 8 or len(set(tour)) != 8:  # Includes start and end at the depot city
        return "FAIL: Tour does not visit exactly 7 different cities including the depot."

    # Requirement 4: Check tour list format
    if not isinstance(tour, list) or not all(isinstance(city, int) for city in tour):
        return "FAIL: Tour format is incorrect."

    # Requirement 5: Check the total travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return f"FAIL: Total travel cost is incorrect. Expected approximately {calculated_cost}, got {total_cost}."

    return "CORRECT"

# City coordinates index corresponds to city number
city_coordinates = [
    (14, 77),  # Depot city 0
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

# Example test solution
tour_example = [0, 6, 2, 13, 8, 9, 14, 0]
total_cost_example = 130.6658168109853

# Verification
print(verify_solution(tour_example, total_cost_example, city_coordinates))